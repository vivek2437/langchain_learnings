# Import necessary components for building conditional branching chains
from typing_extensions import Literal
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnablePassBranch, RunnableLambda
from pydantic import BaseModel, Field

# Initialize the ChatOllama model for sentiment classification and response generation
model = ChatOllama(
    model="gemma:2b"
)

# Generic parser (not used in this example)
parser= PydanticOutputParser()

# Pydantic model defining the Feedback schema with sentiment field
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="the sentiment of the feedback provided")

# Pydantic parser to parse model output into Feedback object
parser2=PydanticOutputParser(pydantic_object=Feedback)

# First prompt: Classify customer feedback sentiment
prompt1=PromptTemplate(
    template="classify the sentiment of the following customer feedback as positive or negative: {feedback}",
    input_variables=["feedback"],
    partial_variables={"responce_format": parser2.get_format_instructions()}
)

# Classifier chain: analyzes sentiment and returns structured Feedback object
classfier_chain= prompt1 | model | parser2

# Second prompt: Generate a response for positive feedback
prompt2=PromptTemplate(
    template="Generate a concise  postive response to the following customer feedback: {feedback}\nSentiment: {sentiment}",
    input_variables=["feedback"]
)

# Third prompt: Generate a response for negative feedback
prompt3=PromptTemplate(
    template="Generate a concise  negative response to the following customer feedback: {feedback}\nSentiment: {sentiment}",
    input_variables=["feedback"]
)

# Conditional branching chain: routes to different prompts based on sentiment
# If positive -> prompt2, if negative -> prompt3, else -> fallback message
branch_chain= RunnablePassBranch(
    (lambda x: x.sentiment == "positive" , prompt2 | model | parser),
    (lambda x: x.sentiment == "negative" , prompt3 | model | parser),
    RunnablePassBranch(lambda x: True, RunnableLambda(lambda x: "No valid sentiment found") )
)

# Full chain: classify sentiment, then branch to appropriate response generator
chain= classfier_chain | branch_chain

# Invoke with negative feedback example
result= chain.invoke({'feedback':'The product quality was terrible and I am very disappointed.'})

# Display the generated response
print(result)