from pathlib import Path

from config import config
from constants import (
    CCRI_METADATA_FILENAME,
    CCRI_METADATA_PERSIST_DIR,
)
from dotenv import load_dotenv
from llama_index.core import (
    Document,
    Settings,
    VectorStoreIndex,
)
from llama_index.embeddings.bedrock import BedrockEmbedding
from logging_config import get_logger

logger = get_logger(__name__)


def process_ccri_doc() -> None:
    with Path(CCRI_METADATA_FILENAME).open("r") as f:
        text = f.read()

    documents = [Document(text=text)]

    config_bedrock_embeddings = BedrockEmbedding(
        model_name=config.embeddings.model_id,
        region_name=config.embeddings.region_name,
    )
    Settings.embed_model = config_bedrock_embeddings

    vector_index = VectorStoreIndex.from_documents(documents)
    query_engine = vector_index.as_query_engine()  # type: ignore[misc]

    response = query_engine.query("What is the CCRI?")

    vector_index.storage_context.persist(CCRI_METADATA_PERSIST_DIR)  # type: ignore[misc]

    logger.info(response)


if __name__ == "__main__":
    load_dotenv(override=True)

    process_ccri_doc()
