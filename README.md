# LangChain Examples (Windows)

Hands-on examples exploring LangChain with Ollama local LLMs. Covers prompt templates, chat interfaces, structured outputs, output parsers, chains (sequential/conditional/parallel), and runnable patterns.

## Repository Structure
- 1.LLMInteraction: basic chat with Ollama
- 2.Chatbots: REPL chatbot + prompt templates
- 3.StructuredOutputs: TypedDict and Pydantic outputs
- 4.Outputparsers: parsing and fixing generated outputs
- 5.Chains: sequential, conditional, and parallel chains
- 6.Embeddings: Hugging Face embeddings example
- 7.Basic RAG: minimal retrieval-augmented generation
- 8.Runnables: sequences and parallel runnables

## Prerequisites
- Python 3.10+
- Ollama installed and running; pull a model once: ollama pull gemma:2b
- Optional: Google GenAI access for langchain_google_genai

## Setup (PowerShell)
`powershell
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
`
If you hit an execution policy warning:
`powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
`

## Environment
You can store API keys in a .env file (e.g., GOOGLE_API_KEY=...). This repository ignores .env and env/ by default.

## Quickstart
- Basic chat: python 1.LLMInteraction/ollama_chat.py
- Chatbot REPL: python 2.Chatbots/1.chatbot.py (type exit/quit to stop)
- Prompt templates: python 2.Chatbots/2.chatprompttemp.py
- Structured outputs:
  - python 3.StructuredOutputs/1.structuredoutput.py
  - python 3.StructuredOutputs/2.deatailed_output_structured.py
  - python 3.StructuredOutputs/3.strucutred_op.py
- Output parsers:
  - python 4.Outputparsers/1.stroutparsers.py
  - python 4.Outputparsers/2.structureoutputparsers.py
- Chains:
  - python 5.Chains/1.sequential_chains.py
  - python 5.Chains/2.conditional_chains.py
  - python 5.Chains/3.parallel_chain.py
- Runnables:
  - python 8.Runnables/1.runnables_sequences.py
  - python 8.Runnables/2.runnnables_parallel.py

## Troubleshooting
- Missing imports (e.g., langchain_google_genai): ensure venv is active, then pip install -r requirements.txt
- Ollama model not found: start Ollama and run ollama pull gemma:2b
- venv activation permissions: use Set-ExecutionPolicy as shown above

---
Maintained as a personal learning sandbox. Contributions welcome.
