# Qdrant

## What is Qdrant?

Qdrant is an AI-native vector database and semantic search engine designed to store, search, and manage vectors along with their associated payload. It enables developers to extract meaningful information from unstructured data by performing similarity searches at scale with high performance and accuracy.

Qdrant addresses the challenge of building production-grade vector search applications by providing efficient storage, fast similarity search, advanced filtering capabilities, and horizontal scalability. It allows developers to focus on their AI applications rather than building vector database infrastructure from scratch.

**GitHub Repository**: [https://github.com/qdrant/qdrant](https://github.com/qdrant/qdrant)

**Official Documentation**: [https://qdrant.tech/documentation/](https://qdrant.tech/documentation/)

**API Reference**: [https://qdrant.tech/documentation/api-reference](https://qdrant.tech/documentation/api-reference)

## Installation and Setup

### Standard Installation

[Installation Guide](https://qdrant.tech/documentation/guides/installation/)

Qdrant can be installed using Docker:

```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

Install Qdrant Python client:

```bash
pip install qdrant-client
```

### Qdrant Cloud

[Cloud Quickstart](https://qdrant.tech/documentation/cloud-quickstart/)

The quickest way to get started is with Qdrant Cloud's free tier, which provides a managed cluster with a web UI for data interaction and scales easily.

### Local Quickstart

[Local Quickstart](https://qdrant.tech/documentation/local-quickstart/)

Run Qdrant locally for development and testing before deploying to production.

## Core Concepts

### Collections

[Collections Documentation](https://qdrant.tech/documentation/concepts/collections/)

Collections are named sets of points (vectors with payload) that share the same configuration. Each collection has its own settings for vectors, indexing, and optimization.

### Points

[Points Documentation](https://qdrant.tech/documentation/concepts/points/)

Points are the central entity in Qdrant. A point is a record consisting of a vector (or multiple vectors) and an optional payload. Each point has a unique ID within a collection.

### Vectors

[Vectors Documentation](https://qdrant.tech/documentation/concepts/vectors/)

Vectors are high-dimensional representations of data. Qdrant supports multiple vector types including dense vectors, sparse vectors, and multi-vectors per point.

### Payload

[Payload Documentation](https://qdrant.tech/documentation/concepts/payload/)

Payload is additional information stored with each point. It can contain any JSON-compatible data and supports filtering during search operations.

### Search

[Search Documentation](https://qdrant.tech/documentation/concepts/search/)

Qdrant provides various search methods including similarity search, filtered search, and recommendation-based search to retrieve the most relevant vectors.

### Explore

[Explore Documentation](https://qdrant.tech/documentation/concepts/explore/)

Discovery and exploration APIs for finding similar items, grouping results, and understanding the vector space structure.

### Hybrid Queries

[Hybrid Queries Documentation](https://qdrant.tech/documentation/concepts/hybrid-queries/)

Combine multiple search strategies including vector similarity and payload filtering to achieve optimal search results.

### Filtering

[Filtering Documentation](https://qdrant.tech/documentation/concepts/filtering/)

Advanced filtering capabilities allow you to combine vector search with complex payload conditions using logical operators and comparison functions.

### Inference

[Inference Documentation](https://qdrant.tech/documentation/concepts/inference/)

Built-in embedding model inference capabilities for generating vectors directly within Qdrant.

### Optimizer

[Optimizer Documentation](https://qdrant.tech/documentation/concepts/optimizer/)

Automatic background optimization processes that improve search performance and reduce memory usage over time.

### Storage

[Storage Documentation](https://qdrant.tech/documentation/concepts/storage/)

Flexible storage options including in-memory, disk-based, and hybrid storage configurations for different performance requirements.

### Indexing

[Indexing Documentation](https://qdrant.tech/documentation/concepts/indexing/)

Various indexing strategies including HNSW (Hierarchical Navigable Small World) for fast approximate nearest neighbor search.

### Snapshots

[Snapshots Documentation](https://qdrant.tech/documentation/concepts/snapshots/)

Create and restore collection snapshots for backup, migration, and disaster recovery purposes.

## API & SDKs

[API & SDKs Overview](https://qdrant.tech/documentation/api-sdks/)

Qdrant provides a REST API and gRPC interface, with official client libraries available for multiple programming languages:

- **Python**: Full-featured client with async support
- **JavaScript/TypeScript**: Node.js and browser support
- **Rust**: Native Rust SDK
- **Go**: Go client library
- **Java**: Java/Kotlin client
- **.NET**: C# client library

## Guides

### Administration

[Administration Guide](https://qdrant.tech/documentation/guides/administration/)

Manage Qdrant instances, configure authentication, monitor performance, and handle operational tasks.

### Running with GPU

[GPU Guide](https://qdrant.tech/documentation/guides/running-with-gpu/)

Leverage GPU acceleration for improved performance in vector operations and indexing.

### Capacity Planning

[Capacity Planning Guide](https://qdrant.tech/documentation/guides/capacity-planning/)

Plan resource allocation and estimate hardware requirements based on your data size and query patterns.

### Optimize Performance

[Performance Optimization Guide](https://qdrant.tech/documentation/guides/optimize-performance/)

Best practices for optimizing search speed, reducing latency, and improving throughput in production deployments.

### Multitenancy

[Multitenancy Guide](https://qdrant.tech/documentation/guides/multitenancy/)

Build vector search applications that serve multiple users with proper data isolation, security, and performance tuning.

### Distributed Deployment

[Distributed Deployment Guide](https://qdrant.tech/documentation/guides/distributed-deployment/)

Scale Qdrant beyond a single node with distributed clusters for high availability, fault tolerance, and billion-scale performance.

### Quantization

[Quantization Guide](https://qdrant.tech/documentation/guides/quantization/)

Reduce memory usage and improve search performance using vector quantization techniques including scalar, product, and binary quantization.

### Text Search

[Text Search Guide](https://qdrant.tech/documentation/guides/text-search/)

Implement full-text search capabilities in combination with vector search for hybrid retrieval systems.

### Monitoring & Telemetry

[Monitoring Guide](https://qdrant.tech/documentation/guides/monitoring-telemetry/)

Monitor Qdrant performance, track metrics, and integrate with observability tools.

### Configuration

[Configuration Guide](https://qdrant.tech/documentation/guides/configuration/)

Configure Qdrant settings for storage, networking, performance, and resource management.

### Security

[Security Guide](https://qdrant.tech/documentation/guides/security/)

Secure your Qdrant deployment with authentication, API keys, TLS encryption, and network security.

## Ecosystem

### FastEmbed

[FastEmbed Quickstart](https://qdrant.tech/documentation/ecosystem/fastembed-quickstart/)

FastEmbed is a lightweight, fast embedding generation library that integrates seamlessly with Qdrant.

#### FastEmbed & Qdrant Integration

[FastEmbed & Qdrant Guide](https://qdrant.tech/documentation/ecosystem/fastembed-qdrant/)

Generate embeddings and store them in Qdrant with minimal code and optimal performance.

#### Advanced Retrieval Methods

- [Working with miniCOIL](https://qdrant.tech/documentation/ecosystem/working-with-minicoil/)
- [Working with SPLADE](https://qdrant.tech/documentation/ecosystem/working-with-splade/)
- [Working with ColBERT](https://qdrant.tech/documentation/ecosystem/working-with-colbert/)

#### Reranking

[Reranking with FastEmbed](https://qdrant.tech/documentation/ecosystem/reranking-with-fastembed/)

Improve search quality by reranking initial search results using FastEmbed models.

#### Multi-Vector Postprocessing

[Multi-Vector Postprocessing](https://qdrant.tech/documentation/ecosystem/multi-vector-postprocessing/)

### Qdrant MCP Server

[Qdrant MCP Server](https://qdrant.tech/documentation/ecosystem/qdrant-mcp-server/)

Model Context Protocol server for integrating Qdrant with AI applications and frameworks.

## Tutorials

### Vector Search Basics

- [Semantic Search 101](https://qdrant.tech/documentation/tutorials/semantic-search-101/)
- [Build a Neural Search Service](https://qdrant.tech/documentation/tutorials/build-neural-search-service/)
- [Setup Hybrid Search with FastEmbed](https://qdrant.tech/documentation/tutorials/setup-hybrid-search-with-fastembed/)
- [Measure Search Quality](https://qdrant.tech/documentation/tutorials/measure-search-quality/)

### Advanced Retrieval

- [How to Use Multivector Representations with Qdrant Effectively](https://qdrant.tech/documentation/tutorials/how-to-use-multivector-representations-with-qdrant-effectively/)
- [Reranking in Hybrid Search](https://qdrant.tech/documentation/tutorials/reranking-in-hybrid-search/)
- [Search Through Your Codebase](https://qdrant.tech/documentation/tutorials/search-through-your-codebase/)
- [Build a Recommendation System with Collaborative Filtering](https://qdrant.tech/documentation/tutorials/build-a-recommendation-system-with-collaborative-filtering/)
- [Scaling PDF Retrieval with Qdrant](https://qdrant.tech/documentation/tutorials/scaling-pdf-retrieval-with-qdrant/)

### Using the Database

- [Bulk Upload Vectors](https://qdrant.tech/documentation/tutorials/bulk-upload-vectors/)
- [Create & Restore Snapshots](https://qdrant.tech/documentation/tutorials/create-and-restore-snapshots/)
- [Large Scale Search](https://qdrant.tech/documentation/tutorials/large-scale-search/)
- [Load a HuggingFace Dataset](https://qdrant.tech/documentation/tutorials/load-a-huggingface-dataset/)
- [Build With Async API](https://qdrant.tech/documentation/tutorials/build-with-async-api/)
- [Migration to Qdrant](https://qdrant.tech/documentation/tutorials/migration-to-qdrant/)

## Qdrant Web UI

[Web UI Documentation](https://qdrant.tech/documentation/qdrant-web-ui/)

Interactive web interface for exploring collections, searching vectors, viewing payloads, and managing your Qdrant instance.

## FAQ

### Qdrant Fundamentals

[Qdrant Fundamentals FAQ](https://qdrant.tech/documentation/faq/qdrant-fundamentals/)

Common questions about Qdrant's architecture, capabilities, and core concepts.

### Database Optimization

[Database Optimization FAQ](https://qdrant.tech/documentation/faq/database-optimization/)

Frequently asked questions about optimizing Qdrant performance, memory usage, and search quality.

## Release Notes

[Release Notes](https://qdrant.tech/documentation/release-notes/)

Stay updated with the latest features, improvements, and bug fixes in Qdrant releases.

## Examples and Resources

- **Official Documentation**: [https://qdrant.tech/documentation/](https://qdrant.tech/documentation/)
- **GitHub Repository**: [https://github.com/qdrant/qdrant](https://github.com/qdrant/qdrant)
- **API Reference**: [https://qdrant.tech/documentation/api-reference](https://qdrant.tech/documentation/api-reference)
- **Cloud Platform**: [https://cloud.qdrant.io/](https://cloud.qdrant.io/)
- **Blog & Articles**: [https://qdrant.tech/blog/](https://qdrant.tech/blog/)

Qdrant provides a comprehensive solution for building production-grade vector search applications with powerful features for semantic search, recommendation systems, and AI-powered data retrieval at scale.
