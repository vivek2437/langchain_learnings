from langchain_community.retrievers import WikipediaRetriever

r= WikipediaRetriever( top_k_results=2 , lang='en')

query= "ipl"

docs=r.invoke(query)

print(docs)

for i,doc in enumerate(docs):
    print(f"-------result: {i+1}")
    print("content:",doc.page_content)