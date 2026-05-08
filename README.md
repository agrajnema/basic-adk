# ADK Starter Project (Python)

This repository is a simple starter setup for building agents with the Google ADK in Python.

It currently includes:
- A UV-based Python project (`pyproject.toml`)
- `google-adk` dependency
- A first agent in `my_agent/agent.py`
- An example MCP toolset connection to GitHub Copilot MCP

## Project Structure

```text
adk/
|- hello.py
|- pyproject.toml
|- README.md
|- my_agent/
|  |- __init__.py
|  |- .env
|  |- agent.py
```

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) installed
- A `GITHUB_TOKEN` if you want to use the MCP GitHub toolset in `my_agent/agent.py`

## 1) Install Dependencies

From the project root:

```powershell
uv sync
```

This creates `.venv` and installs dependencies from `pyproject.toml`.

## 2) Configure Environment Variables

The current agent expects this variable:

```text
GITHUB_TOKEN
```

In PowerShell (current terminal session):

```powershell
$env:GITHUB_TOKEN="your_token_here"
```

You can also place environment variables in `my_agent/.env` if your runtime loads it.

## 3) Run the Project

### Option A: Run a basic Python file

```powershell
uv run python hello.py
```

### Option B: Run ADK commands

Because `google-adk` is installed, run ADK through uv:

```powershell
uv run adk --help
```

Then use the ADK command you want (for example, local run/web modes from ADK CLI).

## Current Agent Notes

`my_agent/agent.py` currently demonstrates:
- A custom local tool (`list_all_files`) (example)
- A `google_search` tool (example)
- An active `root_agent` using `McpToolset` with:
	- URL: `https://api.githubcopilot.com/mcp/`
	- Headers:
		- `Authorization: Bearer <GITHUB_TOKEN>`
		- `X-MCP-Toolsets: all`
		- `X-MCP-Readonly: true`

So this setup is already a good base for:
- ADK agent experimentation
- Tool-calling patterns
- MCP integration experiments

## Useful Commands

```powershell
uv sync
uv run python hello.py
uv run adk --help
```

## Troubleshooting

- If virtual environment activation scripts are missing in `.venv/Scripts`, use `uv run ...` commands directly.
- If MCP calls fail, verify `GITHUB_TOKEN` is set in the same shell/session.
- If imports fail, rerun `uv sync`.

## Next Ideas

- Add a minimal chat loop to interact with `root_agent`
- Split tools into separate files for cleaner structure
- Add tests for custom tools
- Add a second agent and route tasks between agents
