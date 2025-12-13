# Import necessary components for building parallel execution chains
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# Initialize the ChatOllama model for generating educational content
model = ChatOllama(model="gemma:2b")

# String output parser to extract text content from model responses
parser = StrOutputParser()

# First prompt: Generate educational notes for a given topic
prompt_notes = PromptTemplate(
    template="Generate short and simple notes for the following topic:\n{topic}",
    input_variables=["topic"]
)

# Second prompt: Generate quiz questions for the same topic (runs in parallel with notes)
prompt_questions = PromptTemplate(
    template="Generate short quiz questions for the following topic:\n{topic}",
    input_variables=["topic"]
)

# Third prompt: Merge the parallel outputs (notes + questions) into a final document
prompt_merge = PromptTemplate(
    template="""
Create a quiz-style document using the content below.

NOTES:
{notes}

QUESTIONS:
{questions}
""",
    input_variables=["notes", "questions"]
)

# Parallel chain: executes notes and questions generation simultaneously
# Both branches receive the same {topic} input and run concurrently
parallel_chain = RunnableParallel(
    notes=prompt_notes | model | parser,       # Branch 1: Generate notes
    questions=prompt_questions | model | parser  # Branch 2: Generate questions
)

# Full chain: parallel execution followed by merging step
# Flow: topic -> [notes & questions in parallel] -> merge -> final document
final_chain = parallel_chain | prompt_merge | model | parser

# Execute the chain with a topic about the Solar System
result = final_chain.invoke(
    {"topic": "The Solar System"}
)

# Display the final quiz-style document with merged notes and questions
print(result)