"""Test cases for handlers module."""

from constants import EMPTY_QUERY_RESPONSE
from handlers import get_ccri_metadata


class TestHandlers:
    """Test cases for handlers module."""

    def test_get_ccri_metadata_success(self) -> None:
        """Test successful retrieval of CCRI metadata."""
        example_query = "What is the CCRI?"
        result = get_ccri_metadata(example_query)
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_ccri_metadata_empty_query(self) -> None:
        """Test handling of empty query."""
        empty_query = ""
        result = get_ccri_metadata(empty_query)
        assert result is not None
        assert isinstance(result, str)
        assert result == EMPTY_QUERY_RESPONSE
