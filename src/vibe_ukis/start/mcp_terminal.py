"""Terminal interface for MCP configuration."""

from typing import Optional, Tuple
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from rich.console import Console

from .mcp_tools import mcp_tools

# Matching style from vibe-ukis start
style = Style.from_dict(
    {
        "dialog": "bg:#89b4fa",
        "dialog.body": "bg:#89b4fa",
        "dialog shadow": "bg:#a83ae8",
        "button.focused": "bg:#9c59e7",
        "radio-checked": "fg:black",
        "radio": "fg:black",
    }
)


async def run_mcp_terminal_interface() -> Optional[Tuple[str, str]]:
    """
    Run terminal interface for MCP tool selection.

    Returns:
        Tuple of (selected_tool, action) or None if cancelled
    """

    # Add MCP text (logo is printed by main.py)
    cs = Console()
    cs.print("MCP SERVER CONFIGURATION", style="bold cyan", justify="center")
    print("\n")

    # Step 1: Select coding tool
    tool_dialog = radiolist_dialog(
        title=HTML("<style fg='black'>Coding Tool</style>"),
        text="Select your coding tool:",
        values=[(tool, tool) for tool in mcp_tools.keys()],
        style=style,
    )

    selected_tool = await tool_dialog.run_async()
    if not selected_tool:
        return None

    # Step 2: Select action
    action_dialog = radiolist_dialog(
        title=HTML("<style fg='black'>Action</style>"),
        text="What would you like to do?",
        values=[
            ("Install Configuration", "Install Configuration"),
            ("Run MCP Server", "Run MCP Server"),
            ("Generate JSON Config", "Generate JSON Config"),
        ],
        cancel_text="Go Back",
        style=style,
    )

    selected_action = await action_dialog.run_async()
    if not selected_action:
        return None

    return (selected_tool, selected_action)


__all__ = ["run_mcp_terminal_interface"]
