from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from rag.handlers import get_ccri_metadata
from rag.logging_config import get_logger

load_dotenv(override=True)

mcp = FastMCP("RAG MCP")


logger = get_logger(__name__)


@mcp.tool(name="get_ccri_relevant_information")
def get_ccri_relevant_information(query: str) -> str:
    """Get the relevant information from the CCRI technical documentation for a given query.

    The documentation contains detailed information about the CCRI methodology,
    data sources, and technical specifications for the Climate Change Risk Index.

    Args:
        query: The query to search the CCRI technical documentation.

    Returns:
        The most relevant chunks from the CCRI technical documentation as a string.
    """
    data = get_ccri_metadata(query)

    return data
