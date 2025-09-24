# UNICEF Technical Documentation RAG MCP Server

The UNICEF Technical Documentation RAG (Retrieval-Augmented Generation) MCP Server provides intelligent access to technical documentation through semantic search capabilities. This Model Context Protocol (MCP) server specializes in processing and retrieving information from the Global Child Hazard Database - Technical Documentation and related climate risk assessment materials.

## Overview

This MCP server serves as the technical documentation backend for the UNICEF Geosphere project, providing access to the Global Child Hazard Database - Technical Documentation.

## Features

### Core Capabilities

- **Document Processing**: Automatic parsing and indexing of technical documentation
- **Vector Search**: Semantic similarity-based document retrieval
- **Context Extraction**: Relevant passages for answering specific questions

### Technical Documentation Coverage

- **Climate Risk Methodologies**: CCRI calculation approaches and algorithms
- **Dataset Specifications**: Detailed descriptions of hazard and exposure datasets
- **Indicator Definitions**: Technical definitions of risk indicators
- **Data Sources**: Source documentation

## Technology Stack

- **FastMCP**: Model Context Protocol server framework
- **Vector Database**: Document embeddings and similarity search
- **LlamaIndex**: Document processing and RAG pipelines
- **Sentence Transformers**: Text embedding generation

## Project Structure

```
rag/
├── server.py              # MCP server and tool definitions
├── handlers.py            # RAG implementation and document processing
├── config.py              # Configuration and settings management
├── schemas.py             # Pydantic models and validation
├── constants.py           # Application constants
├── config.yaml            # Server configuration
├── logging_config.py      # Logging setup
└── data/vector_index/     # Document storage and vector indices
process_ccri_doc.py        # Document processing script
Global_Child_Hazard_Database_2025_Technical_Documentation.md # Global Child Hazard Database - Technical Documentation
```

## Prerequisites

### Document Processing Requirements

- **Source Documents**: Global Child Hazard Database - Technical Documentation (Markdown format)
- **Vector Storage**: Persistent vector database for document embeddings
- **Processing Power**: Sufficient resources for document embedding generation

Note: The technical documentation must be provided as a single Markdown file named
`Global_Child_Hazard_Database_2025_Technical_Documentation.md` at the repository root. If your source document
is a Word or Google Doc, convert it to Markdown using one of the available online tools
like [word2md.com](https://word2md.com/) or a built-in tool like Pandoc. Using
Pandoc, you can convert the document to Markdown using the following command:

```bash
pandoc --from docx --to markdown --extract-media=. <input_file.docx> -o Global_Child_Hazard_Database_2025_Technical_Documentation.md
```

## Available Tools

The MCP server exposes specialized tools for technical documentation access:

### 1. Technical Documentation Search

#### `get_ccri_relevant_information(question: str)`

Performs semantic search against the Global Child Hazard Database - Technical Documentation to find relevant information.

**Parameters**:

- `question` (required): Natural language question about climate risk methodologies, datasets, or technical specifications

**Returns**: Dictionary containing:

- `data`: List of relevant document sections
- `input_arguments`: Input arguments for the tool

## Installation

### Dependencies

```bash
# Install dependencies using uv
uv sync
```

### Document Processing Setup

**Before running the server**, you must process the Global Child Hazard Database - Technical Documentation:

```bash
# Process and index the Global Child Hazard Database documentation
uv run python process_ccri_doc.py
```

This step:

1. Parses the Global Child Hazard Database - Technical Documentation Markdown
2. Splits content into searchable chunks
3. Generates vector embeddings for each chunk
4. Creates a persistent vector index
5. Stores metadata for each document section

## Configuration

### Server Configuration

**`rag/config.yaml`**:

```yaml
server:
  host: "0.0.0.0" # Server bind address
  port: 8002 # Server port
  transport: "sse" # MCP transport protocol
```

## Development

### Running the Server

```bash
# Development mode
mcp dev rag/server.py

# Production mode
uv run rag/server.py
```

### Testing

```bash
# Run all tests
uv run pytest

# Run specific tests
uv run pytest tests/test_handlers.py -v
```

### Development Setup

1. **Clone repository**
2. **Install dependencies**: `uv sync`
3. **Process documentation**: `uv run python process_ccri_doc.py`
4. **Run tests**: `uv run pytest`
5. **Start server**: `mcp dev rag/server.py`

## Contributing

### Development Guidelines

1. **Code Style**: Follow PEP 8 and use type hints
2. **Testing**: Add tests for new RAG functionality
3. **Documentation**: Update tool descriptions and examples

### Adding New Documents

1. **Document Preparation**: Ensure documents are in markdown format
2. **Processing Script**: Update `process_ccri_doc.py` for new documents
3. **Metadata Schema**: Extend metadata structure if needed
4. **Testing**: Verify search functionality with new content
5. **Index Update**: Regenerate vector index with new documents

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Submit issues on GitHub repository
- **RAG Documentation**: [LlamaIndex RAG Guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/)
- **Technical Support**: Repository maintainers
