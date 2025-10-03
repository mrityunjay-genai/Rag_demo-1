def chunk_text(text, max_words=10):
    words = text.split()
    # chunks = []
    # for i in range(0, len(words), max_words):
    #     chunks.append(" ".join(words[i:i+max_words]))
    # return chunks
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]