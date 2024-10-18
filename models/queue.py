from db import metadata
from sqlalchemy import Column, Table, Integer, String, JSON, Boolean

queues = Table(
    "queues",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type", String(), nullable=False),
    Column("payload", JSON(), nullable=False),
    Column("locked", Boolean(), nullable=True, default=False),
)
