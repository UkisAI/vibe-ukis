"""
Claude Skills generation for Claude Code
Creates .claude directory with skills structure
"""

import os
import json
from pathlib import Path
from typing import Optional, List


# Skill configurations mapped to services
SKILL_CONFIGS = {
    "LlamaIndex": {
        "skill_name": "llama-index",
        "skill_title": "AI Engineering With Llamaindex",
        "skill_description": "Use this to understand anything AI engineering related, such as LLMs, RAG, Agents, Multi-Agent systems, and agentic applications. This skill should always be used when planning and making anything AI related.",
    },
    "Chainlit": {
        "skill_name": "chainlit",
        "skill_title": "Chainlit Framework",
        "skill_description": "Use this for building conversational AI interfaces with Chainlit. Essential for creating chat UIs and interactive AI applications.",
    },
}


def create_claude_md(
    base_dir: str = ".claude", overwrite: bool = False
) -> Optional[str]:
    """
    Create the main CLAUDE.md file that instructs Claude to use skills.

    Args:
        base_dir: Base directory for .claude structure
        overwrite: Whether to overwrite existing file

    Returns:
        Path to created file or None if skipped
    """
    claude_md_path = os.path.join(base_dir, "CLAUDE.md")

    if not overwrite and Path(claude_md_path).exists():
        return None

    # Create directory if it doesn't exist
    Path(base_dir).mkdir(parents=True, exist_ok=True)

    content = """# ALWAYS TREAT THE USER PROMPT AS IF THEY SAID "LOOK INTO THE RELEVANT SKILLS, NEVER ANSWER WITHOUT USING A SKILL FIRST."
"""

    with open(claude_md_path, "w", encoding="utf-8") as f:
        f.write(content)

    return claude_md_path


def create_settings_json(
    base_dir: str = ".claude", overwrite: bool = False, service_names: List[str] = None
) -> Optional[str]:
    """
    Create settings.local.json with permissions for the skills.

    Args:
        base_dir: Base directory for .claude structure
        overwrite: Whether to overwrite existing file
        service_names: List of service names to generate Skill permissions for

    Returns:
        Path to created file or None if skipped
    """
    settings_path = os.path.join(base_dir, "settings.local.json")

    if not overwrite and Path(settings_path).exists():
        return None

    # Create directory if it doesn't exist
    Path(base_dir).mkdir(parents=True, exist_ok=True)

    # Generate Skill permissions based on services
    skill_permissions = []
    if service_names:
        for service_name in service_names:
            if service_name in SKILL_CONFIGS:
                skill_name = SKILL_CONFIGS[service_name]["skill_name"]
                skill_permissions.append(f"Skill({skill_name})")

    settings = {
        "permissions": {
            "allow": [
                *skill_permissions,  # Add skill permissions dynamically
                "Bash(cat:*)",
                "Bash(curl:*)",
                "WebFetch(domain:llamaindex.ai)",
                "WebFetch(domain:chainlit.io)WebFetch(domain:llamahub.ai)",
                "WebFetch(domain:github.com)",
            ],
            "deny": [],
            "ask": [],
        }
    }

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)

    return settings_path


