# 5) convert the user query into a vector
# 6) query the vector table for the most similar chunks
# 7) return the most similar chunks to the user

from embedding.embedding_in_pg_vector import return_vector_store
vector_store = return_vector_store()

def function_query_vector_store(query):
    results = vector_store.similarity_search(query)
    return results

if __name__ == "__main__":
    # query the vector store for the most similar chunks
    query = "what is the the user experience related to cloud computing?"
    results = function_query_vector_store(query)
    # print(results)
    print(len(results))
    print(results[0].page_content)
    print("--------------------------------")
    print(results[1].page_content)
    print("--------------------------------")
    print(results[2].page_content)
    print("--------------------------------")
    print(results[3].page_content)

