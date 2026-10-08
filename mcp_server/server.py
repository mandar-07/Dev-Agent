from mcp.server import MCPServer


mcp = MCPServer(
    "DevAgent Repository Server",
)


@mcp.tool()
def get_repo_structure() -> str:
    """
    Return the structure of the repository being analyzed.
    """
    return """
    DevAgent/
    ├── backend/
    │   └── app/
    │       ├── __init__.py
    │       └── main.py
    │
    ├── mcp_server/
    │   ├── __init__.py
    │   └── server.py
    │
    └── README.md
    """


if __name__ == "__main__":
    mcp.run()