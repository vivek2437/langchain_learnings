from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 1. Load document
loader = TextLoader(
    "C:/Users/ASUS/OneDrive/Desktop/langchain/docs.txt"
)
documents = loader.load()

# 2. Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

# 3. Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_documents(docs, embeddings)

# 4. Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. LLM
llm = ChatOllama(model="gemma:2b")

# 6. Prompt
prompt = PromptTemplate.from_template(
    """Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""
)

# 7. RAG chain (LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# 8. Query
query = "What are the key takeaways from the document?"
response = rag_chain.invoke(query)

print(response)

# print(response["result"])

# print(response["context"])