from langchain_community.document_loaders import TextLoader

loader = TextLoader("docs.txt")
docs = loader.load()

print(docs)
print(docs[0].page_content)