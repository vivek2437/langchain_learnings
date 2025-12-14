from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings= HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-l6-v2')

text=" delhi is the capital of india"


documents=["delhi is the capital  india",
           "paris is the capital of france",
           "berlin is the capital of germany",
           "madrid is the capital of spain"
           ]

result= embeddings.embed_query(text)

# print(str(result))

result_doc= embeddings.embed_documents(documents)

print(str(result_doc))

similarity_scores= cosine_similarity([result], result_doc)

print(str(similarity_scores))