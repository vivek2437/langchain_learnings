from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#chat model initialization
model=ChatOllama(
    model="gemma:2b"
)

#1st template
template1=PromptTemplate(template="write a deatailed report on {topic}",
                        input_variables=['topic'])

#2nd prompt
template2=PromptTemplate(template="write a 4 point summary on the follwing {text}",
                         input_variables=['text'])

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser



result=chain.invoke({"topic":"the impact of climate change on global agriculture"})

print(result) 
