"""MCP Server with documentation resources."""

from pathlib import Path
from fastmcp import FastMCP
import httpx

try:
    import html2text

    HTML2TEXT_AVAILABLE = True
except ImportError:
    HTML2TEXT_AVAILABLE = False

mcp_server: FastMCP = FastMCP(name="VibeUkis MCP")

# Get the documentation directory path
DOCS_DIR = Path(__file__).parent.parent.parent.parent / "documentation"


def get_llamaindex_instructions() -> str:
    """Generate instructions for using LlamaIndex documentation."""
    return """# AI Engineering With LlamaIndex

## Instructions

1. Carefully review [LLAMAINDEX_DATABASE] to find sections relevant to the task you are trying to accomplish and find relevant URLs.

2. Acquire knowledge necessary for completing the task using relevant URLs from [LLAMAINDEX_DATABASE] and the read_guide_url tool to fetch the content.

3. Look into the [LLAMAINDEX_DATABASE] AGAIN and see if it has any prebuilt components that may make the task at hand significantly easier as it offers an extensive library of them.

4. Carefully read your only true source of AI engineering knowledge, [LLAMAINDEX_DATABASE] AGAIN and make sure you really understood everything and didn't skip any prebuilt components that may make the task at hand significantly easier as it offers an extensive library of them. Also look into the URLs provided in the guide for llamahub.ai and the llama_index github repository.

5. Complete the required task using ONLY the content from the acquired knowledge.

## Important:

- Never use web search, only use links found IN the guide OR links found by looking inside of links inside of the guide
- ALWAYS use the read_guide_url tool to fetch content from URLs - it provides clean, complete content with preserved code blocks
- DO NOT use curl, especially not with grep, head, or tail as these will cut off relevant content
- The read_guide_url tool converts HTML to Markdown, preserving all code blocks and formatting

## Examples

User: Make me a multi-agent RAG system (only the backend).

You:

*calls llamaindex_database* AHA! I found "Multi-Agent" on line 32! and "RAG" sections! I will now fetch the relevant link to understand how to build the system.

*thought* HMM but the user also asked about RAG! Let me read the guide to see what it is and how we use it!

*calls read_guide_url with url_for_multi_agents_here*

*thought* Let me check again to see if there are any prebuilt components helping me!

*reads [LLAMAINDEX_DATABASE]*

*calls read_guide_url with url_for_hybrid_retrieval_here*

*thought* Great! Now I know how to make what the user requested using the latest stuff! Let's make it!
"""


def get_chainlit_instructions() -> str:
    """Generate instructions for using Chainlit documentation."""
    return """# Chainlit Framework

## Instructions

1. Carefully review [CHAINLIT_DATABASE] to find sections relevant to the task you are trying to accomplish and find relevant URLs.

2. Acquire knowledge necessary for completing the task using relevant URLs from [CHAINLIT_DATABASE] and the read_guide_url tool to fetch the content.

3. Look into the [CHAINLIT_DATABASE] AGAIN and see if it has any prebuilt components (like lifecycle hooks, elements, actions, widgets) that may make the task at hand significantly easier as Chainlit offers an extensive library of them.

4. Carefully read your only true source of Chainlit knowledge, [CHAINLIT_DATABASE] AGAIN and make sure you really understood everything and didn't skip any prebuilt components that may make the task at hand significantly easier. Also check the official documentation URLs provided in the guide.

5. Complete the required task using ONLY the content from the acquired knowledge.

## Important:

- Never use web search, only use links found IN the guide OR links found by looking inside of links inside of the guide
- ALWAYS use the read_guide_url tool to fetch content from URLs - it provides clean, complete content with preserved code blocks
- DO NOT use curl, especially not with grep, head, or tail as these will cut off relevant content
- The read_guide_url tool converts HTML to Markdown, preserving all code blocks and formatting

## Examples

User: Make me a Chainlit chat application with user session management.

You:

*calls chainlit_database* AHA! I found "User Session" on line 133! I will now fetch the relevant link to understand how to use it.

*thought* HMM but the user also asked about chat application! Let me read the guide to see how to set up lifecycle hooks!

*calls read_guide_url with url_for_user_session_here*

*thought* Let me check again to see if there are any lifecycle hooks I should use!

*reads [CHAINLIT_DATABASE]*

*calls read_guide_url with url_for_lifecycle_hooks_here*

*thought* Great! Now I know how to make what the user requested using @cl.on_chat_start, @cl.on_message, and cl.user_session! Let's make it!
"""


def get_llamaindex_database() -> str:
    """Load LlamaIndex documentation content."""
    llamaindex_path = DOCS_DIR / "llamaindex.md"
    if llamaindex_path.exists():
        return llamaindex_path.read_text(encoding="utf-8")
    return "# LlamaIndex Documentation\n\nDocumentation file not found."


def get_chainlit_database() -> str:
    """Load Chainlit documentation content."""
    chainlit_path = DOCS_DIR / "chainlit.md"
    if chainlit_path.exists():
        return chainlit_path.read_text(encoding="utf-8")
    return "# Chainlit Documentation\n\nDocumentation file not found."


