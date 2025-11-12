# Chainlit
## What is Chainlit?

Chainlit enables developers to rapidly build and deploy Conversational AI applications with a focus on user experience and production readiness. The framework provides a complete solution for creating chat-based applications that integrate with any Python program or library.

Chainlit addresses the challenge of building production-grade conversational applications by providing built-in authentication, data persistence, multi-step reasoning visualization, and seamless integration with popular AI frameworks. It allows developers to focus on their AI logic rather than building UI components and infrastructure from scratch.

**GitHub Repository**: [https://github.com/Chainlit/chainlit](https://github.com/Chainlit/chainlit)

**Official Documentation**: [https://docs.chainlit.io/](https://docs.chainlit.io/)

**Cookbook Examples**: [https://github.com/Chainlit/cookbook](https://github.com/Chainlit/cookbook)

## Installation and Setup

### Standard Installation

Install Chainlit using pip:

```bash
pip install chainlit
```

Verify the installation by running the hello app:

```bash
chainlit hello
```

### Forking and Installing from GitHub

**1. Fork the Repository**

Visit the [Chainlit GitHub Repository](https://github.com/Chainlit/chainlit) and click the "Fork" button to create your own copy.

**2. Clone Your Fork**

```bash
git clone https://github.com/your-username/chainlit.git
cd chainlit
```

**3. Install Dependencies**

Create a virtual environment and install dependencies:

```bash
cd backend;poetry install;poetry self add poetry-plugin-shell;poetry shell;
```

**4. Run Chainlit**

```bash
chainlit run app.py
```


## Running Chainlit Applications

### Basic Command

To run a Chainlit application, use the following command:

```bash
chainlit run app.py
```

Replace `app.py` with the path to your Chainlit application script. This command starts the server and opens the application in your default web browser.

### Command Line Options

Chainlit supports various command-line options to customize the runtime behavior:

```bash
chainlit run app.py -w  # Enable auto-reload on file changes
chainlit run app.py --port 8080  # Run on custom port
chainlit run app.py --host 0.0.0.0  # Make accessible on network
```

For more options, refer to the [Command Line Options Documentation](https://docs.chainlit.io/backend/command-line).

## Core Concepts

The Chainlit application follows a structured life cycle with specific hooks for different events:

- **`@cl.on_chat_start`**: Called when a new chat session starts, perfect for initialization logic
- **`@cl.on_message`**: Called every time a user sends a message, the main message handler
- **`@cl.on_chat_end`**: Called when a chat session ends, useful for cleanup
- **`@cl.on_chat_resume`**: Called when resuming a previous chat session

**Example:**

```python
import chainlit as cl

@cl.on_chat_start
async def start():
    # Initialize your application state
    cl.user_session.set("counter", 0)
    await cl.Message(content="Hello! I'm ready to help.").send()

@cl.on_message
async def main(message: cl.Message):
    # Process incoming messages
    counter = cl.user_session.get("counter")
    counter += 1
    cl.user_session.set("counter", counter)

    response = f"Message {counter}: You said '{message.content}'"
    await cl.Message(content=response).send()

@cl.on_chat_end
async def end():
    # Cleanup resources
    print("Chat ended")
```

### Message

[Message Documentation](https://docs.chainlit.io/concepts/message)

The `Message` class is the primary way to communicate with users. A message is a piece of information sent from the user to an assistant and vice versa. It has content, a timestamp, and cannot be nested.

### Chat Life Cycle

[Chat Life Cycle Documentation](https://docs.chainlit.io/concepts/chat-lifecycle)
### Step

[Step Documentation](https://docs.chainlit.io/concepts/step)

A `Step` represents an intermediary operation in your application. LLM-powered assistants take multiple steps to process a user's request, forming a chain of thought. Unlike a Message, a Step has a type, an input/output, and a start/end.

### User Session

[User Session Documentation](https://docs.chainlit.io/concepts/user-session)

The user session provides a way to store data that persists across messages within a single chat session. This is crucial for maintaining state without relying on global variables.

### Element

[Element Documentation](https://docs.chainlit.io/concepts/element)

Elements are rich content types that can be attached to messages, including images, files, audio, video, and PDFs.

### Action

[Action Documentation](https://docs.chainlit.io/concepts/action)

Actions are interactive buttons that users can click. They enable rich interactions beyond simple text responses and can trigger callbacks in your application code.

### Starters

[Starters Documentation](https://docs.chainlit.io/concepts/starters)

Starters provide suggested prompts to help users get started with your application. They appear when a new chat begins.

### Command

[Command Documentation](https://docs.chainlit.io/concepts/command)

Commands capture user intent in a deterministic way. They are special markers that help the assistant understand what the user wants to do.

## API Reference
Chainlit provides a comprehensive API for building conversational AI applications. Below is a complete reference of all available APIs organized by category.


#### on_chat_start

[on_chat_start Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-chat-start)

Hook to react to the user websocket connection event. Called when a new chat session starts.

#### on_chat_end

[on_chat_end Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-chat-end)

Hook called when a chat session ends, useful for cleanup operations and resource management.

#### on_chat_resume

[on_chat_resume Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-chat-resume)

Hook called when resuming a previous chat session from chat history.

#### on_message

[on_message Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-message)

Hook called every time a user sends a message. This is the main message handler for your application.

#### on_logout

[on_logout Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-logout)

Hook called when a user logs out of the application.

#### on_audio_chunk

[on_audio_chunk Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-audio-chunk)

Hook called when an audio chunk is received from the user.

#### on_audio_end

[on_audio_end Documentation](https://docs.chainlit.io/api-reference/lifecycle-hooks/on-audio-end)

Hook called when audio streaming from the user ends.

### Chat Components

Core components for building chat interactions.

#### Message

[Message API Documentation](https://docs.chainlit.io/api-reference/message)

The Message class is the primary way to send information to users.

#### Step Decorator

[Step Decorator Documentation](https://docs.chainlit.io/api-reference/step-decorator)

Decorator to create steps that represent intermediary operations in your application.

#### Step Class

[Step Class Documentation](https://docs.chainlit.io/api-reference/step-class)

The Step class for programmatically creating and managing steps.

#### Action

[Action API Documentation](https://docs.chainlit.io/api-reference/action)

Create interactive buttons that users can click to trigger callbacks.

#### Chat Profiles

[Chat Profiles API Documentation](https://docs.chainlit.io/api-reference/chat-profiles)

Configure multiple AI assistants or modes within the same application.

#### Chat Settings

[Chat Settings API Documentation](https://docs.chainlit.io/api-reference/chat-settings)

Allow users to customize application behavior with real-time settings.

### Elements

Rich content types that can be attached to messages.

#### Custom Element

[Custom Element Documentation](https://docs.chainlit.io/api-reference/elements/custom)

Create custom elements with your own HTML/JavaScript for specialized visualizations.

#### Text Element

[Text Element Documentation](https://docs.chainlit.io/api-reference/elements/text)

Display text content in a dedicated element.

#### Image Element

[Image Element Documentation](https://docs.chainlit.io/api-reference/elements/image)

Display images in your chat messages.

#### DataFrame Element

[DataFrame Element Documentation](https://docs.chainlit.io/api-reference/elements/dataframe)

Display pandas DataFrames as interactive tables.

#### File Element

[File Element Documentation](https://docs.chainlit.io/api-reference/elements/file)

Attach downloadable files to messages.

#### PDF Viewer Element

[PDF Viewer Documentation](https://docs.chainlit.io/api-reference/elements/pdf)

Display PDF documents with an interactive viewer.

#### Audio Element

[Audio Element Documentation](https://docs.chainlit.io/api-reference/elements/audio)

Embed audio players in your chat messages.

#### Video Element

[Video Element Documentation](https://docs.chainlit.io/api-reference/elements/video)

Embed video players in your chat messages.


#### Pyplot Element

[Pyplot Element Documentation](https://docs.chainlit.io/api-reference/elements/pyplot)

Display matplotlib/pyplot figures.

#### TaskList Element

[TaskList Element Documentation](https://docs.chainlit.io/api-reference/elements/tasklist)

Display a list of tasks with status indicators.

### Ask User

Prompt users for additional input during conversation flow.

#### AskUserMessage

[AskUserMessage Documentation](https://docs.chainlit.io/api-reference/ask/ask-for-input)

Prompt the user for text input with a timeout.

#### AskFileMessage

[AskFileMessage Documentation](https://docs.chainlit.io/api-reference/ask/ask-for-file)

Prompt the user to upload one or more files.

#### AskActionMessage

[AskActionMessage Documentation](https://docs.chainlit.io/api-reference/ask/ask-for-action)

Prompt the user to select from multiple action buttons.

#### AskElementMessage

[AskElementMessage Documentation](https://docs.chainlit.io/api-reference/ask/ask-for-element)

Prompt the user to interact with specific elements.

### Integrations

Integration helpers for popular AI frameworks.

#### LlamaIndex Callback Handler

This integration no longer works and is hense removed. You must find a manual way to integrate callback handling.

### Miscellaneous Utilities

Additional utility functions for advanced use cases.

#### author_rename and Message Author

[Author Rename Documentation](https://docs.chainlit.io/api-reference/author-rename)

Customize the display name of message authors.

#### make_async

[make_async Documentation](https://docs.chainlit.io/api-reference/make-async)

Convert synchronous functions to async for use in Chainlit's async context.

#### cache

[Cache Documentation](https://docs.chainlit.io/api-reference/cache)

Cache expensive computations or resources across chat sessions.

#### Data Persistence API

[Data Persistence API Documentation](https://docs.chainlit.io/api-reference/data-persistence)

APIs for implementing custom data persistence layers.

#### Window Messaging

[Window Messaging Documentation](https://docs.chainlit.io/api-reference/window-message)

Communicate between Chainlit and the parent window when embedded in iframe.

### Input Widgets

Components for chat settings and user input.

#### Select Widget

[Select Widget Documentation](https://docs.chainlit.io/api-reference/input-widgets/select)

Dropdown selection widget for chat settings.

#### Slider Widget

[Slider Widget Documentation](https://docs.chainlit.io/api-reference/input-widgets/slider)

Numeric slider widget for chat settings.

#### Switch Widget

[Switch Widget Documentation](https://docs.chainlit.io/api-reference/input-widgets/switch)

Boolean toggle switch widget for chat settings.

#### Tags Widget

[Tags Widget Documentation](https://docs.chainlit.io/api-reference/input-widgets/tags)

Multi-select tags widget for chat settings.

#### TextInput Widget

[TextInput Widget Documentation](https://docs.chainlit.io/api-reference/input-widgets/textinput)

Text input widget for chat settings.

## Integration Support

Chainlit is compatible with all Python programs and libraries, with dedicated integrations for popular AI frameworks:

**Llama Index**: Integration with Llama Index agents, query engines, and chat engines with automatic step tracking

For integration guides, visit the [Integrations Documentation](https://docs.chainlit.io/integrations).

## Advanced Features

### Streaming

[Streaming Documentation](https://docs.chainlit.io/advanced-features/streaming)

Chainlit supports streaming for both Messages and Steps, allowing you to stream responses token-by-token for better user experience.

### Model Context Protocol (MCP)

[MCP Documentation](https://docs.chainlit.io/advanced-features/mcp)

Model Control Protocol (MCP) allows you to integrate external tool providers with your Chainlit application. This enables your AI models to use tools through standardized interfaces.

### Ask User

[Ask User Documentation](https://docs.chainlit.io/advanced-features/ask-user)

Prompt users for additional input during processing
### Chat Profiles

[Chat Profiles Documentation](https://docs.chainlit.io/advanced-features/chat-profiles)

Support multiple AI assistants or modes within the same application

### Chat Settings

[Chat Settings Documentation](https://docs.chainlit.io/advanced-features/chat-settings)

Allow users to customize behavior with real-time settings
## Data Persistence

[Data Persistence Documentation](https://docs.chainlit.io/data-persistence)

### Chat History

[Chat History Documentation](https://docs.chainlit.io/data-persistence/history)

Chainlit supports persistent chat history across sessions. Configure a data layer to automatically save and restore conversations.

### Human Feedback

[Human Feedback Documentation](https://docs.chainlit.io/data-persistence/feedback)

Collect user feedback on messages with built-in thumbs up/down functionality
### Tags & Metadata

[Tags & Metadata Documentation](https://docs.chainlit.io/data-persistence/tags-metadata)

Attach custom metadata to conversations for analytics

[Authentication Documentation](https://docs.chainlit.io/authentication)

Chainlit provides multiple authentication methods to secure your application:

### Password Authentication

[Password Auth Documentation](https://docs.chainlit.io/authentication/password)

Simple username/password authentication for small teams


### Header-Based Authentication

[Header Auth Documentation](https://docs.chainlit.io/authentication/header)

Integrate with existing authentication proxies

### OAuth

[OAuth Documentation](https://docs.chainlit.io/authentication/oauth)

Support for OAuth providers (Google, GitHub, Azure AD, Okta, etc.):

## Customization
[Customization Documentation](https://docs.chainlit.io/customisation)

Chainlit applications can be fully customized to match your brand and requirements.

### Avatars
[Avatars Documentation](https://docs.chainlit.io/customisation/avatars)

### Logo and Favicon

[Logo Documentation](https://docs.chainlit.io/customisation/custom-logo-and-favicon)

### Theme and Primary Color

[Theme Documentation](https://docs.chainlit.io/customisation/theme)

#### Changing Primary Color in Fork

in frontend folder in index.css you can change the colors

### Hiding Chain of Thought (Steps)

[Config Documentation](https://docs.chainlit.io/backend/config)

### Translation

[Translation Documentation](https://docs.chainlit.io/customisation/translation)
Support multiple languages with i18n by configuring translations in your project.

## Copilot Mode

[Copilot Documentation](https://docs.chainlit.io/deploy/copilot)

##Discord

[Disord] (https://docs.chainlit.io/deploy/discord)

##Teams
[Teams] (https://docs.chainlit.io/deploy/teams)
### Cloud Platforms

[Platforms Documentation](https://docs.chainlit.io/deploy/platforms)

##Async/Sync

[Async/Sync Documentation](https://docs.chainlit.io/guides/sync-async)

## Examples and Resources

- [Chainlit GitHub Repository](https://github.com/Chainlit/chainlit) - Source code and contributions
- [Chainlit Cookbook](https://github.com/Chainlit/cookbook) - Example projects and recipes
- [API Reference](https://docs.chainlit.io/api-reference) - Complete API documentation

Chainlit provides a complete solution for building conversational AI applications with production-grade features and seamless integration with the Python AI ecosystem.
