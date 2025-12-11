from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model= ChatOllama(
    model="gemma:2b"
)

chat_history=[
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input=input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit','quit']:
        print("Exiting chat...")
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("Bot:",result.content)


print("Chat History", chat_history)