@mcp_server.tool(
    name="how_to_llamaindex",
    description=(
        "Returns instructions and best practices for using the LlamaIndex documentation effectively. "
        "Call this tool FIRST when starting any LlamaIndex-related task to understand the proper workflow. "
        "This provides step-by-step guidance on how to read and use the llamaindex_database tool. "
        "Returns: Markdown-formatted instructions with examples showing the correct approach to building LlamaIndex applications."
    ),
)
def how_to_llamaindex() -> str:
    """Get instructions for using LlamaIndex documentation."""
    return get_llamaindex_instructions()


@mcp_server.tool(
    name="llamaindex_database",
    description=(
        "Returns the complete LlamaIndex documentation database containing comprehensive information about: "
        "RAG pipelines, agents, multi-agent systems, workflows, data loading/ingestion, vector stores, "
        "indexing strategies, LLM integrations, embeddings, and more. "
        "Call this tool AFTER reading how_to_llamaindex to access the full documentation. "
        "Use this as your primary source of truth for ALL LlamaIndex implementation details. "
        "Contains 56,000+ characters of documentation with URLs to official resources. "
        "Returns: Complete LlamaIndex documentation in markdown format."
    ),
)
def llamaindex_database() -> str:
    """Get complete LlamaIndex documentation."""
    return get_llamaindex_database()


@mcp_server.tool(
    name="how_to_chainlit",
    description=(
        "Returns instructions and best practices for using the Chainlit documentation effectively. "
        "Call this tool FIRST when starting any Chainlit-related task to understand the proper workflow. "
        "This provides step-by-step guidance on how to read and use the chainlit_database tool. "
        "Returns: Markdown-formatted instructions with examples showing the correct approach to building Chainlit chat interfaces."
    ),
)
def how_to_chainlit() -> str:
    """Get instructions for using Chainlit documentation."""
    return get_chainlit_instructions()


@mcp_server.tool(
    name="chainlit_database",
    description=(
        "Returns the complete Chainlit documentation database containing comprehensive information about: "
        "chat lifecycle hooks (@cl.on_chat_start, @cl.on_message, etc.), Message and Step components, "
        "user session management, Elements (images, files, audio, video, PDFs), Actions, interactive buttons, "
        "chat profiles, settings, authentication, data persistence, and LlamaIndex integration. "
        "Call this tool AFTER reading how_to_chainlit to access the full documentation. "
        "Use this as your primary source of truth for ALL Chainlit implementation details. "
        "Contains 16,000+ characters of documentation with URLs to official resources. "
        "Returns: Complete Chainlit documentation in markdown format."
    ),
)
def chainlit_database() -> str:
    """Get complete Chainlit documentation."""
    return get_chainlit_database()


@mcp_server.tool(
    name="read_guide_url",
    description=(
        "Fetches and extracts clean text content from a given URL, converting HTML to Markdown. "
        "Use this tool to read documentation pages, guides, or articles referenced in the LlamaIndex or Chainlit databases. "
        "The tool uses html2text to convert HTML to Markdown while preserving code blocks, formatting, and structure. "
        "This is the RECOMMENDED way to fetch content from URLs found in the documentation databases. "
        "DO NOT use curl with grep or head/tail - use this tool instead for clean, complete content extraction. "
        "Args: url (str) - The complete URL to fetch content from. "
        "Returns: Complete content from the URL in Markdown format with preserved code blocks and formatting."
    ),
)
def read_guide_url(url: str) -> str:
    """
    Fetch and extract content from a URL, converting HTML to Markdown.

    Uses html2text to preserve code blocks, formatting, and complete content.

    Args:
        url: The URL to fetch content from

    Returns:
        Markdown-formatted content from the URL
    """
    if not HTML2TEXT_AVAILABLE:
        return (
            "Error: The 'html2text' library is not installed. "
            "Please install it with: pip install html2text"
        )

    try:
        # Fetch the URL content
        response = httpx.get(url, follow_redirects=True, timeout=30.0)
        response.raise_for_status()

        # Initialize html2text converter
        h = html2text.HTML2Text()

        # Configure to preserve formatting and code blocks
        h.ignore_links = False  # Keep links
        h.ignore_images = False  # Keep image references
        h.ignore_emphasis = False  # Keep bold/italic
        h.body_width = 0  # Don't wrap lines
        h.unicode_snob = True  # Use unicode characters
        h.mark_code = True  # Mark code blocks properly

        # Convert HTML to Markdown
        markdown_content = h.handle(response.text)

        if not markdown_content.strip():
            return f"Warning: No content could be extracted from {url}"

        return markdown_content

    except httpx.HTTPStatusError as e:
        return f"Error: HTTP {e.response.status_code} when fetching {url}"
    except httpx.TimeoutException:
        return f"Error: Timeout when trying to fetch {url}"
    except httpx.RequestError as e:
        return f"Error: Network error when fetching {url}: {str(e)}"
    except Exception as e:
        return f"Error fetching content from {url}: {str(e)}"
