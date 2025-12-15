from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="The Eiffel Tower is located in Paris, France.", metadata={"location": "Paris"}),
    Document(page_content="The Great Wall of China is a historic fortification in China.", metadata={"location": "China"}),
    Document(page_content="Machu Picchu is an ancient Incan city located in Peru.", metadata={"location": "Peru"}),
    Document(page_content="The Statue of Liberty is a symbol of freedom in New York, USA.", metadata={"location": "USA"}),
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-l6-v2"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,         
    collection_name="sample"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "famous landmarks in China"
results = retriever.invoke(query)

print(results)


for doc in results:
    print(doc.page_content, doc.metadata)