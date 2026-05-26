from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String

metadata = MetaData()

customers = Table(
    "customers",
    metadata,

    Column("customer_id", Integer, primary_key=True),
    Column("customer_name", String(50), nullable=False)
)