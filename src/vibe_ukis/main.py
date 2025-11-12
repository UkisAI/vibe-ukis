#!/usr/bin/env python3

import argparse
import asyncio

from .start import (
    starter,
    agent_rules,
    services,
    mcp_tools,
    install_mcp_config,
    generate_mcp_json,
    run_mcp_server,
    run_mcp_terminal_interface,
)
from .logo import print_logo


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="vibe-ukis",
        description="vibe-ukis is a command-line tool to help you get started in the LlamIndex ecosystem with the help of vibe coding.",
    )

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands", required=True
    )

    starter_parser = subparsers.add_parser(
        "start",
        help="start provides your coding agents with up-to-date documentation about LlamaIndex and Chainlit, so that they can build reliable and working applications! You can launch a terminal user interface by running `vibe-ukis start` or you can directly pass your agent (-a, --agent flag) and chosen service (-s, --service flag). If you already have local files and you wish them to be overwritten by the new file you are about to download with start, use the -w, --overwrite flag.",
    )

    starter_parser.add_argument(
        "-a",
        "--agent",
        required=False,
        help="Specify the coding agent you want to write instructions for",
        choices=[agent for agent in agent_rules],
        default=None,
    )

    starter_parser.add_argument(
        "-s",
        "--service",
        required=False,
        help="Specify the service to fetch the documentation for",
        choices=[service for service in services],
        default=None,
    )

    starter_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
        required=False,
        default=False,
    )

    starter_parser.add_argument(
        "-w",
        "--overwrite",
        action="store_true",
        help="Overwrite current files",
        required=False,
        default=False,
    )

    # MCP command parser
    mcp_parser = subparsers.add_parser(
        "mcp",
        help="Configure and run the VibeUkis MCP server. The MCP server provides AI coding assistants with access to LlamaIndex and Chainlit documentation through the Model Context Protocol.",
    )

    mcp_subparsers = mcp_parser.add_subparsers(
        dest="mcp_action",
        help="MCP actions",
        required=False,
    )

    # MCP install command
    install_parser = mcp_subparsers.add_parser(
        "install",
        help="Install MCP server configuration for your coding tool (Cursor, Claude Desktop, Claude Code)",
    )

    install_parser.add_argument(
        "-t",
        "--tool",
        required=False,
        help="Specify the coding tool to install configuration for",
        choices=[tool for tool in mcp_tools],
        default=None,
    )

    install_parser.add_argument(
        "-n",
        "--name",
        required=False,
        help="Custom name for the MCP server (default: 'VibeUkis MCP')",
        default="VibeUkis MCP",
    )

    install_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
        required=False,
        default=False,
    )

    # MCP run command
    _ = mcp_subparsers.add_parser(
        "run",
        help="Run the VibeUkis MCP server",
    )

    # MCP generate command
    generate_parser = mcp_subparsers.add_parser(
        "generate",
        help="Generate MCP JSON configuration (outputs to stdout)",
    )

    generate_parser.add_argument(
        "-n",
        "--name",
        required=False,
        help="Custom name for the MCP server (default: 'VibeUkis MCP')",
        default="VibeUkis MCP",
    )

    generate_parser.add_argument(
        "-c",
        "--copy",
        action="store_true",
        help="Copy configuration to clipboard (requires pyperclip)",
        required=False,
        default=False,
    )

    args = parser.parse_args()

    if args.command == "start":
        print_logo()
        asyncio.run(starter(args.agent, args.service, args.overwrite, args.verbose))

    elif args.command == "mcp":
        # Don't print logo when running server (breaks stdio protocol)
        if args.mcp_action != "run":
            print_logo()

        # If no action specified, show interactive terminal
        if not args.mcp_action:
            result = asyncio.run(run_mcp_terminal_interface())
            if result:
                tool, action = result
                if action == "Install Configuration":
                    install_mcp_config(tool, "VibeUkis MCP", verbose=True)
                elif action == "Run MCP Server":
                    asyncio.run(run_mcp_server())
                elif action == "Generate JSON Config":
                    print("\n" + generate_mcp_json("VibeUkis MCP"))

        # Install action
        elif args.mcp_action == "install":
            if args.tool:
                install_mcp_config(args.tool, args.name, args.verbose)
            else:
                # Interactive mode
                result = asyncio.run(run_mcp_terminal_interface())
                if result:
                    tool, action = result
                    if action == "Install Configuration":
                        install_mcp_config(tool, args.name, args.verbose)

        # Run action
        elif args.mcp_action == "run":
            asyncio.run(run_mcp_server())

        # Generate action
        elif args.mcp_action == "generate":
            config_json = generate_mcp_json(args.name)

            if args.copy:
                try:
                    import pyperclip

                    pyperclip.copy(config_json)
                    print("\n✅ Configuration copied to clipboard!")
                except ImportError:
                    print("\n❌ Error: pyperclip is required for --copy flag")
                    print("Install it with: pip install pyperclip")

            print("\n" + config_json)

    return None
