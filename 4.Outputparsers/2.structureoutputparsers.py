from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.output_parsers import OutputFixingParser

model = ChatOllama(
    model="gemma:2b"
)

schemas = [
    ResponseSchema(name="fact1", description="first important fact about black holes"),
    ResponseSchema(name="fact2", description="second important fact about black holes"),
    ResponseSchema(name="fact3", description="third important fact about black holes"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)
safe_parser = OutputFixingParser.from_llm(llm=model, parser=parser)

template = PromptTemplate(
    template="""
    Give me exactly 3 facts about {topic}. 
    Return ONLY JSON that matches this format:  
    {response_format}
    """,
    input_variables=["topic"],
    partial_variables={"response_format": parser.get_format_instructions()},
)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})
print(result)