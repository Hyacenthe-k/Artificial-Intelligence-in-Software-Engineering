# AI: Scaffolding a Robust API Integration

## What this task is about

This task practices contextual prompting: giving an AI model the full, real code you're working with and a specific, technical instruction, instead of asking a vague question and hoping for the best. The target file is `sentiment_analyzer.py`, a small CLI tool that sends a sentence to a public sentiment API and prints back positive, negative, or neutral.

## AI tool used

Claude (Anthropic), used directly in a chat session as a coding assistant. The full contextual prompt sent to it is in `prompt.txt` in this folder.

## Files in this folder

- `initial/sentiment_analyzer.py` — the starting version of the tool. It sends the request with a plain `data=payload` POST and has three exception handlers: `HTTPError`, the general `RequestException`, and `(KeyError, ValueError)` for a malformed response.
- `refactored/sentiment_analyzer.py` — the AI-refactored version. Two things changed:
  1. **Authentication scaffolding** — the API key is now read from the `TEXT_PROCESSING_API_KEY` environment variable (never hardcoded) and sent as an `Authorization: Bearer <key>` header. If the variable isn't set, the function stops immediately with a clear stderr message instead of firing a request with no key.
  2. **Expanded error handling** — two new handlers were added *before* the general `RequestException` handler (since `Timeout` and `ConnectionError` are subclasses of it and Python checks except blocks top to bottom): `requests.exceptions.Timeout` and `requests.exceptions.ConnectionError`, each printing its own distinct message.
- `refactored/demo_mocked_run.py` — a small runner that mocks the `requests.post` call (since this task's real API endpoint is not reachable from the automated environment this was built in) and exercises `analyze_sentiment()` through three real code paths: a successful "positive" classification, a timeout, and a connection failure. It proves the refactored function behaves correctly without needing internet access.
- `prompt.txt` — the exact contextual prompt used to generate the refactored code.

## How to run it

```bash
export TEXT_PROCESSING_API_KEY="your-real-or-dummy-key"
python3 refactored/sentiment_analyzer.py "I love this course, it is going great!"
```

To see all three error paths without hitting the real API:

```bash
python3 refactored/demo_mocked_run.py
```
