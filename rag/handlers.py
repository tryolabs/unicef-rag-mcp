from config import config
from constants import (
    CCRI_METADATA_PERSIST_DIR,
    EMPTY_QUERY_RESPONSE,
)
from llama_index.core import (
    Settings,
    StorageContext,
    load_index_from_storage,  # type: ignore[misc]
)
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.embeddings.bedrock import BedrockEmbedding
from logging_config import get_logger

logger = get_logger(__name__)


def get_ccri_metadata(query: str) -> str:
    """Get the relevant information from the Technical Documentation.

    The function searches the Global Child Hazard Database - Technical Documentation
    for a given query, returning the most relevant chunks.

    The documentation contains detailed information about the Global Child Hazard Database,
    data sources, and technical specifications for the Global Child Hazard Database.

    Args:
        query (str): The query to search the Global Child Hazard Database - Technical Documentation.

    Returns:
        str: A string containing the most relevant chunks from
          the Global Child Hazard Database - Technical Documentation and the input arguments.
    """
    if query.strip() == "":
        logger.warning("Empty query received. Returning empty response.")
        return EMPTY_QUERY_RESPONSE

    config_bedrock_embeddings = BedrockEmbedding(
        model_name=config.embeddings.model_id,
        region_name=config.embeddings.region_name,
    )

    Settings.embed_model = config_bedrock_embeddings

    vector_index = load_index_from_storage(  # type: ignore[misc]
        StorageContext.from_defaults(persist_dir=CCRI_METADATA_PERSIST_DIR)
    )

    retriever = VectorIndexRetriever(
        index=vector_index,  # type: ignore[arg-type]
        similarity_top_k=5,
    )

    response = retriever.retrieve(query)
    return "\n".join([r.text for r in response])
