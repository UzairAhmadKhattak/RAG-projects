from embedding.embedding_in_pg_vector import return_vector_store

vector_store = return_vector_store()

if __name__ == "__main__":
    # query the vector store for the most similar chunks
    query = "what is the the user experience related to cloud computing?"
    results = vector_store.similarity_search(query)
    # print(results)
    print(len(results))
    print(results[0].page_content)
    print("--------------------------------")
    print(results[1].page_content)
    print("--------------------------------")
    print(results[2].page_content)
    print("--------------------------------")
    print(results[3].page_content)

