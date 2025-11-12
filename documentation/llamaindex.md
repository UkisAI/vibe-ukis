- [Welcome to LlamaIndex 🦙 !](https://developers.llamaindex.ai/python/framework/)

# Building an LLM application

Welcome to Understanding LlamaIndex. This is a series of short, bite-sized tutorials on every stage of building an agentic LLM application to get you acquainted with how to use LlamaIndex before diving into more advanced and subtle strategies. If you’re an experienced programmer new to LlamaIndex, this is the place to start.

## Key steps in building an agentic LLM application

[Section titled “Key steps in building an agentic LLM application”](https://developers.llamaindex.ai/python/framework/understanding/#key-steps-in-building-an-agentic-llm-application)

Tip

You might want to read our [high-level\\
concepts](https://developers.llamaindex.ai/python/framework/getting_started/concepts) if these terms are
unfamiliar.

This tutorial has three main parts: **Building a RAG pipeline**, **Building an agent**, and **Building Workflows**, with some smaller sections before and after. Here’s what to expect:

- **[Using LLMs](https://developers.llamaindex.ai/python/framework/understanding/using_llms)**: hit the ground running by getting started working with LLMs. We’ll show you how to use any of our [dozens of supported LLMs](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/modules), whether via remote API calls or running locally on your machine.

- **[Building agents](https://developers.llamaindex.ai/python/framework/understanding/agent)**: agents are LLM-powered knowledge workers that can interact with the world via a set of tools. Those tools can retrieve information (such as RAG, see below) or take action. This tutorial includes:
  - **[Building a single agent](https://developers.llamaindex.ai/python/framework/understanding/agent)**: We show you how to build a simple agent that can interact with the world via a set of tools.

  - **[Using existing tools](https://developers.llamaindex.ai/python/framework/understanding/agent/tools)**: LlamaIndex provides a registry of pre-built agent tools at [LlamaHub](https://llamahub.ai/) that you can incorporate into your agents.

  - **[Maintaining state](https://developers.llamaindex.ai/python/framework/understanding/agent/state)**: agents can maintain state, which is important for building more complex applications.

  - **[Streaming output and events](https://developers.llamaindex.ai/python/framework/understanding/agent/streaming)**: providing visibility and feedback to the user is important, and streaming allows you to do that.

  - **[Human in the loop](https://developers.llamaindex.ai/python/framework/understanding/agent/human_in_the_loop)**: getting human feedback to your agent can be critical.

  - **[Multi-agent systems with AgentWorkflow](https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent)**: combining multiple agents to collaborate is a powerful technique for building more complex systems; this section shows you how to do so.
- **[Workflows](https://developers.llamaindex.ai/python/framework/understanding/workflows)**: Workflows are a lower-level, event-driven abstraction for building agentic applications. They’re the base layer you should be using to build any advanced agentic application. You can use the pre-built abstractions you learned above, or build agents completely from scratch. This tutorial covers:
  - **[Building a simple workflow](https://developers.llamaindex.ai/python/framework/understanding/workflows)**: a simple workflow that shows you how to use the `Workflow` class to build a basic agentic application.

  - **[Looping and branching](https://developers.llamaindex.ai/python/framework/understanding/workflows/branches_and_loops)**: these core control flow patterns are the building blocks of more complex workflows.

  - **[Concurrent execution](https://developers.llamaindex.ai/python/framework/understanding/workflows/concurrent_execution)**: you can run steps in parallel to split up work efficiently.

  - **[Streaming events](https://developers.llamaindex.ai/python/framework/understanding/workflows/stream)**: your agents can emit user-facing events just like the agents you built above.

  - **[Stateful workflows](https://developers.llamaindex.ai/python/framework/understanding/workflows/state)**: workflows can maintain state, which is important for building more complex applications.

  - **[Observability](https://developers.llamaindex.ai/python/framework/understanding/workflows/observability)**: workflows can be traced and debugged using various integrations like Arize Pheonix, OpenTelemetry, and more.
- **[Adding RAG to your agents](https://developers.llamaindex.ai/python/framework/understanding/rag)**: Retrieval-Augmented Generation (RAG) is a key technique for getting your data to an LLM, and a component of more sophisticated agentic systems. We’ll show you how to enhance your agents with a full-featured RAG pipeline that can answer questions about your data. This includes:
  - **[Loading & Ingestion](https://developers.llamaindex.ai/python/framework/understanding/rag/loading)**: Getting your data from wherever it lives, whether that’s unstructured text, PDFs, databases, or APIs to other applications. LlamaIndex has hundreds of connectors to every data source over at [LlamaHub](https://llamahub.ai/).

  - **[Indexing and Embedding](https://developers.llamaindex.ai/python/framework/understanding/rag/indexing)**: Once you’ve got your data there are an infinite number of ways to structure access to that data to ensure your applications is always working with the most relevant data. LlamaIndex has a huge number of these strategies built-in and can help you select the best ones.

  - **[Storing](https://developers.llamaindex.ai/python/framework/understanding/rag/storing)**: You will probably find it more efficient to store your data in indexed form, or pre-processed summaries provided by an LLM, often in a specialized database known as a `Vector Store` (see below). You can also store your indexes, metadata and more.

  - **[Querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying)**: Every indexing strategy has a corresponding querying strategy and there are lots of ways to improve the relevance, speed and accuracy of what you retrieve and what the LLM does with it before returning it to you, including turning it into structured responses such as an API.
- **[Putting it all together](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together)**: whether you are building question & answering, chatbots, an API, or an autonomous agent, we show you how to get your application into production.

- **[Tracing and debugging](https://developers.llamaindex.ai/python/framework/understanding/tracing_and_debugging/tracing_and_debugging)**: also called **observability**, it’s especially important with LLM applications to be able to look into the inner workings of what’s going on to help you debug problems and spot places to improve.

- **[Evaluating](https://developers.llamaindex.ai/python/framework/understanding/evaluating/evaluating)**: every strategy has pros and cons and a key part of building, shipping and evolving your application is evaluating whether your change has improved your application in terms of accuracy, performance, clarity, cost and more. Reliably evaluating your changes is a crucial part of LLM application development.


- Getting Started
- [High-Level Concepts](https://developers.llamaindex.ai/python/framework/getting_started/concepts/)
- [Installation and Setup](https://developers.llamaindex.ai/python/framework/getting_started/installation/)
- [How to read these docs](https://developers.llamaindex.ai/python/framework/getting_started/reading/)
- [Starter Tutorial (Using OpenAI)](https://developers.llamaindex.ai/python/framework/getting_started/starter_example/)
- [Starter Tutorial (Using Local LLMs)](https://developers.llamaindex.ai/python/framework/getting_started/starter_example_local/)
- [Discover LlamaIndex Video Series](https://developers.llamaindex.ai/python/framework/getting_started/discover_llamaindex/)
- [Frequently Asked Questions (FAQ)](https://developers.llamaindex.ai/python/framework/getting_started/faq/)
- Starter Tools
- [Starter Tools](https://developers.llamaindex.ai/python/framework/getting_started/starter_tools/)
- [RAG CLI](https://developers.llamaindex.ai/python/framework/getting_started/starter_tools/rag_cli/)
- [Async Programming in Python](https://developers.llamaindex.ai/python/framework/getting_started/async_python/)
- Learn
- [Building an LLM application](https://developers.llamaindex.ai/python/framework/understanding/)
- [Using LLMs](https://developers.llamaindex.ai/python/framework/understanding/using_llms/)
- Building agents
- [Building an agent](https://developers.llamaindex.ai/python/framework/understanding/agent/)
- [Using existing tools](https://developers.llamaindex.ai/python/framework/understanding/agent/tools/)
- [Maintaining state](https://developers.llamaindex.ai/python/framework/understanding/agent/state/)
- [Streaming output and events](https://developers.llamaindex.ai/python/framework/understanding/agent/streaming/)
- [Human in the loop](https://developers.llamaindex.ai/python/framework/understanding/agent/human_in_the_loop/)
- [Multi-agent patterns in LlamaIndex](https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent/)
- [Using Structured Output](https://developers.llamaindex.ai/python/framework/understanding/agent/structured_output/)



- Building Workflows



- [Workflows introduction](https://developers.llamaindex.ai/python/framework/understanding/workflows/)
- [Basic workflow](https://developers.llamaindex.ai/python/framework/understanding/workflows/basic_flow/)
- [Branches and loops](https://developers.llamaindex.ai/python/framework/understanding/workflows/branches_and_loops/)
- [Maintaining state](https://developers.llamaindex.ai/python/framework/understanding/workflows/state/)
- [Streaming events](https://developers.llamaindex.ai/python/framework/understanding/workflows/stream/)
- [Concurrent execution of workflows](https://developers.llamaindex.ai/python/framework/understanding/workflows/concurrent_execution/)
- [Subclassing workflows](https://developers.llamaindex.ai/python/framework/understanding/workflows/subclass/)
- [Resources](https://developers.llamaindex.ai/python/framework/understanding/workflows/resources/)
- [Observability](https://developers.llamaindex.ai/python/framework/understanding/workflows/observability/)
- [Workflows from unbound functions](https://developers.llamaindex.ai/python/framework/understanding/workflows/unbound_functions/)

#Building a RAG pipeline



- [Introduction to RAG](https://developers.llamaindex.ai/python/framework/understanding/rag/)
- Indexing



- [Indexing](https://developers.llamaindex.ai/python/framework/understanding/rag/indexing/)

- Loading



- [Loading Data (Ingestion)](https://developers.llamaindex.ai/python/framework/understanding/rag/loading/)
- [Loading from LlamaCloud](https://developers.llamaindex.ai/python/framework/understanding/rag/loading/llamacloud/)
- [LlamaHub](https://developers.llamaindex.ai/python/framework/understanding/rag/loading/llamahub/)

- Querying



- [Querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/)

- Storing



- [Storing](https://developers.llamaindex.ai/python/framework/understanding/rag/storing/)

- Structured Data Extraction



- [Introduction to Structured Data Extraction](https://developers.llamaindex.ai/python/framework/understanding/extraction/)
- [Using Structured LLMs](https://developers.llamaindex.ai/python/framework/understanding/extraction/structured_llms/)
- [Structured Prediction](https://developers.llamaindex.ai/python/framework/understanding/extraction/structured_prediction/)
- [Low-level structured data extraction](https://developers.llamaindex.ai/python/framework/understanding/extraction/lower_level/)
- [Structured Input](https://developers.llamaindex.ai/python/framework/understanding/extraction/structured_input/)

- Tracing And Debugging



- [Tracing and Debugging](https://developers.llamaindex.ai/python/framework/understanding/tracing_and_debugging/tracing_and_debugging/)

- Evaluating



- Cost Analysis



- [Cost Analysis](https://developers.llamaindex.ai/python/framework/understanding/evaluating/cost_analysis/)
- [Usage Pattern](https://developers.llamaindex.ai/python/framework/understanding/evaluating/cost_analysis/usage_pattern/)

- [Evaluating](https://developers.llamaindex.ai/python/framework/understanding/evaluating/evaluating/)

- Putting It All Together



- [Putting It All Together](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/)
- [Agents](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/agents/)
- Apps



- [Full-Stack Web Application](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/apps/)
- [A Guide to Building a Full-Stack Web App with LLamaIndex](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/apps/fullstack_app_guide/)
- [A Guide to Building a Full-Stack LlamaIndex Web App with Delphic](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/apps/fullstack_with_delphic/)

- Chatbots



- [How to Build a Chatbot](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/chatbots/building_a_chatbot/)

- Q And A



- [Q&A patterns](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/q_and_a/)
- [A Guide to Extracting Terms and Definitions](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/q_and_a/terms_definitions_tutorial/)

- Structured Data



- [Structured Data](https://developers.llamaindex.ai/python/framework/understanding/putting_it_all_together/structured_data/)

- [Privacy and Security](https://developers.llamaindex.ai/python/framework/understanding/privacy/)

- Use Cases



- [Use Cases](https://developers.llamaindex.ai/python/framework/use_cases/)
- [Agents](https://developers.llamaindex.ai/python/framework/use_cases/agents/)
- [Chatbots](https://developers.llamaindex.ai/python/framework/use_cases/chatbots/)
- [Structured Data Extraction](https://developers.llamaindex.ai/python/framework/use_cases/extraction/)
- [Fine-tuning](https://developers.llamaindex.ai/python/framework/use_cases/fine_tuning/)
- [Querying Graphs](https://developers.llamaindex.ai/python/framework/use_cases/graph_querying/)
- [Multi-modal](https://developers.llamaindex.ai/python/framework/use_cases/multimodal/)
- [Prompting](https://developers.llamaindex.ai/python/framework/use_cases/prompting/)
- [Question-Answering (RAG)](https://developers.llamaindex.ai/python/framework/use_cases/q_and_a/)
- [Querying CSVs](https://developers.llamaindex.ai/python/framework/use_cases/querying_csvs/)
- [Parsing Tables and Charts](https://developers.llamaindex.ai/python/framework/use_cases/tables_charts/)
- [Text to SQL](https://developers.llamaindex.ai/python/framework/use_cases/text_to_sql/)

- Component Guides



- [Component Guides](https://developers.llamaindex.ai/python/framework/module_guides/)
- Deploying



- Agents



- [Agents](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/)
- [Memory](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/memory/)
- [Module Guides](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/modules/)
- [Tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/)

- Chat Engines



- [Chat Engine](https://developers.llamaindex.ai/python/framework/module_guides/deploying/chat_engines/)
- [Module Guides](https://developers.llamaindex.ai/python/framework/module_guides/deploying/chat_engines/modules/)
- [Usage Pattern](https://developers.llamaindex.ai/python/framework/module_guides/deploying/chat_engines/usage_pattern/)

- Query Engine



- [Query Engine](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/)
- [Module Guides](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/modules/)
- [Response Modes](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/response_modes/)
- [Streaming](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/streaming/)
- [Supporting Modules](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/supporting_modules/)
- [Usage Pattern](https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine/usage_pattern/)

- Evaluating



- [Evaluating](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/)
- [Contributing A \`LabelledRagDataset\`](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/contributing_llamadatasets/)
- [Evaluating Evaluators with \`LabelledEvaluatorDataset\`'s](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/evaluating_evaluators_with_llamadatasets/)
- [Evaluating With \`LabelledRagDataset\`'s](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/evaluating_with_llamadatasets/)
- [Modules](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/modules/)
- [Usage Pattern (Response Evaluation)](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/usage_pattern/)
- [Usage Pattern (Retrieval)](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/usage_pattern_retrieval/)

- Indexing



- [Indexing](https://developers.llamaindex.ai/python/framework/module_guides/indexing/)
- [Document Management](https://developers.llamaindex.ai/python/framework/module_guides/indexing/document_management/)
- [How Each Index Works](https://developers.llamaindex.ai/python/framework/module_guides/indexing/index_guide/)
- [LlamaCloudIndex + LlamaCloudRetriever](https://developers.llamaindex.ai/python/framework/module_guides/indexing/llama_cloud_index/)
- [Using a Property Graph Index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/)
- [Metadata Extraction](https://developers.llamaindex.ai/python/framework/module_guides/indexing/metadata_extraction/)
- [Module Guides](https://developers.llamaindex.ai/python/framework/module_guides/indexing/modules/)
- [Using VectorStoreIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/)

- Loading



- [Loading Data](https://developers.llamaindex.ai/python/framework/module_guides/loading/)
- Connector



- [Data Connectors (LlamaHub)](https://developers.llamaindex.ai/python/framework/module_guides/loading/connector/)
- [LlamaParse](https://developers.llamaindex.ai/python/framework/module_guides/loading/connector/llama_parse/)
- [Module Guides](https://developers.llamaindex.ai/python/framework/module_guides/loading/connector/modules/)
- [Usage Pattern](https://developers.llamaindex.ai/python/framework/module_guides/loading/connector/usage_pattern/)

- Documents And Nodes



- [Documents / Nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/)
- [Defining and Customizing Documents](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_documents/)
- [Metadata Extraction Usage Pattern](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_metadata_extractor/)
- [Defining and Customizing Nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_nodes/)

- Ingestion Pipeline



- [Ingestion Pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/)
- [Transformations](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/transformations/)

- Node Parsers



- [Node Parser Usage Pattern](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/)
- [Node Parser Modules](https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/modules/)

- [SimpleDirectoryReader](https://developers.llamaindex.ai/python/framework/module_guides/loading/simpledirectoryreader/)

- MCP



- [Model Context Protocol (MCP)](https://developers.llamaindex.ai/python/framework/module_guides/mcp/)
- [Converting Existing LlamaIndex Workflows & Tools to MCP](https://developers.llamaindex.ai/python/framework/module_guides/mcp/convert_existing/)
- [LlamaCloud MCP Servers & Tools](https://developers.llamaindex.ai/python/framework/module_guides/mcp/llamacloud_mcp/)
- [Using MCP Tools with LlamaIndex](https://developers.llamaindex.ai/python/framework/module_guides/mcp/llamaindex_mcp/)

- Models



- [Models](https://developers.llamaindex.ai/python/framework/module_guides/models/)
- [Embeddings](https://developers.llamaindex.ai/python/framework/module_guides/models/embeddings/)
- Llms



- [Using LLMs](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/)
- [Using local models](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/local/)
- [Available LLM integrations](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/modules/)
- [Customizing LLMs within LlamaIndex Abstractions](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/usage_custom/)
- [Using LLMs as standalone modules](https://developers.llamaindex.ai/python/framework/module_guides/models/llms/usage_standalone/)

- [Multi-modal models](https://developers.llamaindex.ai/python/framework/module_guides/models/multi_modal/)
- Prompts



- [Prompts](https://developers.llamaindex.ai/python/framework/module_guides/models/prompts/)
- [Prompt Usage Pattern](https://developers.llamaindex.ai/python/framework/module_guides/models/prompts/usage_pattern/)

- Observability



- [Observability](https://developers.llamaindex.ai/python/framework/module_guides/observability/)
- Callbacks



- [Callbacks](https://developers.llamaindex.ai/python/framework/module_guides/observability/callbacks/)
- [Token Counting - Migration Guide](https://developers.llamaindex.ai/python/framework/module_guides/observability/callbacks/token_counting_migration/)

- [Instrumentation](https://developers.llamaindex.ai/python/framework/module_guides/observability/instrumentation/)

- Querying



- [Querying](https://developers.llamaindex.ai/python/framework/module_guides/querying/)
- Node Postprocessors



- [Node Postprocessor](https://developers.llamaindex.ai/python/framework/module_guides/querying/node_postprocessors/)
- [Node Postprocessor Modules](https://developers.llamaindex.ai/python/framework/module_guides/querying/node_postprocessors/node_postprocessors/)

- Response Synthesizers



- [Response Synthesizer](https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/)
- [Response Synthesis Modules](https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/)

- Retriever



- [Retriever](https://developers.llamaindex.ai/python/framework/module_guides/querying/retriever/)
- [Retriever Modes](https://developers.llamaindex.ai/python/framework/module_guides/querying/retriever/retriever_modes/)
- [Retriever Modules](https://developers.llamaindex.ai/python/framework/module_guides/querying/retriever/retrievers/)

- Router



- [Routers](https://developers.llamaindex.ai/python/framework/module_guides/querying/router/)

- Structured Outputs



- [Structured Outputs](https://developers.llamaindex.ai/python/framework/module_guides/querying/structured_outputs/)
- [Output Parsing Modules](https://developers.llamaindex.ai/python/framework/module_guides/querying/structured_outputs/output_parser/)
- [Pydantic Programs](https://developers.llamaindex.ai/python/framework/module_guides/querying/structured_outputs/pydantic_program/)
- [(Deprecated) Query Engines + Pydantic Outputs](https://developers.llamaindex.ai/python/framework/module_guides/querying/structured_outputs/query_engine/)

- Storing



- [Storing](https://developers.llamaindex.ai/python/framework/module_guides/storing/)
- [Chat Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/chat_stores/)
- [Customizing Storage](https://developers.llamaindex.ai/python/framework/module_guides/storing/customization/)
- [Document Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/docstores/)
- [Index Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/index_stores/)
- [Key-Value Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/kv_stores/)
- [Persisting & Loading Data](https://developers.llamaindex.ai/python/framework/module_guides/storing/save_load/)
- [Vector Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/vector_stores/)

- Supporting Modules



- [Migrating from ServiceContext to Settings](https://developers.llamaindex.ai/python/framework/module_guides/supporting_modules/service_context_migration/)
- [Configuring Settings](https://developers.llamaindex.ai/python/framework/module_guides/supporting_modules/settings/)
- [Supporting Modules](https://developers.llamaindex.ai/python/framework/module_guides/supporting_modules/supporting_modules/)

- Workflow



- [Workflows](https://developers.llamaindex.ai/python/framework/module_guides/workflow/)

- Open Source Community



- FAQ



- [Frequently Asked Questions](https://developers.llamaindex.ai/python/framework/community/faq/)
- [Chat Engines](https://developers.llamaindex.ai/python/framework/community/faq/chat_engines/)
- [Documents and Nodes](https://developers.llamaindex.ai/python/framework/community/faq/documents_and_nodes/)
- [Embeddings](https://developers.llamaindex.ai/python/framework/community/faq/embeddings/)
- [Large Language Models](https://developers.llamaindex.ai/python/framework/community/faq/llms/)
- [Query Engines](https://developers.llamaindex.ai/python/framework/community/faq/query_engines/)
- [Vector Database](https://developers.llamaindex.ai/python/framework/community/faq/vector_database/)

- [Full-Stack Projects](https://developers.llamaindex.ai/python/framework/community/full_stack_projects/)
- Integrations



- [Integrations](https://developers.llamaindex.ai/python/framework/community/integrations/)
- [ChatGPT Plugin Integrations](https://developers.llamaindex.ai/python/framework/community/integrations/chatgpt_plugins/)
- [Unit Testing LLMs/RAG With DeepEval](https://developers.llamaindex.ai/python/framework/community/integrations/deepeval/)
- [Fleet Context Embeddings - Building a Hybrid Search Engine for the Llamaindex Library](https://developers.llamaindex.ai/python/framework/community/integrations/fleet_libraries_context/)
- [Using Graph Stores](https://developers.llamaindex.ai/python/framework/community/integrations/graph_stores/)
- [Tracing with Graphsignal](https://developers.llamaindex.ai/python/framework/community/integrations/graphsignal/)
- [Guidance](https://developers.llamaindex.ai/python/framework/community/integrations/guidance/)
- [LM Format Enforcer](https://developers.llamaindex.ai/python/framework/community/integrations/lmformatenforcer/)
- [Using Managed Indices](https://developers.llamaindex.ai/python/framework/community/integrations/managed_indices/)
- [Tonic Validate](https://developers.llamaindex.ai/python/framework/community/integrations/tonicvalidate/)
- [Evaluating and Tracking with TruLens](https://developers.llamaindex.ai/python/framework/community/integrations/trulens/)
- [Perform Evaluations on LlamaIndex with UpTrain](https://developers.llamaindex.ai/python/framework/community/integrations/uptrain/)
- [Using Vector Stores](https://developers.llamaindex.ai/python/framework/community/integrations/vector_stores/)

- Llama Packs



- [Llama Packs 🦙📦](https://developers.llamaindex.ai/python/framework/community/llama_packs/)

- [ChangeLog](https://developers.llamaindex.ai/python/framework/changelog/)

- Examples



- LLMs



- [AI21](https://developers.llamaindex.ai/python/examples/llm/ai21/)
- [Aleph Alpha](https://developers.llamaindex.ai/python/examples/llm/alephalpha/)
- [Anthropic](https://developers.llamaindex.ai/python/examples/llm/anthropic/)
- [Anthropic Prompt Caching](https://developers.llamaindex.ai/python/examples/llm/anthropic_prompt_caching/)
- [Anyscale](https://developers.llamaindex.ai/python/examples/llm/anyscale/)
- [ASI LLM](https://developers.llamaindex.ai/python/examples/llm/asi1/)
- [Azure AI model inference](https://developers.llamaindex.ai/python/examples/llm/azure_inference/)
- [Azure OpenAI](https://developers.llamaindex.ai/python/examples/llm/azure_openai/)
- [Baseten Cookbook](https://developers.llamaindex.ai/python/examples/llm/baseten/)
- [Bedrock](https://developers.llamaindex.ai/python/examples/llm/bedrock/)
- [Bedrock Converse](https://developers.llamaindex.ai/python/examples/llm/bedrock_converse/)
- [Cerebras](https://developers.llamaindex.ai/python/examples/llm/cerebras/)
- [Clarifai LLM](https://developers.llamaindex.ai/python/examples/llm/clarifai/)
- [Cleanlab Trustworthy Language Model](https://developers.llamaindex.ai/python/examples/llm/cleanlab/)
- [Cohere](https://developers.llamaindex.ai/python/examples/llm/cohere/)
- [CometAPI](https://developers.llamaindex.ai/python/examples/llm/cometapi/)
- [DashScope LLMS](https://developers.llamaindex.ai/python/examples/llm/dashscope/)
- [Databricks](https://developers.llamaindex.ai/python/examples/llm/databricks/)
- [DeepInfra](https://developers.llamaindex.ai/python/examples/llm/deepinfra/)
- [DeepSeek](https://developers.llamaindex.ai/python/examples/llm/deepseek/)
- [EverlyAI](https://developers.llamaindex.ai/python/examples/llm/everlyai/)
- [Featherless AI LLM](https://developers.llamaindex.ai/python/examples/llm/featherlessai/)
- [Fireworks](https://developers.llamaindex.ai/python/examples/llm/fireworks/)
- [Fireworks Function Calling Cookbook](https://developers.llamaindex.ai/python/examples/llm/fireworks_cookbook/)
- [Friendli](https://developers.llamaindex.ai/python/examples/llm/friendli/)
- [Gemini](https://developers.llamaindex.ai/python/examples/llm/gemini/)
- [Google GenAI](https://developers.llamaindex.ai/python/examples/llm/google_genai/)
- [Grok 4](https://developers.llamaindex.ai/python/examples/llm/grok/)
- [Groq](https://developers.llamaindex.ai/python/examples/llm/groq/)
- [Heroku LLM Managed Inference](https://developers.llamaindex.ai/python/examples/llm/heroku/)
- [Hugging Face LLMs](https://developers.llamaindex.ai/python/examples/llm/huggingface/)
- [IBM watsonx.ai](https://developers.llamaindex.ai/python/examples/llm/ibm_watsonx/)
- [IPEX-LLM on Intel CPU](https://developers.llamaindex.ai/python/examples/llm/ipex_llm/)
- [IPEX-LLM on Intel GPU](https://developers.llamaindex.ai/python/examples/llm/ipex_llm_gpu/)
- [Konko](https://developers.llamaindex.ai/python/examples/llm/konko/)
- [LangChain LLM](https://developers.llamaindex.ai/python/examples/llm/langchain/)
- [LiteLLM](https://developers.llamaindex.ai/python/examples/llm/litellm/)
- [Replicate - Llama 2 13B](https://developers.llamaindex.ai/python/examples/llm/llama_2/)
- [🦙 x 🦙 Rap Battle](https://developers.llamaindex.ai/python/examples/llm/llama_2_rap_battle/)
- [Llama API](https://developers.llamaindex.ai/python/examples/llm/llama_api/)
- [LlamaCPP](https://developers.llamaindex.ai/python/examples/llm/llama_cpp/)
- [llamafile](https://developers.llamaindex.ai/python/examples/llm/llamafile/)
- [LLM Predictor](https://developers.llamaindex.ai/python/examples/llm/llm_predictor/)
- [LM Studio](https://developers.llamaindex.ai/python/examples/llm/lmstudio/)
- [LocalAI](https://developers.llamaindex.ai/python/examples/llm/localai/)
- [Maritalk](https://developers.llamaindex.ai/python/examples/llm/maritalk/)
- [MistralRS LLM](https://developers.llamaindex.ai/python/examples/llm/mistral_rs/)
- [MistralAI](https://developers.llamaindex.ai/python/examples/llm/mistralai/)
- [ModelScope LLMS](https://developers.llamaindex.ai/python/examples/llm/modelscope/)
- [Monster API <> LLamaIndex](https://developers.llamaindex.ai/python/examples/llm/monsterapi/)
- [MyMagic AI LLM](https://developers.llamaindex.ai/python/examples/llm/mymagic/)
- [Nebius LLMs](https://developers.llamaindex.ai/python/examples/llm/nebius/)
- [Netmind AI LLM](https://developers.llamaindex.ai/python/examples/llm/netmind/)
- [Neutrino AI](https://developers.llamaindex.ai/python/examples/llm/neutrino/)
- [NVIDIA NIMs](https://developers.llamaindex.ai/python/examples/llm/nvidia/)
- [NVIDIA NIMs](https://developers.llamaindex.ai/python/examples/llm/nvidia_nim/)
- [Nvidia TensorRT-LLM](https://developers.llamaindex.ai/python/examples/llm/nvidia_tensorrt/)
- [NVIDIA's LLM Text Completion API](https://developers.llamaindex.ai/python/examples/llm/nvidia_text_completion/)
- [Nvidia Triton](https://developers.llamaindex.ai/python/examples/llm/nvidia_triton/)
- [Oracle Cloud Infrastructure Data Science](https://developers.llamaindex.ai/python/examples/llm/oci_data_science/)
- [Oracle Cloud Infrastructure Generative AI](https://developers.llamaindex.ai/python/examples/llm/oci_genai/)
- [OctoAI](https://developers.llamaindex.ai/python/examples/llm/octoai/)
- [Ollama LLM](https://developers.llamaindex.ai/python/examples/llm/ollama/)
- [Ollama - Gemma](https://developers.llamaindex.ai/python/examples/llm/ollama_gemma/)
- [OpenAI](https://developers.llamaindex.ai/python/examples/llm/openai/)
- [OpenAI JSON Mode vs. Function Calling for Data Extraction](https://developers.llamaindex.ai/python/examples/llm/openai_json_vs_function_calling/)
- [OpenAI Responses API](https://developers.llamaindex.ai/python/examples/llm/openai_responses/)
- [OpenRouter](https://developers.llamaindex.ai/python/examples/llm/openrouter/)
- [OpenVINO LLMs](https://developers.llamaindex.ai/python/examples/llm/openvino/)
- [OpenVINO GenAI LLMs](https://developers.llamaindex.ai/python/examples/llm/openvino-genai/)
- [Optimum Intel LLMs optimized with IPEX backend](https://developers.llamaindex.ai/python/examples/llm/optimum_intel/)
- [Using Opus 4.1 with LlamaIndex](https://developers.llamaindex.ai/python/examples/llm/opus_4_1/)
- [AlibabaCloud-PaiEas](https://developers.llamaindex.ai/python/examples/llm/paieas/)
- [PaLM](https://developers.llamaindex.ai/python/examples/llm/palm/)
- [Perplexity](https://developers.llamaindex.ai/python/examples/llm/perplexity/)
- [\[Pipeshift\](https://pipeshift.com)](https://developers.llamaindex.ai/python/examples/llm/pipeshift/)
- [Portkey](https://developers.llamaindex.ai/python/examples/llm/portkey/)
- [Predibase](https://developers.llamaindex.ai/python/examples/llm/predibase/)
- [PremAI LlamaIndex](https://developers.llamaindex.ai/python/examples/llm/premai/)
- [Client of Baidu Intelligent Cloud's Qianfan LLM Platform](https://developers.llamaindex.ai/python/examples/llm/qianfan/)
- [RunGPT](https://developers.llamaindex.ai/python/examples/llm/rungpt/)
- [Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex](https://developers.llamaindex.ai/python/examples/llm/sagemaker_endpoint_llm/)
- [SambaNova Systems](https://developers.llamaindex.ai/python/examples/llm/sambanovasystems/)
- [Together AI LLM](https://developers.llamaindex.ai/python/examples/llm/together/)
- [Upstage](https://developers.llamaindex.ai/python/examples/llm/upstage/)
- [Vercel AI Gateway](https://developers.llamaindex.ai/python/examples/llm/vercel-ai-gateway/)
- [Vertex AI](https://developers.llamaindex.ai/python/examples/llm/vertex/)
- [Replicate - Vicuna 13B](https://developers.llamaindex.ai/python/examples/llm/vicuna/)
- [vLLM](https://developers.llamaindex.ai/python/examples/llm/vllm/)
- [Xorbits Inference](https://developers.llamaindex.ai/python/examples/llm/xinference_local_deployment/)
- [Yi LLMs](https://developers.llamaindex.ai/python/examples/llm/yi/)

- Embeddings



- [Aleph Alpha Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/alephalpha/)
- [Anyscale Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/anyscale/)
- [Baseten Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/baseten/)
- [Bedrock Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/bedrock/)
- [Embeddings with Clarifai](https://developers.llamaindex.ai/python/examples/embeddings/clarifai/)
- [Cloudflare Workers AI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/cloudflare_workersai/)
- [CohereAI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/cohereai/)
- [Custom Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/custom_embeddings/)
- [DashScope Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/dashscope_embeddings/)
- [Databricks Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/databricks/)
- [DeepInfra](https://developers.llamaindex.ai/python/examples/embeddings/deepinfra/)
- [Elasticsearch Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/elasticsearch/)
- [Qdrant FastEmbed Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/fastembed/)
- [Fireworks Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/fireworks/)
- [Google Gemini Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/gemini/)
- [GigaChat](https://developers.llamaindex.ai/python/examples/embeddings/gigachat/)
- [Google GenAI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/google_genai/)
- [Google PaLM Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/google_palm/)
- [Heroku LLM Managed Inference Embedding](https://developers.llamaindex.ai/python/examples/embeddings/heroku/)
- [Local Embeddings with HuggingFace](https://developers.llamaindex.ai/python/examples/embeddings/huggingface/)
- [IBM watsonx.ai](https://developers.llamaindex.ai/python/examples/embeddings/ibm_watsonx/)
- [Local Embeddings with IPEX-LLM on Intel CPU](https://developers.llamaindex.ai/python/examples/embeddings/ipex_llm/)
- [Local Embeddings with IPEX-LLM on Intel GPU](https://developers.llamaindex.ai/python/examples/embeddings/ipex_llm_gpu/)
- [Jina 8K Context Window Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/jina_embeddings/)
- [Jina Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/jinaai_embeddings/)
- [LangChain Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/langchain/)
- [Llamafile Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/llamafile/)
- [LLMRails Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/llm_rails/)
- [MistralAI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/mistralai/)
- [Mixedbread AI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/mixedbreadai/)
- [ModelScope Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/modelscope/)
- [Nebius Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/nebius/)
- [Netmind AI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/netmind/)
- [Nomic Embedding](https://developers.llamaindex.ai/python/examples/embeddings/nomic/)
- [NVIDIA NIMs](https://developers.llamaindex.ai/python/examples/embeddings/nvidia/)
- [Oracle Cloud Infrastructure (OCI) Data Science Service](https://developers.llamaindex.ai/python/examples/embeddings/oci_data_science/)
- [Oracle Cloud Infrastructure Generative AI](https://developers.llamaindex.ai/python/examples/embeddings/oci_genai/)
- [Ollama Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/ollama_embedding/)
- [OpenAI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/openai/)
- [Local Embeddings with OpenVINO](https://developers.llamaindex.ai/python/examples/embeddings/openvino/)
- [Optimized Embedding Model using Optimum-Intel](https://developers.llamaindex.ai/python/examples/embeddings/optimum_intel/)
- [Oracle AI Vector Search: Generate Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/oracleai/)
- [PremAI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/premai/)
- [Interacting with Embeddings deployed in Amazon SageMaker Endpoint with LlamaIndex](https://developers.llamaindex.ai/python/examples/embeddings/sagemaker_embedding_endpoint/)
- [Text Embedding Inference](https://developers.llamaindex.ai/python/examples/embeddings/text_embedding_inference/)
- [TextEmbed - Embedding Inference Server](https://developers.llamaindex.ai/python/examples/embeddings/textembed/)
- [Together AI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/together/)
- [Upstage Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/upstage/)
- [Interacting with Embeddings deployed in Vertex AI Endpoint with LlamaIndex](https://developers.llamaindex.ai/python/examples/embeddings/vertex_embedding_endpoint/)
- [VoyageAI Embeddings](https://developers.llamaindex.ai/python/examples/embeddings/voyageai/)
- [YandexGPT](https://developers.llamaindex.ai/python/examples/embeddings/yandexgpt/)

- Vector Stores



- [Alibaba Cloud OpenSearch Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/alibabacloudopensearchindexdemo/)
- [Google AlloyDB for PostgreSQL - \`AlloyDBVectorStore\`](https://developers.llamaindex.ai/python/examples/vector_stores/alloydbvectorstoredemo/)
- [Amazon Neptune - Neptune Analytics vector store](https://developers.llamaindex.ai/python/examples/vector_stores/amazonneptunevectordemo/)
- [AnalyticDB](https://developers.llamaindex.ai/python/examples/vector_stores/analyticdbdemo/)
- [ApertureDB as a Vector Store with LlamaIndex.](https://developers.llamaindex.ai/python/examples/vector_stores/aperturedbvectorstoredemo/)
- [Astra DB](https://developers.llamaindex.ai/python/examples/vector_stores/astradbindexdemo/)
- [Simple Vector Store - Async Index Creation](https://developers.llamaindex.ai/python/examples/vector_stores/asyncindexcreationdemo/)
- [Awadb Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/awadbdemo/)
- [Test delete](https://developers.llamaindex.ai/python/examples/vector_stores/awsdocdbdemo/)
- [Azure AI Search](https://developers.llamaindex.ai/python/examples/vector_stores/azureaisearchindexdemo/)
- [Azure CosmosDB MongoDB Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/azurecosmosdbmongodbvcoredemo/)
- [Azure Cosmos DB No SQL Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/azurecosmosdbnosqldemo/)
- [Azure Postgres Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/azurepostgresql/)
- [Bagel Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/bagelautoretriever/)
- [Bagel Network](https://developers.llamaindex.ai/python/examples/vector_stores/bagelindexdemo/)
- [Baidu VectorDB](https://developers.llamaindex.ai/python/examples/vector_stores/baiduvectordbindexdemo/)
- [Cassandra Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/cassandraindexdemo/)
- [Auto-Retrieval from a Vector Database](https://developers.llamaindex.ai/python/examples/vector_stores/chroma_auto_retriever/)
- [Chroma Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/chroma_metadata_filter/)
- [Chroma + Fireworks + Nomic with Matryoshka embedding](https://developers.llamaindex.ai/python/examples/vector_stores/chromafireworksnomic/)
- [Chroma](https://developers.llamaindex.ai/python/examples/vector_stores/chromaindexdemo/)
- [ClickHouse Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/clickhouseindexdemo/)
- [Google Cloud SQL for PostgreSQL - \`PostgresVectorStore\`](https://developers.llamaindex.ai/python/examples/vector_stores/cloudsqlpgvectorstoredemo/)
- [Wait until the cluster is ready for use.](https://developers.llamaindex.ai/python/examples/vector_stores/couchbasevectorstoredemo/)
- [DashVector Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/dashvectorindexdemo/)
- [Databricks Vector Search](https://developers.llamaindex.ai/python/examples/vector_stores/databricksvectorsearchdemo/)
- [IBM Db2 Vector Store and Vector Search](https://developers.llamaindex.ai/python/examples/vector_stores/db2llamavs/)
- [Deep Lake Vector Store Quickstart](https://developers.llamaindex.ai/python/examples/vector_stores/deeplakeindexdemo/)
- [DocArray Hnsw Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/docarrayhnswindexdemo/)
- [DocArray InMemory Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/docarrayinmemoryindexdemo/)
- [Dragonfly and Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/dragonflyindexdemo/)
- [DuckDB](https://developers.llamaindex.ai/python/examples/vector_stores/duckdbdemo/)
- [Auto-Retrieval from a Vector Database](https://developers.llamaindex.ai/python/examples/vector_stores/elasticsearch_auto_retriever/)
- [Elasticsearch](https://developers.llamaindex.ai/python/examples/vector_stores/elasticsearch_demo/)
- [Elasticsearch Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/elasticsearchindexdemo/)
- [Epsilla Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/epsillaindexdemo/)
- Existing data



- [Guide: Using Vector Store Index with Existing Pinecone Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/existing_data/pinecone_existing_data/)
- [Guide: Using Vector Store Index with Existing Weaviate Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/existing_data/weaviate_existing_data/)

- [Faiss Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/faissindexdemo/)
- [Firestore Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/firestorevectorstore/)
- [Gel Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/gel/)
- [Hnswlib](https://developers.llamaindex.ai/python/examples/vector_stores/hnswlibindexdemo/)
- [Hologres](https://developers.llamaindex.ai/python/examples/vector_stores/hologresdemo/)
- [Jaguar Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/jaguarindexdemo/)
- [Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store](https://developers.llamaindex.ai/python/examples/vector_stores/kdbai_advanced_rag_demo/)
- [LanceDB Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/lancedbindexdemo/)
- [Lantern Vector Store (auto-retriever)](https://developers.llamaindex.ai/python/examples/vector_stores/lanternautoretriever/)
- [Lantern Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/lanternindexdemo/)
- [Lindorm](https://developers.llamaindex.ai/python/examples/vector_stores/lindormdemo/)
- [Milvus Vector Store with Async API](https://developers.llamaindex.ai/python/examples/vector_stores/milvusasyncapidemo/)
- [Milvus Vector Store with Full-Text Search](https://developers.llamaindex.ai/python/examples/vector_stores/milvusfulltextsearchdemo/)
- [Milvus Vector Store With Hybrid Search](https://developers.llamaindex.ai/python/examples/vector_stores/milvushybridindexdemo/)
- [Milvus Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/milvusindexdemo/)
- [Milvus Vector Store - Metadata Filter](https://developers.llamaindex.ai/python/examples/vector_stores/milvusoperatorfunctiondemo/)
- [MongoDB Atlas Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/mongodbatlasvectorsearch/)
- [MongoDB Atlas + Fireworks AI RAG Example](https://developers.llamaindex.ai/python/examples/vector_stores/mongodbatlasvectorsearchragfireworks/)
- [MongoDB Atlas + OpenAI RAG Example](https://developers.llamaindex.ai/python/examples/vector_stores/mongodbatlasvectorsearchragopenai/)
- [Moorcheh Vector Store Demo](https://developers.llamaindex.ai/python/examples/vector_stores/moorchehdemo/)
- [MyScale Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/myscaleindexdemo/)
- [Neo4j Vector Store - Metadata Filter](https://developers.llamaindex.ai/python/examples/vector_stores/neo4j_metadata_filter/)
- [Neo4j vector store](https://developers.llamaindex.ai/python/examples/vector_stores/neo4jvectordemo/)
- [Nile Vector Store (Multi-tenant PostgreSQL)](https://developers.llamaindex.ai/python/examples/vector_stores/nilevectorstore/)
- [ObjectBox VectorStore Demo](https://developers.llamaindex.ai/python/examples/vector_stores/objectboxindexdemo/)
- [OceanBase Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/oceanbasevectorstore/)
- [Opensearch Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/opensearchdemo/)
- [Oracle AI Vector Search: Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/orallamavs/)
- [pgvecto.rs](https://developers.llamaindex.ai/python/examples/vector_stores/pgvectorsdemo/)
- [A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)](https://developers.llamaindex.ai/python/examples/vector_stores/pinecone_auto_retriever/)
- [Pinecone Vector Store - Metadata Filter](https://developers.llamaindex.ai/python/examples/vector_stores/pinecone_metadata_filter/)
- [Pinecone Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/pineconeindexdemo/)
- [Pinecone Vector Store - Hybrid Search](https://developers.llamaindex.ai/python/examples/vector_stores/pineconeindexdemo-hybrid/)
- [Postgres Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/postgres/)
- [Hybrid Search with Qdrant BM42](https://developers.llamaindex.ai/python/examples/vector_stores/qdrant_bm42/)
- [Qdrant Hybrid Search](https://developers.llamaindex.ai/python/examples/vector_stores/qdrant_hybrid/)
- [Hybrid RAG with Qdrant: multi-tenancy, custom sharding, distributed setup](https://developers.llamaindex.ai/python/examples/vector_stores/qdrant_hybrid_rag_multitenant_sharding/)
- [Qdrant Vector Store - Metadata Filter](https://developers.llamaindex.ai/python/examples/vector_stores/qdrant_metadata_filter/)
- [Qdrant Vector Store - Default Qdrant Filters](https://developers.llamaindex.ai/python/examples/vector_stores/qdrant_using_qdrant_filters/)
- [Qdrant Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/qdrantindexdemo/)
- [Redis Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/redisindexdemo/)
- [Relyt](https://developers.llamaindex.ai/python/examples/vector_stores/relytdemo/)
- [Rockset Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/rocksetindexdemo/)
- [S3VectorStore Integration](https://developers.llamaindex.ai/python/examples/vector_stores/s3vectorstore/)
- [Simple Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/simpleindexdemo/)
- [Local Llama2 + VectorStoreIndex](https://developers.llamaindex.ai/python/examples/vector_stores/simpleindexdemollama-local/)
- [Llama2 + VectorStoreIndex](https://developers.llamaindex.ai/python/examples/vector_stores/simpleindexdemollama2/)
- [Simple Vector Stores - Maximum Marginal Relevance Retrieval](https://developers.llamaindex.ai/python/examples/vector_stores/simpleindexdemommr/)
- [S3/R2 Storage](https://developers.llamaindex.ai/python/examples/vector_stores/simpleindexons3/)
- [Supabase Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/supabasevectorindexdemo/)
- [TablestoreVectorStore](https://developers.llamaindex.ai/python/examples/vector_stores/tablestoredemo/)
- [Tair Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/tairindexdemo/)
- [Tencent Cloud VectorDB](https://developers.llamaindex.ai/python/examples/vector_stores/tencentvectordbindexdemo/)
- [TiDB Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/tidbvector/)
- [Timescale Vector Store (PostgreSQL)](https://developers.llamaindex.ai/python/examples/vector_stores/timescalevector/)
- [txtai Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/txtaiindexdemo/)
- [Typesense Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/typesensedemo/)
- [Upstash Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/upstashvectordemo/)
- [load documents](https://developers.llamaindex.ai/python/examples/vector_stores/vearchdemo/)
- [Google Vertex AI Vector Search](https://developers.llamaindex.ai/python/examples/vector_stores/vertexaivectorsearchdemo/)
- [Vespa Vector Store demo](https://developers.llamaindex.ai/python/examples/vector_stores/vespaindexdemo/)
- [Auto-Retrieval from a Weaviate Vector Database](https://developers.llamaindex.ai/python/examples/vector_stores/weaviateindex_auto_retriever/)
- [Weaviate Vector Store Metadata Filter](https://developers.llamaindex.ai/python/examples/vector_stores/weaviateindex_metadata_filter/)
- [Weaviate Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/weaviateindexdemo/)
- [Weaviate Vector Store - Hybrid Search](https://developers.llamaindex.ai/python/examples/vector_stores/weaviateindexdemo-hybrid/)
- [\*\*WordLift\*\* Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/wordliftdemo/)
- [Zep Vector Store](https://developers.llamaindex.ai/python/examples/vector_stores/zepindexdemo/)

- Retrievers



- [Auto Merging Retriever](https://developers.llamaindex.ai/python/examples/retrievers/auto_merging_retriever/)
- [Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)](https://developers.llamaindex.ai/python/examples/retrievers/auto_vs_recursive_retriever/)
- [Bedrock (Knowledge Bases)](https://developers.llamaindex.ai/python/examples/retrievers/bedrock_retriever/)
- [BM25 Retriever](https://developers.llamaindex.ai/python/examples/retrievers/bm25_retriever/)
- [Composable Objects](https://developers.llamaindex.ai/python/examples/retrievers/composable_retrievers/)
- [Activeloop Deep Memory](https://developers.llamaindex.ai/python/examples/retrievers/deep_memory/)
- [Ensemble Retrieval Guide](https://developers.llamaindex.ai/python/examples/retrievers/ensemble_retrieval/)
- [Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)](https://developers.llamaindex.ai/python/examples/retrievers/multi_doc_together_hybrid/)
- [Pathway Retriever](https://developers.llamaindex.ai/python/examples/retrievers/pathway_retriever/)
- [Reciprocal Rerank Fusion Retriever](https://developers.llamaindex.ai/python/examples/retrievers/reciprocal_rerank_fusion/)
- [Recursive Retriever + Node References + Braintrust](https://developers.llamaindex.ai/python/examples/retrievers/recurisve_retriever_nodes_braintrust/)
- [Recursive Retriever + Node References](https://developers.llamaindex.ai/python/examples/retrievers/recursive_retriever_nodes/)
- [Relative Score Fusion and Distribution-Based Score Fusion](https://developers.llamaindex.ai/python/examples/retrievers/relative_score_dist_fusion/)
- [Router Retriever](https://developers.llamaindex.ai/python/examples/retrievers/router_retriever/)
- [Simple Fusion Retriever](https://developers.llamaindex.ai/python/examples/retrievers/simple_fusion/)
- [Auto-Retrieval from a Vectara Index](https://developers.llamaindex.ai/python/examples/retrievers/vectara_auto_retriever/)
- [Vertex AI Search Retriever](https://developers.llamaindex.ai/python/examples/retrievers/vertex_ai_search_retriever/)
- [connect to VideoDB](https://developers.llamaindex.ai/python/examples/retrievers/videodb_retriever/)
- [You.com Retriever](https://developers.llamaindex.ai/python/examples/retrievers/you_retriever/)

- [Framework API Reference 🔗](https://developers.llamaindex.ai/python/framework-api-reference/)
