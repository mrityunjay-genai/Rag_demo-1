from utils.embedding import get_embeddings
import numpy as np


def retrieve_chunks(query, index, chunk_mapping, k=3):
    query_vec = get_embeddings(query)
    distances, indices = index.search(np.array([query_vec]).astype("float32"), k)
    return [chunk_mapping[i] for i in indices[0]]