from sqlalchemy import select, insert, update, delete
from app.db.database import engine
from app.db.models import customers


# CREATE
def create_customer(customer_data: dict):

    query = insert(customers).values(
        customer_id=customer_data["customer_id"],
        customer_name=customer_data["customer_name"]
    )

    with engine.begin() as conn:
        conn.execute(query)

    return customer_data


# READ ALL
def get_customers():

    query = select(customers)
    
    with engine.connect() as conn:
        result = conn.execute(query)
        rows = result.mappings().all()

    return rows


# READ ONE
def get_customer(customer_id: int):

    query = (
        select(customers)
        .where(customers.c.customer_id == customer_id)
    )

    with engine.connect() as conn:
        result = conn.execute(query)
        row = result.mappings().first()

    return row


# UPDATE
def update_customer(customer_id: int, customer_name: str):

    query = (
        update(customers)
        .where(customers.c.customer_id == customer_id)
        .values(customer_name=customer_name)
    )

    with engine.begin() as conn:
        conn.execute(query)

    return {
        "customer_id": customer_id,
        "customer_name": customer_name
    }

 
# DELETE
def delete_customer(customer_id: int):

    query = (
        delete(customers)
        .where(customers.c.customer_id == customer_id)
    )

    with engine.begin() as conn:
        conn.execute(query)

    return {"message": "deleted"}