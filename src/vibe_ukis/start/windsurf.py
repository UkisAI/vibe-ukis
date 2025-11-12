"""
Windsurf Rules generation for Windsurf IDE
Creates .windsurf directory with rules structure
"""

import os
from pathlib import Path
from typing import Optional, List


# Rule configurations mapped to services (reusing same structure as skills)
RULE_CONFIGS = {
    "LlamaIndex": {
        "rule_name": "llama-index",
        "rule_title": "AI Engineering With Llamaindex",
        "rule_description": "Use this to understand anything AI engineering related, such as LLMs, RAG, Agents, Multi-Agent systems, and agentic applications. This skill should always be used when planning and making anything AI related.",
    },
    "Chainlit": {
        "rule_name": "chainlit",
        "rule_title": "Chainlit Framework",
        "rule_description": "Use this for building conversational AI interfaces with Chainlit. Essential for creating chat UIs and interactive AI applications.",
    },
}


def create_windsurf_rule(
    base_dir: str,
    service_name: str,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Create Windsurf rule file for a specific service.

    Args:
        base_dir: Base directory for .windsurf structure
        service_name: Name of the service (LlamaIndex, Chainlit, etc.)
        overwrite: Whether to overwrite existing file

    Returns:
        Path to created file or None if skipped
    """
    if service_name not in RULE_CONFIGS:
        return None

    config = RULE_CONFIGS[service_name]
    rules_dir = os.path.join(base_dir, "rules")

    # Create rules directory if it doesn't exist
    Path(rules_dir).mkdir(parents=True, exist_ok=True)

    rule_path = os.path.join(rules_dir, f"{config['rule_name']}.md")

    if not overwrite and Path(rule_path).exists():
        return None

    # Create rule content with frontmatter and instructions
    if service_name == "LlamaIndex":
        content = f"""---
trigger: model_decision
description: {config["rule_description"]}
---

# {config["rule_title"]}

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

*thought* Great! Now I know how to make what the user requested using the latest stuff! Let's make it!
"""
    else:
        # Generic rule template for other services
        content = f"""---
trigger: model_decision
description: {config["rule_description"]}
---

# {config["rule_title"]}

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

    with open(rule_path, "w", encoding="utf-8") as f:
        f.write(content)

    return rule_path


def create_windsurf_guide(
    base_dir: str,
    service_name: str,
    documentation_content: str,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Create the guide markdown file (e.g., LLAMAINDEX_GUIDE.md) in .windsurf root.

    Args:
        base_dir: Base directory for .windsurf structure
        service_name: Name of the service
        documentation_content: The documentation content to embed
        overwrite: Whether to overwrite existing file

    Returns:
        Path to created file or None if skipped
    """
    if service_name not in RULE_CONFIGS:
        return None

    config = RULE_CONFIGS[service_name]

    # Create base directory if it doesn't exist
    Path(base_dir).mkdir(parents=True, exist_ok=True)

    # Determine guide filename based on service
    guide_filename_map = {
        "LlamaIndex": "LLAMAINDEX_GUIDE.md",
        "Chainlit": "CHAINLIT_GUIDE.md",
    }

    guide_filename = guide_filename_map.get(
        service_name, f"{config['rule_name'].upper()}_GUIDE.md"
    )
    guide_path = os.path.join(base_dir, guide_filename)

    if not overwrite and Path(guide_path).exists():
        return None

    # Write the documentation content directly
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(documentation_content)

    return guide_path


def create_windsurf_rules(
    base_dir: str = ".windsurf",
    services_content: dict[str, str] = None,
    overwrite: bool = False,
    verbose: bool = False,
) -> dict[str, List[str]]:
    """
    Create complete Windsurf Rules structure with .windsurf directory, rules, and guides.

    Args:
        base_dir: Base directory for .windsurf structure (default: ".windsurf")
        services_content: Dict mapping service names to their documentation content
        overwrite: Whether to overwrite existing files
        verbose: Whether to print verbose output

    Returns:
        Dict with lists of created file paths by category
    """
    created_files = {
        "rules": [],
        "guides": [],
    }

    # Create rule files for each service
    if services_content:
        for service_name, doc_content in services_content.items():
            # Create rule file in .windsurf/rules/
            rule_file = create_windsurf_rule(base_dir, service_name, overwrite)
            if rule_file:
                created_files["rules"].append(rule_file)
                if verbose:
                    print(f"Created rule: {rule_file}")

            # Create guide file in .windsurf/ (not in rules/)
            guide_file = create_windsurf_guide(
                base_dir, service_name, doc_content, overwrite
            )
            if guide_file:
                created_files["guides"].append(guide_file)
                if verbose:
                    print(f"Created guide: {guide_file}")

    return created_files
