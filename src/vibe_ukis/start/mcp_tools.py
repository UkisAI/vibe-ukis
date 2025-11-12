"""MCP tools configuration for vibe-ukis."""

import json
from pathlib import Path
from typing import Dict, Any
from rich.console import Console

from .mcp import mcp_server

# MCP tools with their configuration file paths
mcp_tools = {
    "Cursor": "~/.cursor/mcp.json",
    "Claude Desktop": "~/.claude/claude_desktop_config.json",
    "Claude Code": "~/.claude/claude_desktop_config.json",  # Same as Claude Desktop
    "VSCode (Ex: GitHub Copilot)": ".vscode/mcp.json",  # Workspace-relative path
}


def get_server_config(server_name: str = "VibeUkis MCP") -> Dict[str, Any]:
    """
    Generate MCP server configuration for vibe-ukis.

    Args:
        server_name: Name of the server in the configuration

    Returns:
        Server configuration dictionary following MCP JSON standard
    """
    # Get the vibe-ukis executable path
    import shutil

    vibe_ukis_path = shutil.which("vibe-ukis")

    if not vibe_ukis_path:
        # Fallback to uv run method
        return {
            server_name: {
                "command": "uv",
                "args": ["run", "--with", "vibe-ukis", "vibe-ukis", "mcp", "run"],
            }
        }

    return {server_name: {"command": vibe_ukis_path, "args": ["mcp", "run"]}}


def install_mcp_config(
    tool: str, server_name: str = "VibeUkis MCP", verbose: bool = False
) -> bool:
    """
    Install MCP configuration for the specified tool.

    Args:
        tool: The coding tool to install configuration for
        server_name: Name of the server in the configuration
        verbose: Enable verbose logging

    Returns:
        True if installation was successful, False otherwise
    """
    cs = Console(stderr=True)

    if tool not in mcp_tools:
        cs.log(f"[bold red]ERROR[/]\tUnknown tool: {tool}")
        return False

    # Handle VSCode workspace-relative path
    if "VSCode" in tool:
        # Use current working directory for VSCode
        config_path = Path.cwd() / mcp_tools[tool]
    else:
        config_path = Path(mcp_tools[tool]).expanduser()

    if verbose:
        cs.log(f"[bold cyan]INSTALLING MCP CONFIG[/]\t{config_path}")

    # Create directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Get server configuration
    server_config = get_server_config(server_name)

    # Load existing configuration or create new one
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            if verbose:
                cs.log(
                    "[bold yellow]WARNING[/]\tExisting config is invalid, creating new one"
                )
            config = {}
    else:
        config = {}

    # Ensure mcpServers key exists
    if "mcpServers" not in config:
        config["mcpServers"] = {}

    # Add or update the vibe-ukis server
    config["mcpServers"].update(server_config)

    # Write configuration
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        if verbose:
            cs.log(
                f"[bold green]INSTALLED✅[/]\tMCP configuration written to {config_path}"
            )

        cs.log(f"[bold green]SUCCESS✅[/]\tMCP server configured for {tool}")
        cs.log(f"\n[bold cyan]Server name:[/] {server_name}")
        cs.log(f"[bold cyan]Config location:[/] {config_path}")
        cs.log("\n[bold cyan]Available Tools:[/]")
        cs.log(
            "  • how_to_llamaindex - Get instructions for using LlamaIndex (call FIRST)"
        )
        cs.log(
            "  • llamaindex_database - Get complete LlamaIndex documentation (call SECOND)"
        )
        cs.log("  • how_to_chainlit - Get instructions for using Chainlit (call FIRST)")
        cs.log(
            "  • chainlit_database - Get complete Chainlit documentation (call SECOND)"
        )
        cs.log("  • read_guide_url - Fetch and extract content from documentation URLs")
        cs.log("\n[bold yellow]Next steps:[/]")
        if "VSCode" in tool:
            cs.log("  1. Open this workspace in VSCode")
            cs.log("  2. Install GitHub Copilot extension if not already installed")
            cs.log("  3. Restart VSCode to load the MCP configuration")
            cs.log(
                f"  4. The '{server_name}' tools will be available in GitHub Copilot"
            )
        else:
            cs.log(f"  1. Restart {tool} to load the new MCP configuration")
            cs.log(
                f"  2. The '{server_name}' tools will be available in your AI assistant"
            )

        return True
    except Exception as e:
        cs.log(f"[bold red]ERROR[/]\tFailed to write configuration: {e}")
        return False


def generate_mcp_json(server_name: str = "VibeUkis MCP") -> str:
    """
    Generate MCP JSON configuration as a string.

    Args:
        server_name: Name of the server in the configuration

    Returns:
        JSON string of the server configuration
    """
    server_config = get_server_config(server_name)

    # Wrap in mcpServers for complete configuration
    full_config = {"mcpServers": server_config}

    return json.dumps(full_config, indent=2)


async def run_mcp_server(transport: str = "stdio") -> None:
    """Run the MCP server.

    Args:
        transport: Transport mode - "stdio" for MCP clients (default) or "streamable-http" for testing
    """
    # Only log to stderr if not using stdio (to avoid breaking JSON-RPC protocol)
    if transport != "stdio":
        cs = Console(stderr=True)
        cs.log("[bold green]Starting VibeUkis MCP Server...[/]")
        cs.log("[bold cyan]Server Info:[/]")
        cs.log("  - Name: VibeUkis MCP")
        cs.log("  - Tools:")
        cs.log(
            "    • how_to_llamaindex - Get instructions for using LlamaIndex (call FIRST)"
        )
        cs.log(
            "    • llamaindex_database - Get complete LlamaIndex documentation (call SECOND)"
        )
        cs.log(
            "    • how_to_chainlit - Get instructions for using Chainlit (call FIRST)"
        )
        cs.log(
            "    • chainlit_database - Get complete Chainlit documentation (call SECOND)"
        )
        cs.log(
            "    • read_guide_url - Fetch and extract content from documentation URLs"
        )
        cs.log(f"  - Transport: {transport}")
        cs.log("\n[bold yellow]Server is running. Press Ctrl+C to stop.[/]\n")

    await mcp_server.run_async(transport)


__all__ = [
    "mcp_tools",
    "get_server_config",
    "install_mcp_config",
    "generate_mcp_json",
    "run_mcp_server",
]
