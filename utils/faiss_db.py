import faiss
import numpy as np
import pickle
import os

from utils.embedding import get_embeddings
from utils.chunking import chunk_text
from utils.data_read import data_read

def load_faiss_index():
    index_path = "faiss_store/index.faiss"
    mapping_path = "faiss_store/chunk_mapping.pkl"

    valid = os.path.exists(index_path) and os.path.getsize(index_path)>0
    valid = os.path.exists(mapping_path) and os.path.getsize(mapping_path) >0

    if valid:
        try:
            index = faiss.read_index(index_path)
            with open(mapping_path, "rb") as f:
                chunk_mapping = pickle.load(f)
            return index,chunk_mapping
        except Exception as e:
            print("Corrupted Index detected. Rebuilding.....",e)
    
    ## Creating Index -------------------------------
    print("Generating new FAISS index from operation_sindoor.txt.....")
    
    # Data read from file
    raw_text = data_read()
    
    # Data Chunking
    chunks = chunk_text(raw_text)

    # Vector DB
    chunk_mapping = []
    all_embeddings = []

    for chunk in chunks:
        emb = get_embeddings(chunk)
        all_embeddings.append(emb)
        chunk_mapping.append(chunk)

    all_embeddings = np.array(all_embeddings).astype("float32")
    dimension = all_embeddings.shape[1]
    
    #index creation
    index = faiss.IndexFlatL2(dimension)
    index.add(all_embeddings)

    os.makedirs("faiss_store",exist_ok=True)
    # write index
    faiss.write_index(index,index_path)

    with open(mapping_path, "wb") as f:
        pickle.dump(chunk_mapping,f)

    print("Index built and saved.")
    return index, chunk_mapping




