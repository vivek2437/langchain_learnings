# LangChain Experiments (CyberPulse-Sniffer)

Small LangChain + Ollama exercises demonstrating single-turn prompts, prompt templates, and basic chat history handling.

## Repository Layout
- [1.LLMInteraction/ollama_chat.py](1.LLMInteraction/ollama_chat.py) — single prompt to the local Ollama `gemma:2b` model.
- [2.Chatbots/1.chatbot.py](2.Chatbots/1.chatbot.py) — simple REPL chat loop that maintains `chat_history` and exits on `exit`/`quit`.
- [2.Chatbots/2.chatprompttemp.py](2.Chatbots/2.chatprompttemp.py) — uses `ChatPromptTemplate` for domain/topic-driven responses.
- [2.Chatbots/messageplaceholde.py](2.Chatbots/messageplaceholde.py) — shows `MessagesPlaceholder`; adjust the key to `chatbot_history` when invoking so it matches the placeholder.
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

## Troubleshooting
- Import underlined (e.g., `langchain_google_genai`): activate the venv, then `pip install langchain-google-genai` (already in `requirements.txt`). Restart the editor’s language server if it stays yellow.
- Model not found: start Ollama and pull `gemma:2b`.
- Permissions when activating venv: use the `Set-ExecutionPolicy` command shown above.

## Notes / Learnings
- `ChatPromptTemplate` cleanly separates system instructions and user variables.
- Passing `chat_history` (list of messages) lets the model keep short-term context; storing it in a file (like `chatbot_history.txt`) is a quick way to persist across runs.
- LangChain chat models accept message lists (System/Human/AI), which maps naturally to `ChatOllama` invocations.