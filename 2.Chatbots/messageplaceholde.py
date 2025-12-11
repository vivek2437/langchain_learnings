from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat_example
chat_template=ChatPromptTemplate([
    'system',"You are a helpful assistant.",
    MessagesPlaceholder(variable_name="chatbot_history"),
    ('human', '{query}')
])


#load the history

chat_history=[]

with open("chatbot_history.txt")as file:
    chat_history.extend(file.readlines())

prompt=chat_template.invoke({
    'chat_history': chat_history,
    'query':"where is my refund?"
})

print(prompt)