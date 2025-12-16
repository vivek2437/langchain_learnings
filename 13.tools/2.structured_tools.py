from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

# 1. Input schema
class MultiplyInput(BaseModel):
    x: int = Field(..., description="The first integer to multiply")
    y: int = Field(..., description="The second integer to multiply")

# 2. Business logic
def multiply(x: int, y: int) -> int:
    """Multiply two integers."""
    return x * y

# 3. Create structured tool
multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply_tool",
    description="Multiplies two integers and returns the result",
    args_schema=MultiplyInput
)

# 4. Invoke tool
result = multiply_tool.invoke({"x": 6, "y": 7})

print(f"The result of multiplication is: {result}")