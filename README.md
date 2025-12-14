# LangChain Experiments 

A hands-on learning repository exploring LangChain with Ollama's local LLM models. This collection demonstrates core concepts including prompt engineering, chat interfaces, structured outputs, output parsing strategies, and chain patterns (sequential, conditional, parallel), plus runnable patterns for concurrent executions.

## Prerequisites
- Python 3.10+.
- Ollama installed and running locally; pull the model once: `ollama pull gemma:2b`.
- (Optional) Google GenAI access if you plan to extend with `langchain_google_genai`.

## Setup
1) Create and activate a virtual environment (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
If you hit an execution policy warning, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2) Install dependencies inside the venv:
```powershell
pip install -r requirements.txt
```

## Running the Examples
- Minimal single prompt: `python 1.LLMInteraction/ollama_chat.py`
- Chat REPL with running memory: `python 2.Chatbots/1.chatbot.py` (type `exit` or `quit` to stop)
- Prompt template demo: `python 2.Chatbots/2.chatprompttemp.py`
- Messages placeholder demo: ensure the invoke key matches `chatbot_history` in [2.Chatbots/messageplaceholde.py](2.Chatbots/messageplaceholde.py), then run it to see the rendered prompt.
- Structured output (TypedDict, simple): `python 3.StructuredOutputs/1.structuredoutput.py`
- Structured output (TypedDict, detailed): `python 3.StructuredOutputs/2.deatailed_output_structured.py`
- Structured output (Pydantic, literals): `python 3.StructuredOutputs/3.strucutred_op.py`
- Output parser chain (double pass): `python 4.Outputparsers/1.stroutparsers.py`
- JSON facts with structured parser: `python 4.Outputparsers/structureoutputparsers.py`
- Sequential chain (report + summary): `python 5.Chains/1.sequential_chains.py`
- Conditional chain (sentiment routing): `python 5.Chains/2.conditional_chains.py`
- Parallel chain (notes + questions): `python 5.Chains/3.parallel_chain.py`
- Parallel runnables (tweet + LinkedIn): `python 8.Runnables/2.runnnables_parallel.py`

## Troubleshooting
- Import underlined (e.g., `langchain_google_genai`): activate the venv, then `pip install langchain-google-genai` (already in `requirements.txt`). Restart the editor’s language server if it stays yellow.
- Model not found: start Ollama and pull `gemma:2b`.
- Permissions when activating venv: use the `Set-ExecutionPolicy` command shown above.

## Notes / Learnings
- `ChatPromptTemplate` cleanly separates system instructions and user variables.
- Passing `chat_history` (list of messages) lets the model keep short-term context; storing it in a file (like `chatbot_history.txt`) is a quick way to persist across runs.
- LangChain chat models accept message lists (System/Human/AI), which maps naturally to `ChatOllama` invocations.
- `with_structured_output` enforces response shapes; start simple with `TypedDict`, then move to `BaseModel` when you need stricter validation.
- `StructuredOutputParser` plus `OutputFixingParser` can repair slightly off-spec generations by re-parsing through the LLM.
- **Sequential chains** pass output from one step as input to the next (linear flow: A → B → C).
- **Conditional chains** use `RunnablePassBranch` to route data through different paths based on runtime conditions (if-else logic).
- **Parallel chains** with `RunnableParallel` execute multiple branches concurrently, then merge results—ideal for independent tasks like generating notes and questions simultaneously.