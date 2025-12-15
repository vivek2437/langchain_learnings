from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader("Profile.pdf")
docs = loader.load()

print(docs)