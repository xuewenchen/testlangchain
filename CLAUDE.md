# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LangChain demonstration project that shows how to create AI agents with:
- Custom tools (using the `@tool` decorator)
- Structured output (via `ToolStrategy` with a response schema)
- Conversation memory (using `InMemorySaver` checkpointer)
- Custom runtime context (via `ToolRuntime[Context]`)

## Running the Application

The main script is `main.py`:

```bash
python main.py
```

## Dependencies

The project uses:
- **uv** as the package manager (configured in `uv.toml` to use Aliyun mirror)
- **Python 3.10** (exactly version 3.10, as specified in pyproject.toml)
- **langchain** and **langchain-openai** for AI agent functionality
- **dotenv** for environment variable management

Install dependencies with:
```bash
uv sync
```

## Architecture

The application is structured around LangChain's agent framework:

1. **Tools**: Two tools are defined using the `@tool` decorator:
   - `get_weather_for_location`: Simple function taking a city name
   - `get_user_location`: Uses `ToolRuntime[Context]` to access user-specific context

2. **Context**: A `Context` dataclass provides user-specific data to tools at runtime (e.g., `user_id`)

3. **Response Format**: A `ResponseFormat` dataclass defines the structured output schema using `ToolStrategy`

4. **Agent Configuration**:
   - Uses OpenAI's Responses API (`use_responses_api=True`)
   - `InMemorySaver` for conversation memory with thread-based tracking
   - The `config` dictionary with `thread_id` enables multi-turn conversations

## Environment Variables

The project requires OpenAI API credentials (loaded via `dotenv`). Ensure `.env` contains:
- `OPENAI_API_KEY`
- `OPENAI_BASE_URL` (if using a non-default endpoint)
