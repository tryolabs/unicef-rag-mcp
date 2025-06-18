from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import (
    Document,
    VectorStoreIndex,
)

from rag.constants import (
    CCRI_METADATA_FILENAME,
    CCRI_METADATA_PERSIST_DIR,
)
from rag.logging_config import get_logger

logger = get_logger(__name__)


def process_ccri_doc() -> None:
    with Path(CCRI_METADATA_FILENAME).open("r") as f:
        text = f.read()

    documents = [Document(text=text)]

    vector_index = VectorStoreIndex.from_documents(documents)
    query_engine = vector_index.as_query_engine()  # type: ignore[misc]

    response = query_engine.query("What is the CCRI?")

    vector_index.storage_context.persist(CCRI_METADATA_PERSIST_DIR)  # type: ignore[misc]

    logger.info(response)


if __name__ == "__main__":
    load_dotenv(override=True)

    process_ccri_doc()
