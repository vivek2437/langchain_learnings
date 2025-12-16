from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1"
)

@tool

def add(x:int , y:int) -> int:
    """Add two numbers."""
    return x + y

llm_with_tools = llm.bind_tools([add])

user_query="can you add the 10 & 97?"
query= HumanMessage(user_query)

messages= [query]

result= llm_with_tools.invoke(messages)
messages.append(result)

toll_result= add.invoke(result.tool_calls[0])

messages.append(toll_result)
final_result= llm.invoke(messages)

print(final_result)