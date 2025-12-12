from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat_example
chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chatbot_history"),
    ('human', '{query}')
])

# load the history
chat_history = []

with open("chatbot_history.txt") as file:
    lines = file.readlines()
    # convert each line into a human or ai message
    chat_history = [{"role": "user", "content": line.strip()} for line in lines]

# FIX: USE THE SAME VARIABLE NAME AS THE PLACEHOLDER
prompt = chat_template.invoke({
    'chatbot_history': chat_history,
    'query': "where is my refund?"
})

print(prompt)