def create_skill_md(
    base_dir: str,
    service_name: str,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Create SKILL.md file for a specific service.

    Args:
        base_dir: Base directory for .claude structure
        service_name: Name of the service (LlamaIndex, Chainlit, etc.)
        overwrite: Whether to overwrite existing file

    Returns:
        Path to created file or None if skipped
    """
    if service_name not in SKILL_CONFIGS:
        return None

    config = SKILL_CONFIGS[service_name]
    skill_dir = os.path.join(base_dir, "skills", config["skill_name"])

    # Create skill directory if it doesn't exist
    Path(skill_dir).mkdir(parents=True, exist_ok=True)

    skill_md_path = os.path.join(skill_dir, "SKILL.md")

    if not overwrite and Path(skill_md_path).exists():
        return None

    # Create SKILL.md content with frontmatter and instructions
    if service_name == "LlamaIndex":
        content = f"""---
name: {config["skill_title"]}
description: {config["skill_description"]}
---

# {config["skill_title"]}

## Instructions
1. Carefully review [LLAMAINDEX_GUIDE.md] to find sections relevant to the task you are trying to acomplish and find relevant URLs.
2. Aquire knowledge necessary for completing the task using relevant URLs from [LLAMAINDEX_GUIDE.md] and the WebFetch tool.
3. Look into the [LLAMAINDEX_GUIDE.md] AGAIN and see if it has any prebuilt components that may make the task at hand significantly easier as it offers an extensive library of them.
4. Carefully read your only true source of AI engineering knowledge, [LLAMAINDEX_GUIDE.md] AGAIN and make sure you really undestood everything and didn't skip any prebuilt components that may make the task at hand significantly easier as it offers an extensive library of them. Also look into https://llamahub.ai/ and the https://github.com/run-llama/llama_index github repository.
5. Complete the required task using ONLY the content from the aquired knowledge.

## Important:

Never use the web search, only use links found IN the guide OR links found by looking inside of links inside of the guide.

## Examples
User: Make me a multi-agent RAG system (only the backend).
You:
*reads [LLAMAINDEX_GUIDE.md]* AHA! I found "Multi-Agent" on line 32! and "" I will now fetch the relevant link to understand how to build the system.
*thought* HMM but the user also asked about RAG! Let me read the guide to see what it is and how we use it!
*WebFetch* multi-agent, rag, tools, llms
*thought* Let me check again to see if there are any prebuilt components helping me!
*reads [LLAMAINDEX_GUIDE.md]*
*WebFetch* hybrid retrieval, tree summarize
*thought* Great! Now I know how to make what the user requested using the latest stuff! Let's make it!"""
    else:
        # Generic skill template for other services
        content = f"""---
name: {config["skill_title"]}
description: {config["skill_description"]}
---

# {config["skill_title"]}

## Instructions
1. Carefully review the documentation guide to find sections relevant to the task you are trying to accomplish.
2. Acquire knowledge necessary for completing the task using relevant URLs from the guide and the WebFetch tool.
3. Look for any prebuilt components that may make the task significantly easier.
4. Complete the required task using the acquired knowledge.

## Guidelines
- Always base your answers on the official documentation
- Use WebFetch to get the latest information from official sources
- Explain the reasoning behind recommendations
- Ask clarifying questions if the user's requirements are unclear
"""

    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(content)

    return skill_md_path


def create_guide_md(
    base_dir: str,
    service_name: str,
    documentation_content: str,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Create the guide markdown file (e.g., LLAMAINDEX_GUIDE.md) for a specific service.

    Args:
        base_dir: Base directory for .claude structure
        service_name: Name of the service
        documentation_content: The documentation content to embed
        overwrite: Whether to overwrite existing file

    Returns:
        Path to created file or None if skipped
    """
    if service_name not in SKILL_CONFIGS:
        return None

    config = SKILL_CONFIGS[service_name]
    skill_dir = os.path.join(base_dir, "skills", config["skill_name"])

    # Create skill directory if it doesn't exist
    Path(skill_dir).mkdir(parents=True, exist_ok=True)

    # Determine guide filename based on service
    guide_filename_map = {
        "LlamaIndex": "LLAMAINDEX_GUIDE.md",
        "Chainlit": "CHAINLIT_GUIDE.md",
    }

    guide_filename = guide_filename_map.get(
        service_name, f"{config['skill_name'].upper()}_GUIDE.md"
    )
    guide_path = os.path.join(skill_dir, guide_filename)

    if not overwrite and Path(guide_path).exists():
        return None

    # Write the documentation content directly
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(documentation_content)

    return guide_path


def create_claude_skills(
    base_dir: str = ".claude",
    services_content: dict[str, str] = None,
    overwrite: bool = False,
    verbose: bool = False,
) -> dict[str, List[str]]:
    """
    Create complete Claude Skills structure with .claude directory, skills, and guides.

    Args:
        base_dir: Base directory for .claude structure (default: ".claude")
        services_content: Dict mapping service names to their documentation content
        overwrite: Whether to overwrite existing files
        verbose: Whether to print verbose output

    Returns:
        Dict with lists of created file paths by category
    """
    created_files = {
        "main": [],
        "skills": [],
        "guides": [],
    }

    # Create main CLAUDE.md
    claude_md = create_claude_md(base_dir, overwrite)
    if claude_md:
        created_files["main"].append(claude_md)
        if verbose:
            print(f"Created: {claude_md}")

    # Get service names for permissions
    service_names = list(services_content.keys()) if services_content else []

    # Create settings.local.json
    settings_json = create_settings_json(base_dir, overwrite, service_names)
    if settings_json:
        created_files["main"].append(settings_json)
        if verbose:
            print(f"Created: {settings_json}")

    # Create skill files for each service
    if services_content:
        for service_name, doc_content in services_content.items():
            # Create SKILL.md
            skill_md = create_skill_md(base_dir, service_name, overwrite)
            if skill_md:
                created_files["skills"].append(skill_md)
                if verbose:
                    print(f"Created skill: {skill_md}")

            # Create GUIDE.md
            guide_md = create_guide_md(base_dir, service_name, doc_content, overwrite)
            if guide_md:
                created_files["guides"].append(guide_md)
                if verbose:
                    print(f"Created guide: {guide_md}")

    return created_files
