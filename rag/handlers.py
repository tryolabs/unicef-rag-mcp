from constants import (
    CCRI_METADATA_PERSIST_DIR,
    EMPTY_QUERY_RESPONSE,
)
from llama_index.core import (
    StorageContext,
    load_index_from_storage,  # type: ignore[misc]
)
from llama_index.core.retrievers import VectorIndexRetriever
from logging_config import get_logger

logger = get_logger(__name__)


def get_ccri_metadata(query: str) -> str:
    """Get the metadata for the CCRI dataset.

    The documentation contains detailed information about the CCRI methodology,
    data sources, and technical specifications for the Climate Change Risk Index.

    This function uses a vector index to search the CCRI technical documentation.
    It returns the most relevant information from the documentation based on the query.

    Args:
        query: The query to search the CCRI technical documentation.

    Returns:
        The most relevant chunks from the CCRI technical documentation as a string.
    """
    if query.strip() == "":
        logger.warning("Empty query received. Returning empty response.")
        return EMPTY_QUERY_RESPONSE

    vector_index = load_index_from_storage(  # type: ignore[misc]
        StorageContext.from_defaults(persist_dir=CCRI_METADATA_PERSIST_DIR)
    )

    retriever = VectorIndexRetriever(
        index=vector_index,  # type: ignore[arg-type]
        similarity_top_k=5,
    )

    response = retriever.retrieve(query)
    return "\n".join([r.text for r in response])
