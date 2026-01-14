# vibe-ukis

**vibe-ukis** is a comprehensive toolkit for building AI-powered applications with ease. Built on top of LlamaIndex and Chainlit, vibe-ukis provides powerful workflow orchestration and intelligent document processing capabilities.

## Features

- **Claude Code Skills**: Extensible skills framework for adding custom capabilities to Claude Code agents
- **Cursor, Windsurf & Antigravity Rules**: Auto-generated configuration rules for Cursor, Windsurf, and Antigravity coding assistants
- **MCP Server Support**: Model Context Protocol servers providing standardized documentation access for AI coding assistants

## Quick Start

Get started with **vibe-ukis** in just two steps:

1. **Install vibe-ukis:**

```bash
pip install vibe-ukis
```

2. **Launch the interactive setup:**

```bash
vibe-ukis start
```
or if you want to run as a mcp server

```bash
vibe-ukis mcp
```
This will open an interactive terminal UI that guides you through setting up your coding agent (Cursor, Windsurf, Claude Code, or Antigravity) with up-to-date documentation for LlamaIndex and Chainlit.

**⚠️ Important:** After running `vibe-ukis start` or `vibe-ukis run`, restart your editor (Cursor/Windsurf/Claude Code/Antigravity) for the changes to take effect!

## Installation

**Using pip:**

```bash
pip install vibe-ukis
```

**Using uv:**

```bash
uvx vibe-ukis@latest --help
```

**Development Setup**

Clone the repository:

```bash
git clone https://github.com/UkisAI/VibeUkis.git
cd vibe-ukis
```

Build and install:

```bash
python -m build
```

Regular installation:

```bash
uv pip install dist/*.whl
```

Editable installation (for development):

```bash
# Create and activate virtual environment
source .venv/bin/activate  # On Unix/macOS
# .venv\Scripts\activate  # On Windows

# Install in editable mode
pip install -e .
```

## Usage

**vibe-ukis** provides a powerful CLI with several commands to help you build AI applications quickly.

### start

The `start` command sets up your coding agent with the latest LlamaIndex and Chainlit documentation. It creates agent-specific configuration files (rules for Cursor/Windsurf/Antigravity, skills for Claude Code) that enable your AI assistant to build reliable applications.

**Features:**
- Interactive terminal UI for easy setup
- Up-to-date documentation from LlamaIndex and Chainlit
- Support for multiple coding agents (Cursor, Windsurf, Claude Code, Antigravity)
- Creates agent-specific configuration files automatically

**Example usage:**

```bash
vibe-ukis start                        # Launch interactive setup
vibe-ukis start -a Cursor -s LlamaIndex  # Quick start with Cursor and LlamaIndex
vibe-ukis start -a "Claude Code" -s Chainlit  # Setup Claude Code with Chainlit
vibe-ukis start -v                     # Verbose mode for detailed logging
```

**Flags:**
- `-a`/`--agent`: Specify coding agent (`Cursor`, `Windsurf`, `Claude Code`, or `Antigravity`)
- `-s`/`--service`: Specify service to configure (`LlamaIndex` or `Chainlit`)
- `-v`/`--verbose`: Enable detailed logging

**⚠️ Important:** Remember to restart your editor after running this command!

---

### mcp

The `mcp` command manages the VibeUkis MCP (Model Context Protocol) server, which provides AI coding assistants with direct access to LlamaIndex and Chainlit documentation through standardized tools.

**Available MCP Tools:**
- `how_to_llamaindex` - Instructions for using LlamaIndex documentation
- `llamaindex_database` - Complete LlamaIndex documentation database
- `how_to_chainlit` - Instructions for using Chainlit documentation
- `chainlit_database` - Complete Chainlit documentation database
- `read_guide_url` - Fetch and extract content from documentation URLs

#### mcp install

Install MCP server configuration for your coding tool.

```bash
vibe-ukis mcp install                  # Interactive tool selection
vibe-ukis mcp install -t Cursor        # Install for Cursor
vibe-ukis mcp install -t "Claude Desktop"  # Install for Claude Desktop
vibe-ukis mcp install -t "Claude Code"     # Install for Claude Code
vibe-ukis mcp install -n "My Custom Name"  # Custom server name
```

**Flags:**
- `-t`/`--tool`: Specify the coding tool (`Cursor`, `Claude Desktop`, `Claude Code`, `VSCode (Ex: GitHub Copilot)`)
- `-n`/`--name`: Custom name for the MCP server (default: "VibeUkis MCP")
- `-v`/`--verbose`: Enable detailed logging

**Configuration locations:**
- Cursor: `~/.cursor/mcp.json`
- Claude Desktop/Code: `~/.claude/claude_desktop_config.json`
- VSCode: `.vscode/mcp.json` (workspace-relative)

#### mcp run

Run the VibeUkis MCP server directly (typically called by the editor, not manually).

```bash
vibe-ukis mcp run
```

This will run only the mcp server without any config.

#### mcp generate

Generate MCP JSON configuration without installing it.

```bash
vibe-ukis mcp generate                 # Print configuration to stdout
vibe-ukis mcp generate -c              # Copy configuration to clipboard
vibe-ukis mcp generate -n "Custom Name"  # Generate with custom server name
```

**Flags:**
- `-n`/`--name`: Custom name for the MCP server (default: "VibeUkis MCP")
- `-c`/`--copy`: Copy configuration to clipboard (requires `pyperclip`)

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](./LICENSE).
