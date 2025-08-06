from dataclasses import dataclass
from typing import Literal

Transport = Literal["stdio", "sse", "streamable-http"]


@dataclass
class ServerConfig:
    """Server configuration settings."""

    host: str
    port: int
    transport: Transport


@dataclass
class EmbeddingsConfig:
    """Model configuration settings."""

    model_id: str
    region_name: str


@dataclass
class Config:
    """Configuration settings."""

    server: ServerConfig
    embeddings: EmbeddingsConfig
