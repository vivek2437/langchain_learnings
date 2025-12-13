from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model= ChatOllama(
    model="gemma:2b"
)

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(gt=18 , lt=100 ,description="The person's age in years must be grater then 18")
    city: str = Field(..., description="The person's city of residence")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate (template="""
give me the name , age and city of residence of a fictinal {place} person. make sure  the age is greater than 18 and less than 100. return response in following format: {response_format}
""",
input_variables=["place"],
partial_variables={"response_format": parser.get_format_instructions()}
)

chain = template | model | parser

result=chain.invoke({"place":"New York"})

print(result)