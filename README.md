# UNICEF Technical Documentation RAG MCP

This is the project for the MCP server for the UNICEF Technical Documentation RAG.

## Development

### Dependencies

Dependencies are managed with [uv](https://docs.astral.sh/uv/).

To install the dependencies, run:

```bash
uv sync
```

### Processing the CCRI technical documentation

**Before** running the server, you need to process the CCRI technical documentation and persist the vector index.

To do this, run:

```bash
uv run python process_ccri_doc.py
```

### Running the server

To run the server, run:

```bash
mcp dev rag/server.py
```

### Running the tests

To run the tests, run:

```bash
uv run pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
