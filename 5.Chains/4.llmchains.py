from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

model= ChatOllama(
    model="gemma:2b"
)

prompt=PromptTemplate(
    template="suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

chain= LLMChain(llm=model, prompt=prompt)

topic="3I Atlas Interstellar object"

responce= chain.invoke({'topic':topic})

print(responce)