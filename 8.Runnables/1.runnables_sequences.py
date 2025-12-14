from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


prompt1= PromptTemplate(
    template="genrate the joke about the {topic}",
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template="exaplin the following the joke {topic}",
    input_variables=["topic"]
)

model=ChatOllama(
    model="gemma:2b"
)

parser=StrOutputParser()

chain= RunnableSequence(prompt1 ,model , parser , prompt2 , model , parser)

result= chain.invoke({'topic':'monkey'})
print(result)