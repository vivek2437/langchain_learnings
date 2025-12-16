from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def add(x: int, y: int) -> int:
    """Add two integers and return the result."""
    return x + y

llm = ChatOllama(
    model="llama3.1",   # ← TOOL-CAPABLE MODEL
    temperature=0
)

llm_with_tools = llm.bind_tools([add])

response = llm_with_tools.invoke("Add 3 and 147")

tool_call = response.tool_calls[0]
result = add.invoke(tool_call["args"])

print("Final Answer:", result)