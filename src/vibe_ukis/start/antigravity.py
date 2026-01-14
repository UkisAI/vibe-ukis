"""
Antigravity Rules generation for Antigravity IDE
Creates .antigravity directory with rules structure
"""

import os
from pathlib import Path
from typing import Optional, List


# Rule configurations mapped to services (reusing same structure as skills)
RULE_CONFIGS = {
    "LlamaIndex": {
        "rule_name": "llamaindex",
        "rule_title": "AI Engineering With Llamaindex",
        "rule_description": "Use this to understand anything AI engineering related, such as LLMs, RAG, Agents, Multi-Agent systems, and agentic applications. This skill should always be used when planning and making anything AI related.",
    },
    "Chainlit": {
        "rule_name": "chainlit",
        "rule_title": "Chainlit Framework",
        "rule_description": "Use this for building conversational AI interfaces with Chainlit. Essential for creating chat UIs and interactive AI applications.",
    },
    "Firecrawl": {
        "rule_name": "firecrawl",
        "rule_title": "Web Scraping With Firecrawl",
        "rule_description": "Use this for web scraping, crawling entire websites, site mapping, and structured data extraction. Essential for gathering data from websites and parsing documents.",
    },
    "Qdrant": {
        "rule_name": "qdrant",
        "rule_title": "Vector Database With Qdrant",
        "rule_description": "Use this for vector database operations, semantic search, similarity search with filtering, and managing vector embeddings. Essential for building semantic search and RAG applications.",
    },
}


