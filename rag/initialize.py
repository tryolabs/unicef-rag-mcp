import os
from pathlib import Path

from dotenv import load_dotenv
from logging_config import get_logger

logger = get_logger(__name__)


def initialize_app() -> None:
    """Initialize the app."""
    logger.info("Initializing app")
    load_dotenv(override=True)
    set_env_vars()


def _read_secret_or_env(secret_name: str, env_var_name: str) -> str:
    """Read from Docker secret file first, then fallback to environment variable.

    Args:
        secret_name: Name of the Docker secret file (without path)
        env_var_name: Name of the environment variable

    Returns:
        str: The secret value

    Raises:
        ValueError: If neither secret file nor environment variable is available
    """
    secret_path = Path(f"/run/secrets/{secret_name}")

    # First try Docker secrets
    if secret_path.exists():
        logger.debug("Reading %s from Docker secret", secret_name)
        return secret_path.read_text().strip()

    # Fallback to environment variable
    env_value = os.environ.get(env_var_name)
    if env_value:
        logger.debug("Reading %s from environment variable", env_var_name)
        return env_value.strip()

    msg = "Neither Docker secret '%s' nor environment variable '%s' is available"
    logger.error(msg, secret_name, env_var_name)
    raise ValueError(msg % (secret_name, env_var_name))


def set_env_vars() -> None:
    """Set the environment variables.

    This function works in both Docker (using secrets) and local environments (using env vars).

    Raises:
        ValueError: If the environment variables are not set.
    """
    try:
        # Set AWS credentials and configuration
        os.environ["AWS_BEARER_TOKEN_BEDROCK"] = _read_secret_or_env(
            "aws_bearer_token_bedrock", "AWS_BEARER_TOKEN_BEDROCK"
        )

        logger.info("Successfully set all environment variables")

    except ValueError as e:
        msg = "Failed to set environment variables: %s"
        logger.exception(msg)
        raise ValueError(msg) from e
