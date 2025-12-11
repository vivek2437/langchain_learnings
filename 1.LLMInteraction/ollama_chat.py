from langchain_ollama import ChatOllama

model = ChatOllama(
    model="gemma:2b"
)

prompt = "do you remember what is my name?"
result = model.invoke(prompt)

print(result.content)