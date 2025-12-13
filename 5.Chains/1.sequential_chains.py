# Import necessary LangChain components for building sequential chains
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the ChatOllama model with gemma:2b
model= ChatOllama(
    model="gemma:2b"
)

# First prompt: Generate a detailed report on a given topic
prompt1= PromptTemplate(template="genarate 3 detailed report on a {topic}",
                        input_variables=["topic"],
)

# Second prompt: Summarize the report output from the first step
prompt2= PromptTemplate(template="summarize the following report in one sentence: {report}",
                        input_variables=['text'],
)

# Output parser to extract string content from model responses
parser=StrOutputParser()

# Sequential chain: prompt1 -> model -> prompt2 -> model -> parser
# Data flows linearly through each step
chain= prompt1 | model | prompt2 | model | parser

# Execute the chain with a topic about an interstellar object
result= chain.invoke({'topic':'3I Atlas Interstellar object'})

# Display the final summarized output
print(result)