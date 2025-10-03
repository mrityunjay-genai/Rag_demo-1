import streamlit as st
from utils.chunking import chunk_text
from utils.completion import generate_completion
from utils.data_read import data_read
from utils.embedding import get_embeddings
from utils.faiss_db import load_faiss_index
from utils.prompt import build_prompt
from utils.retrieval import retrieve_chunks

st.title("RAG App, Operation Sindoor Story")
st.write("Ask question related to the Operation Sindoor")

query = st.text_input("Enter your Question  here")

if query:
    index, chunk_mapping = load_faiss_index()
    top_k_chunks = retrieve_chunks(query, index, chunk_mapping)
    prompt = build_prompt(top_k_chunks,query)
    response = generate_completion(prompt)

    st.subheader("Answere")
    st.write(response)

    with st.expander("Retrived Chunks"):
        for chunk in top_k_chunks:
            st.markdown(f"- {chunk}")