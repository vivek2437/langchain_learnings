from langchain_ollama import ChatOllama
from typing import TypedDict , Annotated ,Literal , Optional
from pydantic import BaseModel

model=ChatOllama(
        model="gemma:2b"
)

class Review(BaseModel):
    key_themes: Annotated[list[str], "write down 3 keys themes discussed in the review in a list"]
    summary: Annotated[str, "Brief summary of the review."]
    sentiment: Annotated[Literal["positive", "negative"], "Overall sentiment: positive or negative."]
    pros: Annotated[Optional[list[str]], "All pros mentioned in the review."]
    cons: Annotated[Optional[list[str]], "All cons mentioned in the review."]


st_model=model.with_structured_output(Review)

prompt="""
I recently bought the Google Pixel 8, and the camera is absolutely amazing.
The photos are sharp, the night mode is incredible, and the AI editing tools are very useful.

However, the battery life is disappointing. It barely lasts a day with moderate usage, 
and the charging speed is slower compared to other flagship phones.

The display quality is excellent, and the software experience is clean and smooth, 
but the phone gets warm quickly when recording 4K videos.
"""

result= st_model.invoke(prompt)

print(result)