# Tests Documentation

## Overview

The UNICEF RAG MCP project contains unit tests to ensure the reliability of the Retrieval-Augmented Generation (RAG) system for querying the Global Child Hazard Database - Technical Documentation and metadata.

## Test Structure

### Test Files

- **`test_handlers.py`** - Tests metadata retrieval and query handling for the Global Child Hazard Database
- **`test_server.py`** - Tests MCP server functionality
- **`test_logging.py`** - Tests logging configuration and setup

### Test Categories

#### Unit Tests

- **Handler Tests**: Global Child Hazard Database metadata querying, response formatting
- **Server Tests**: MCP server function testing
- **Query Processing**: Text search and retrieval functionality

#### Integration Tests

- **RAG Pipeline**: End-to-end document retrieval and response generation
- **LlamaIndex Integration**: Testing document indexing and search capabilities

## Key Test Coverage

### Core Functionality

- ✅ `get_ccri_metadata()` - Retrieves CCRI metadata based on queries
- ✅ Query validation and processing
- ✅ Empty query handling with appropriate responses
- ✅ Response formatting and validation
- ✅ Logging configuration and setup
- ✅ MCP server function operations

### Query Handling

- **Valid Queries**: Tests with meaningful questions like "What is the Global Child Hazard Database?"
- **Empty Queries**: Handles empty/null queries with predefined responses
- **Response Validation**: Ensures responses are strings with content
- **Error Handling**: Graceful handling of query processing errors

## Running Tests

### Prerequisites

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate

# Ensure Global Child Hazard Database documentation is available
# The system should have access to Global_Child_Hazard_Database_2025_Technical_Documentation.md
```

### Run All Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=rag --cov-report=html

# Run specific test file
uv run pytest tests/test_handlers.py

# Run specific test class
uv run pytest tests/test_handlers.py::TestHandlers

# Run with verbose output
uv run pytest -v
```

## Test Configuration

Tests are configured via `pyproject.toml`:

- Test path: `tests/`
- Python path includes: `[".", "rag"]`
- Coverage excludes test files and `__init__.py`

## Notes

- Tests validate RAG system responses without requiring external API calls
- Document indexing may be required before running certain tests
- Empty query handling ensures system robustness
- Response validation ensures meaningful output for all valid queries
- Integration with LlamaIndex provides robust document retrieval capabilities
