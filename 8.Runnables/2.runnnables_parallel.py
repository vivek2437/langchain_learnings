from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

# Build lightweight prompt templates for two social channels
prompt1 = PromptTemplate(
    template="genrate the tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="genrate the linkedin post about {topic}",
    input_variables=["topic"]
)

# Initialize the local LLM via Ollama
model = ChatOllama(
    model="gemma:2b"
)

# Parser to extract plain text from each model response
parser = StrOutputParser()

# Run both prompts in parallel: each branch returns text for its channel
parallel_chain = RunnableParallel(
    {
        'tweet': prompt1 | model | parser,
        'linkedin_post': prompt2 | model | parser
    }
)

# Invoke with a single topic; both branches execute concurrently
result = parallel_chain.invoke({'topic': 'artificial intelligence'})

# Display the combined outputs (dict with tweet and linkedin_post)
print(result)