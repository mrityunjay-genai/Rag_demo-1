def build_prompt(context_chunk,query):
    context = "\n\n".join(context_chunk)
    # print(context)
    prompt = f"""Use the following context to answere the question
    
    Context:
    {context}

    Question:
    {query}

    Answere:
    """ 
    return prompt