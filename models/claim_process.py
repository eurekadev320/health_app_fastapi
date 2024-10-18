from db import metadata
from sqlalchemy import Column, Table, Integer, ForeignKey, String, Float, DateTime

claim_processes = Table(
    "claim_processes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("net_fee", Float(), nullable=True, default=0),
)

claim_process_items = Table(
    "claim_process_items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("claim_process_id", ForeignKey("claim_processes.id", ondelete="CASCADE"), nullable=False),
    Column("service_date", DateTime(), nullable=False),
    Column("submitted_procedure", String(), nullable=False),
    Column("quadrant", String(), nullable=True, default=""),
    Column("plan_group_no", String(), nullable=False),
    Column("subscriber_no", String(), nullable=False),
    Column("provider_npi", String(), nullable=False),
    Column("provider_fee", Float(), nullable=False),
    Column("allowed_fee", Float(), nullable=False),
    Column("member_coinsurance", Float(), nullable=False),
    Column("member_copay", Float(), nullable=False),
)

