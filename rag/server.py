from config import config
from dotenv import load_dotenv
from handlers import get_ccri_metadata
from mcp.server.fastmcp import FastMCP

load_dotenv(override=True)


mcp = FastMCP(
    "RAG MCP",
    host=config.server.host,
    port=config.server.port,
)

from logging_config import get_logger  # noqa: E402

logger = get_logger(__name__)


@mcp.tool(name="get_ccri_relevant_information")
def get_ccri_relevant_information(query: str) -> dict[str, str | dict[str, str]]:
    """Get the relevant information from the Technical Documentation.

    The function searches the Global Child Hazard Database - Technical Documentation
    for a given query, returning the most relevant chunks.

    The documentation contains detailed information about the Global Child Hazard Database,
    data sources, and technical specifications for the Global Child Hazard Database.

    Args:
        query (str): The query to search the Global Child Hazard Database - Technical Documentation.

    Returns:
        dict[str, str | dict[str, str]]: A dictionary containing the most relevant chunks from
          the Global Child Hazard Database - Technical Documentation and the input arguments.
    """
    logger.info("Getting CCRI relevant information for query: %s", query)
    data = get_ccri_metadata(query)
    logger.info("Successfully got CCRI relevant information for query: %s", query)

    return {"data": data, "input_arguments": {"query": query}}


if __name__ == "__main__":
    from initialize import initialize_app

    initialize_app()

    logger.info("🚀 Starting server... ")

    logger.info(
        'Check "http://localhost:%s/%s" for the server status',
        config.server.port,
        config.server.transport,
    )

    mcp.run(config.server.transport)
