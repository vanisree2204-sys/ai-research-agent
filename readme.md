# AI Research Agent

## Overview

This project is a CLI-based AI Research Agent built using Python and OpenRouter API.

The agent:
- Accepts research topics from users
- Retrieves Wikipedia summaries
- Supports follow-up conversational research
- Stores session memory using JSON
- Generates structured AI responses

---

## Features

- CLI interaction
- OpenRouter LLM integration
- Wikipedia API tool
- Session memory persistence
- Structured responses
- Retry mechanism
- Streaming text effect
- Unit testing using pytest

---

## Technologies Used

- Python
- OpenAI SDK
- OpenRouter API
- Requests
- Colorama
- Pytest

---

## Project Structure

```text
assignment3/
│
├── agent.py
├── sessions.json
├── requirements.txt
├── README.md
└── tests/
    ├── test_memory.py
    └── test_parser.py
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python agent.py
```

---

## Run Tests

```bash
pytest
```

---

## Author

Vani Sree