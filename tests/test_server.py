"""Test cases for server module."""

from constants import EMPTY_QUERY_RESPONSE
from server import get_ccri_relevant_information


class TestServer:
    """Test cases for server module."""

    def test_get_ccri_relevant_information_success(self) -> None:
        """Test successful retrieval of CCRI relevant information."""
        example_query = "What is the CCRI?"
        result = get_ccri_relevant_information(example_query)
        assert result is not None
        assert isinstance(result, dict)
        assert "data" in result
        assert "input_arguments" in result
        assert result["input_arguments"]["query"] == example_query
        assert isinstance(result["data"], str)
        assert len(result["data"]) > 0

    def test_get_ccri_relevant_information_empty_query(self) -> None:
        """Test handling of empty query."""
        empty_query = ""
        result = get_ccri_relevant_information(empty_query)

        assert result == {"data": EMPTY_QUERY_RESPONSE, "input_arguments": {"query": empty_query}}
