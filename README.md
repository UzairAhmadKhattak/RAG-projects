How to use `pg_vector`

### 1. Run `pg_vector` in Docker
- **Start container**: Pull the `pg_vector` image and run it as a container.
- **Configure connection**: Provide username, password, port, and database name when starting the container.

### 2. Prepare the database
- **Create vector extension**: In the database, run the `CREATE EXTENSION IF NOT EXISTS vector;`

### 3. Environment variables
Create a `.env` file with values similar to:

```env
openai_api_key=YOUR_OPENAI_API_KEY
database_url=postgresql+psycopg://postgres:test@localhost:5432/db_vector
collection_name=resume_chunks
resume_file_name=UzairAhmad-SoftwareEngineer.pdf
```

### 4. What the script does some stepes are not visiable but this is what the concept
1. **Load the resume** using a LangChain PDF loader.
2. **Split the resume into chunks**.
3. **Embed the chunks** using an OpenAI embedding model.
4. **Store the chunks** and their embeddings in a Postgres vector table.
5. **Convert the user query into a vector** using the same embedding model.
6. **Query the vector table** for the most similar chunks to that query.
7. **Return the most similar chunks** as the answer to the user.