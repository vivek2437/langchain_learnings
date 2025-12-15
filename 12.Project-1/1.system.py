from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

# Step 1: Fetch transcript
video_id = "DlIAd4Rtkr8"

try:
    yt_api = YouTubeTranscriptApi()
    transcript_list = yt_api.fetch(video_id)

    transcript = " ".join(item.text for item in transcript_list)

except TranscriptsDisabled:
    raise RuntimeError("Transcript is disabled for this video.")
except Exception as e:
    raise RuntimeError(f"Transcript error: {e}")

# Step 2: Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=50
)

documents = splitter.create_documents([transcript])
print(f"Chunks created: {len(documents)}")

# Step 3: Embeddings + Vector Store
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-l6-v2"
)

vector_store = FAISS.from_documents(
    documents=documents,
    embedding=embedding_model
)

# Step 4: Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# Step 5: Prompt
prompt = PromptTemplate(
    template="""
You are a helpful assistant.
Answer ONLY using the context below.

Context:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)

question = "What is the video talking about?"

docs = retriever.invoke(question)
context_text = "\n\n".join(doc.page_content for doc in docs)

final_prompt = prompt.invoke({
    "context": context_text,
    "question": question
})

# Step 6: LLM
model = ChatOllama(model="gemma:2b")
answer = model.invoke(final_prompt)

print(answer.content)