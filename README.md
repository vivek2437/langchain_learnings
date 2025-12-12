# LangChain Experiments (CyberPulse-Sniffer)

Small LangChain + Ollama exercises covering single-turn prompts, prompt templates, structured outputs, and output-parsing workflows.

## Repository Layout
- [1.LLMInteraction/ollama_chat.py](1.LLMInteraction/ollama_chat.py) — single prompt to the local Ollama `gemma:2b` model.
- [2.Chatbots/1.chatbot.py](2.Chatbots/1.chatbot.py) — simple REPL chat loop that maintains `chat_history` and exits on `exit`/`quit`.
- [2.Chatbots/2.chatprompttemp.py](2.Chatbots/2.chatprompttemp.py) — uses `ChatPromptTemplate` for domain/topic-driven responses.
- [2.Chatbots/messageplaceholde.py](2.Chatbots/messageplaceholde.py) — shows `MessagesPlaceholder`; adjust the key to `chatbot_history` when invoking so it matches the placeholder.
- [3.StructuredOutputs/1.structuredoutput.py](3.StructuredOutputs/1.structuredoutput.py) — minimal `TypedDict` schema with `with_structured_output`.
- [3.StructuredOutputs/2.deatailed_output_structured.py](3.StructuredOutputs/2.deatailed_output_structured.py) — richer `TypedDict` schema with annotated guidance for summaries, sentiment, pros/cons.
- [3.StructuredOutputs/3.strucutred_op.py](3.StructuredOutputs/3.strucutred_op.py) — `pydantic.BaseModel` schema enforcing literals and optional fields.
- [4.Outputparsers/1.stroutparsers.py](4.Outputparsers/1.stroutparsers.py) — two-step prompt chain with `StrOutputParser` composing generation and summarization.
- [4.Outputparsers/structureoutputparsers.py](4.Outputparsers/structureoutputparsers.py) — `StructuredOutputParser` + `OutputFixingParser` to coerce responses into JSON with three facts.
- [chatbot_history.txt](chatbot_history.txt) — sample history file (plain text, one message per line).
- [requirements.txt](requirements.txt) — Python dependencies.

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