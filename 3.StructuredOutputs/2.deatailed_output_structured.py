from langchain_ollama import ChatOllama
from typing import TypedDict, Optional
from typing_extensions import Annotated

# Create the model
model = ChatOllama(
    model="gemma:2b"
)

# Schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "List all important concepts discussed in the review."]
    summary: Annotated[str, "Brief summary of the review."]
    sentiment: Annotated[str, "Overall sentiment: positive or negative."]
    pros: Annotated[Optional[list[str]], "All pros mentioned in the review."]
    cons: Annotated[Optional[list[str]], "All cons mentioned in the review."]

# Structured output model
structured_model = model.with_structured_output(Review)

# Google Pixel review text
prompt = """
I recently bought the Google Pixel 8, and the camera is absolutely amazing.
The photos are sharp, the night mode is incredible, and the AI editing tools are very useful.

However, the battery life is disappointing. It barely lasts a day with moderate usage, 
and the charging speed is slower compared to other flagship phones.

The display quality is excellent, and the software experience is clean and smooth, 
but the phone gets warm quickly when recording 4K videos.
"""

# Use structured model (IMPORTANT)
result = structured_model.invoke(prompt)

print("Structured Output:")
print(result)