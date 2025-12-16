from langchain_core.tools import tool

@tool
def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y

@tool
def subtract(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


class MathTools:
    def get_tools(self):
        return [add, subtract]


toolkit = MathTools()
tools = toolkit.get_tools()

for tl in tools:
    print(tl.name, "-->", tl.description)
