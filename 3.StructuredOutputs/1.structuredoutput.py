from langchain_ollama import ChatOllama
from typing import TypedDict

#create the model
model = ChatOllama(
    model="gemma:2b"
)

#schema 
class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)


prompt="""
This hardware is greate , but the software feels kind of bloated. so many boilerplate apps. and my phone keeps hanging when i play PUBG.
"""

# result=structured_model.invoke(prompt)

# print("Structured Output:\n", result)

new_prompt=f"generate sentiment and summary of the review given.The review is '{prompt}'"
result=model.invoke(new_prompt)

print(result)