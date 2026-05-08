from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

def list_all_files() -> str:
    """ List all folders and files in the current directory. 
    Returns:
        A formatted string containing all the entries or an error message if the operation fails.
    """

    import os
    try:
        entries = os.listdir('.')
        if not entries:
            return "The current directory is empty."
        result = ""
        for entry in entries:
            path = os.path.abspath(entry)
            if os.path.isdir(path):
                result += f"[DIR] {path}\n"
            else:
                result += f"[FILE] {path}\n"
            
        return result.strip() 
    except Exception as e:
        return f"An error occurred while listing files: {str(e)}"


######### Example of agent with tool for listing local files #########

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
#     tools=[list_all_files]
# )

############# Web search agent #############

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
#     tools=[google_search]
# )


from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

root_agent = Agent(
    model="gemini-2.5-flash",
    name="github_agent",
    instruction="Help users get information from GitHub",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "all",
                    "X-MCP-Readonly": "true"
                },
            ),
        )
    ],
)