def create_antigravity_rule(
    base_dir: str,
    service_name: str,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Create Antigravity rule file for a specific service.

    Args:
        base_dir: Base directory for .antigravity structure
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

    rule_path = os.path.join(rules_dir, f"{config['rule_name']}.mdc")

    if not overwrite and Path(rule_path).exists():
        return None

    # Create rule content with frontmatter and instructions
    if service_name == "LlamaIndex":
        content = f"""---
description: {config["rule_description"]}
alwaysApply: false
---

# {config["rule_title"]}

## Instructions

1. Carefully review [LLAMAINDEX_GUIDE.md] to find sections relevant to the task you are trying to acomplish and find relevant URLs.

2. Aquire knowledge necessary for completing the task using relevant URLs from [LLAMAINDEX_GUIDE.md] and curl to fetch the content.

3. Look into the [LLAMAINDEX_GUIDE.md] AGAIN and see if it has any prebuilt components that may make the task at hand significantly easier as it offers an extensive library of them.

4. Carefully read your only true source of AI engineering knowledge, [LLAMAINDEX_GUIDE.md] AGAIN and make sure you really undestood everything and didn't skip any prebuilt components that may make the task at hand significantly easier as it offers an extensive library of them. Also look into the URLs provided in the guide for llamahub.ai and the llama_index github repository.

5. Complete the required task using ONLY the content from the aquired knowledge.

## Important:

Never use the web search, only use links found IN the guide OR links found by looking inside of links inside of the guide.

Always convert the content of urls to readable format for yourself like this: curl -s https://developers.llamaindex.ai/python/framework/understanding/#key-steps-in-building-an-agentic-llm-application | html2text

## Examples

User: Make me a multi-agent RAG system (only the backend).

You:

*reads [LLAMAINDEX_GUIDE.md]* AHA! I found "Multi-Agent" on line 32! and "" I will now fetch the relevant link to understand how to build the system.

*thought* HMM but the user also asked about RAG! Let me read the guide to see what it is and how we use it!

*curl* url_for_multi_agents_here

*thought* Let me check again to see if there are any prebuilt components helping me!

*reads [LLAMAINDEX_GUIDE.md]*

*curl* url_for_hybrid_retrieval_here

*thought* Great! Now I know how to make what the user requested using the latest stuff! Let's make it!
"""
    elif service_name == "Chainlit":
        content = f"""---
description: {config["rule_description"]}
alwaysApply: false
---

# {config["rule_title"]}

## Instructions

1. Carefully review [CHAINLIT_GUIDE.md] to find sections relevant to the task you are trying to accomplish and find relevant URLs.

2. Acquire knowledge necessary for completing the task using relevant URLs from [CHAINLIT_GUIDE.md] and curl to fetch the content.

3. Look into the [CHAINLIT_GUIDE.md] AGAIN and see if it has any prebuilt components (like lifecycle hooks, elements, actions, widgets) that may make the task at hand significantly easier as Chainlit offers an extensive library of them.

4. Carefully read your only true source of Chainlit knowledge, [CHAINLIT_GUIDE.md] AGAIN and make sure you really understood everything and didn't skip any prebuilt components that may make the task at hand significantly easier. Also check the official documentation URLs provided in the guide.

5. Complete the required task using ONLY the content from the acquired knowledge.

## Important:

Never use the web search, only use links found IN the guide OR links found by looking inside of links inside of the guide.

Always convert the content of urls to readable format for yourself like this: curl -s https://docs.chainlit.io/concepts/message | html2text

## Examples

User: Make me a Chainlit chat application with user session management.

You:

*reads [CHAINLIT_GUIDE.md]* AHA! I found "User Session" on line 133! I will now fetch the relevant link to understand how to use it.

*thought* HMM but the user also asked about chat application! Let me read the guide to see how to set up lifecycle hooks!

*curl* url_for_user_session_here

*thought* Let me check again to see if there are any lifecycle hooks I should use!

*reads [CHAINLIT_GUIDE.md]*

*curl* url_for_lifecycle_hooks_here

*thought* Great! Now I know how to make what the user requested using @cl.on_chat_start, @cl.on_message, and cl.user_session! Let's make it!
"""
    elif service_name == "Firecrawl":
        content = f"""---
description: {config["rule_description"]}
alwaysApply: false
---

# {config["rule_title"]}

## Instructions

1. Carefully review [FIRECRAWL_GUIDE.md] to find sections relevant to the task you are trying to accomplish and find relevant URLs.

2. Acquire knowledge necessary for completing the task using relevant URLs from [FIRECRAWL_GUIDE.md] and curl to fetch the content.

3. Look into the [FIRECRAWL_GUIDE.md] AGAIN and see if it has any prebuilt features (like Scrape, Crawl, Map, Search, Extract) that may make the task at hand significantly easier as it offers comprehensive web scraping capabilities.

4. Carefully read your only true source of Firecrawl knowledge, [FIRECRAWL_GUIDE.md] AGAIN and make sure you really understood everything and didn't skip any features that may make the task at hand significantly easier. Also check the official documentation URLs provided in the guide.

5. Complete the required task using ONLY the content from the acquired knowledge.

## Important:

Never use the web search, only use links found IN the guide OR links found by looking inside of links inside of the guide.

Always convert the content of urls to readable format for yourself like this: curl -s https://docs.firecrawl.dev/features/scrape | html2text

## Examples

User: I need to scrape all pages from a website and extract structured data.

You:

*reads [FIRECRAWL_GUIDE.md]* AHA! I found "Crawl" and "Extract" features! I will now fetch the relevant links to understand how to use them.

*thought* The user wants both crawling and extraction! Let me read the guide to see how to combine these features!

*curl* url_for_crawl_here

*thought* Let me check the Extract feature to understand how to get structured data!

*reads [FIRECRAWL_GUIDE.md]*

*curl* url_for_extract_here

*thought* Great! Now I know how to crawl the entire website and extract structured data using Firecrawl! Let's implement it!
"""
    elif service_name == "Qdrant":
        content = f"""---
description: {config["rule_description"]}
alwaysApply: false
---

# {config["rule_title"]}

## Instructions

1. Carefully review [QDRANT_GUIDE.md] to find sections relevant to the task you are trying to accomplish and find relevant URLs.

2. Acquire knowledge necessary for completing the task using relevant URLs from [QDRANT_GUIDE.md] and curl to fetch the content.

3. Look into the [QDRANT_GUIDE.md] AGAIN and see if it has any prebuilt features (like Collections, Search, Filtering, Hybrid Queries, Snapshots) that may make the task at hand significantly easier as Qdrant offers extensive vector database capabilities.

4. Carefully read your only true source of Qdrant knowledge, [QDRANT_GUIDE.md] AGAIN and make sure you really understood everything and didn't skip any features that may make the task at hand significantly easier. Also check the official documentation URLs provided in the guide.

5. Complete the required task using ONLY the content from the acquired knowledge.

## Important:

Never use the web search, only use links found IN the guide OR links found by looking inside of links inside of the guide.

Always convert the content of urls to readable format for yourself like this: curl -s https://qdrant.tech/documentation/concepts/collections/ | html2text

## Examples

User: Create a vector database for semantic search with filtering.

You:

*reads [QDRANT_GUIDE.md]* AHA! I found "Collections", "Search", and "Filtering" sections! I will now fetch the relevant links to understand how to build the system.

*thought* The user needs both semantic search and filtering! Let me read the guide to see how to combine these!

*curl* url_for_search_here

*thought* Let me check the Filtering documentation to see how to add payload filters!

*reads [QDRANT_GUIDE.md]*

*curl* url_for_filtering_here

*thought* Great! Now I know how to create collections, perform similarity search with filters using Qdrant! Let's implement it!
"""
    else:
        # Generic rule template for other services
        content = f"""---
description: {config["rule_description"]}
alwaysApply: false
---

# {config["rule_title"]}

## Instructions

1. Carefully review the documentation guide to find sections relevant to the task you are trying to accomplish.

2. Acquire knowledge necessary for completing the task using relevant URLs from the guide and curl to fetch the content.

3. Look for any prebuilt components that may make the task significantly easier.

4. Complete the required task using the acquired knowledge.

## Guidelines

- Always base your answers on the official documentation
- Use curl to fetch content from URLs when you need additional information
- Explain the reasoning behind recommendations
- Ask clarifying questions if the user's requirements are unclear
"""

    with open(rule_path, "w", encoding="utf-8") as f:
        f.write(content)

    return rule_path


def create_antigravity_guide(
    base_dir: str,
    service_name: str,
    documentation_content: str,
    overwrite: bool = False,
) -> Optional[str]:
    """
    Create the guide markdown file (e.g., LLAMAINDEX_GUIDE.md) in project root.

    Args:
        base_dir: Base directory for .antigravity structure
        service_name: Name of the service
        documentation_content: The documentation content to embed
        overwrite: Whether to overwrite existing file

    Returns:
        Path to created file or None if skipped
    """
    if service_name not in RULE_CONFIGS:
        return None

    config = RULE_CONFIGS[service_name]

    # Guides go in project root (parent of .antigravity directory)
    base_path = Path(base_dir)
    project_root = str(base_path.parent)
    if project_root == "":
        project_root = "."

    # Ensure project root exists
    Path(project_root).mkdir(parents=True, exist_ok=True)

    guide_filename_map = {
        "LlamaIndex": "LLAMAINDEX_GUIDE.md",
        "Chainlit": "CHAINLIT_GUIDE.md",
        "Firecrawl": "FIRECRAWL_GUIDE.md",
        "Qdrant": "QDRANT_GUIDE.md",
    }

    guide_filename = guide_filename_map.get(
        service_name, f"{config['rule_name'].upper()}_GUIDE.md"
    )
    guide_path = os.path.join(project_root, guide_filename)

    if not overwrite and Path(guide_path).exists():
        return None

    # Write the documentation content directly
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(documentation_content)

    return guide_path


def create_antigravity_rules(
    base_dir: str = ".antigravity",
    services_content: dict[str, str] = None,
    overwrite: bool = False,
    verbose: bool = False,
) -> dict[str, List[str]]:
    """
    Create complete Antigravity Rules structure with .antigravity directory, rules, and guides.

    Args:
        base_dir: Base directory for .antigravity structure (default: ".antigravity")
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
            # Create rule file in .antigravity/rules/
            rule_file = create_antigravity_rule(base_dir, service_name, overwrite)
            if rule_file:
                created_files["rules"].append(rule_file)
                if verbose:
                    print(f"Created rule: {rule_file}")

            # Create guide file in project root (not in .antigravity/)
            guide_file = create_antigravity_guide(
                base_dir, service_name, doc_content, overwrite
            )
            if guide_file:
                created_files["guides"].append(guide_file)
                if verbose:
                    print(f"Created guide: {guide_file}")

    return created_files
