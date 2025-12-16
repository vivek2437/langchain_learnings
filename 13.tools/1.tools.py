from langchain_core.tools import tool

@tool
def multiply_tool(x: int, y: int) -> int:
    """Multiply two integers and return the result."""
    return x * y

result = multiply_tool.invoke({"x": 6, "y": 7})

print(f"The result of multiplication is: {result}")