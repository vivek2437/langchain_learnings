from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# model
model = ChatOllama(
    model="gemma:2b"
)

# prompt template
chat_template = ChatPromptTemplate.from_messages([
    ('system', "you are a helpful {domain} expert."),
    ('human', "explain in simple terms, the concept of {topic}")
])

# domain and topic
prompt = chat_template.invoke({
    'domain': "quantum computing",
    'topic': "superposition"
})

# show messages
print("Messages:", prompt.messages)

# correct call
result = model.invoke(prompt.messages)

print("\nModel Output:\n", result.content)