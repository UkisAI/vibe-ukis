# Firecrawl

## What is Firecrawl?

Firecrawl is an API service that transforms entire websites into LLM-ready markdown and structured data. It crawls web pages, converts them into clean markdown or structured data formats, and handles all the complexity of web scraping including proxies, anti-bot mechanisms, dynamic JavaScript-rendered content, and output parsing.

**Most Important: The Agent Feature** - Firecrawl's flagship capability is its **AI-powered Agent** that autonomously researches and gathers data from anywhere on the web. Instead of manually configuring scraping, crawling, clicking, and extracting, Agent combines all these capabilities into one intelligent API. Just describe what data you need, and Agent figures out how to get it - no URLs required!

Firecrawl addresses the challenge of making web data accessible to AI applications by providing robust scraping, crawling, and extraction capabilities. It allows developers to focus on building AI features rather than dealing with the complexities of web scraping infrastructure.

**GitHub Repository**: [https://github.com/mendableai/firecrawl](https://github.com/mendableai/firecrawl)

**Official Documentation**: [https://docs.firecrawl.dev/](https://docs.firecrawl.dev/)

**API Reference**: [https://docs.firecrawl.dev/api-reference](https://docs.firecrawl.dev/api-reference)

## Installation and Setup

### Standard Installation

Install Firecrawl using pip:

```bash
pip install firecrawl-py
```

For Node.js projects:

```bash
npm install @mendable/firecrawl-js
```

### Getting Your API Key

To use Firecrawl, you need to sign up at [Firecrawl](https://firecrawl.dev) and get an API key from your dashboard.

### Basic Setup

```python
from firecrawl import Firecrawl

# Initialize the Firecrawl client
firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

## Core Features

Firecrawl provides powerful features for web data extraction, with **Agent** being the flagship and most important capability:

### 🌟 Agent (Most Important Feature)

**Agent is Firecrawl's magic API** that combines all other features (scraping, crawling, clicking, searching, extracting) into one AI-powered agent. It autonomously searches, navigates, and gathers data from anywhere on the web - accomplishing in minutes what would take humans hours.

**Key Features:**
1. **Agent**: AI-powered autonomous web research and data extraction (combines all features below)
2. **Models**: Firecrawls own models for better extraction
2. **Scrape**: Extract content from a single URL in LLM-ready format
3. **Crawl**: Scrape all accessible URLs from a website automatically
4. **Map**: Quickly get all URLs from a website
5. **Search**: Search the web and get full content from results
6. **Extract**: Use AI to extract structured data from pages


## Agent - Deep Web Research

[Agent Documentation](https://docs.firecrawl.dev/features/agent)

Agent autonomously searches, navigates, and gathers data from anywhere on the web. No URLs required!

**Parameters:**
- `prompt` - **REQUIRED**: Natural language description of the data you want to extract
- `schema` - optional: JSON schema for structured output (supports Pydantic/Zod)
- `urls` - optional: List of URLs to focus the agent's search scope
- `model` - optional: Choose between `spark-1-mini` (default) or `spark-1-pro`
- `maxCredits` - optional: Set maximum credits to spend (for cost control)

## Models

[Models Documentation](https://docs.firecrawl.dev/features/models)

- `spark-1-mini` - **Default**, 60% cheaper, good for most tasks
- `spark-1-pro` - Higher accuracy for complex research and critical extraction

**When to use Pro:** Multi-domain competitive analysis, complex reasoning, or when accuracy is critical


## Scrape

[Scrape Documentation](https://docs.firecrawl.dev/features/scrape)

### Available Output Formats

- **markdown**: Clean markdown optimized for LLMs
- **html**: Raw HTML content
- **links**: All links found on the page
- **screenshot**: Visual screenshot of the page
- **extract**: Structured data extraction using AI

### Actions

[Actions Documentation](https://docs.firecrawl.dev/features/scrape#actions)

Firecrawl allows you to interact with web pages before scraping (clicking, typing, scrolling, waiting). This is useful for dynamic content, logins, or navigating through pages.

## Crawl

[Crawl Documentation](https://docs.firecrawl.dev/features/crawl)

The `crawl` method automatically discovers and scrapes all accessible pages from a website. It intelligently explores the website structure and extracts content from all reachable pages.

### Crawl Parameters

- **limit**: Maximum number of pages to crawl
- **max_depth**: Maximum depth from the starting URL
- **include_paths**: Only crawl URLs matching these patterns
- **exclude_paths**: Skip URLs matching these patterns
- **ignore_sitemap**: Whether to use sitemap if available
- **scrape_options**: Options to pass to the scrape method for each page

### Asynchronous Crawling

[Async Crawl Documentation](https://docs.firecrawl.dev/features/crawl#async-crawl)

## Extract

[Extract Documentation](https://docs.firecrawl.dev/features/extract)

The Extract feature uses AI to intelligently extract structured data from web pages using schemas or natural language prompts. This is useful for turning unstructured web content into structured data for your applications.

## Map

[Map Documentation](https://docs.firecrawl.dev/features/map)

Quickly get all URLs from a website without scraping content. This is extremely fast and useful for discovering the structure of a website.

## Search

[Search Documentation](https://docs.firecrawl.dev/features/search)

Search the web and get full content from results, including web pages, images, and news articles.

## Advanced Features

### PDF and Document Parsing

[Advanced Scraping Guide](https://docs.firecrawl.dev/get-started/advanced-scraping)

Firecrawl can extract text from PDFs, DOCX files, and images.

### Custom Headers and Authentication

Add custom headers or handle authentication for protected pages.

### Mobile Emulation

Scrape pages as they appear on mobile devices.

### JavaScript-Heavy Sites

Configure wait times and selectors for dynamic content that loads via JavaScript.

## Integrations

[LLM SDKs and Frameworks](https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks)

Firecrawl integrates with popular AI frameworks:

- **LangChain**: Python and JavaScript integrations
- **LlamaIndex**: Query and chat engines
- **CrewAI**: Multi-agent systems
- **Dify**: Low-code AI platform
- **Langflow**: Visual AI workflow builder

## Rate Limits and Pricing

[Rate Limits Documentation](https://docs.firecrawl.dev/get-started/rate-limits)

Firecrawl operates on a credit-based system. Rate limits vary by plan.

## Open Source vs Cloud

[Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-vs-cloud)

Firecrawl is available as both a cloud service and open source under the AGPL-3.0 license. The cloud service is recommended for most use cases due to enhanced features, reliability, and performance.

## Examples and Resources

- **Agent Documentation (Most Important)**: [https://docs.firecrawl.dev/features/agent](https://docs.firecrawl.dev/features/agent)
- **Agent Models**: [https://docs.firecrawl.dev/features/models](https://docs.firecrawl.dev/features/models)
- **Official Documentation**: [https://docs.firecrawl.dev](https://docs.firecrawl.dev)
- **GitHub Repository**: [https://github.com/mendableai/firecrawl](https://github.com/mendableai/firecrawl)
- **API Reference**: [https://docs.firecrawl.dev/api-reference](https://docs.firecrawl.dev/api-reference)
- **Developer Guides**: [https://docs.firecrawl.dev/developer-guides](https://docs.firecrawl.dev/developer-guides)
- **Use Cases**: [https://docs.firecrawl.dev/use-cases](https://docs.firecrawl.dev/use-cases)

Firecrawl provides a comprehensive solution for turning web content into AI-ready data. **The Agent feature is the flagship capability** - it combines scraping, crawling, clicking, searching, and extracting into one AI-powered API that autonomously gathers data from anywhere on the web.
