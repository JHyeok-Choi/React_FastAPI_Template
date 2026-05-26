from fastapi import FastAPI, HTTPException

from app.db.schemas import (
    CustomerCreate,
    CustomerUpdate
)

from app.db.crudTest import (
    create_customer,
    get_customers,
    get_customer,
    update_customer,
    delete_customer
)

app = FastAPI()


# CREATE
@app.post("/customers")
def create(customer: CustomerCreate):

    existing = get_customer(customer.customer_id)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Customer already exists"
        )

    return create_customer(customer.dict())


# READ ALL
@app.get("/customers")
def read_all():

    return get_customers()


# READ ONE
@app.get("/customers/{customer_id}")
def read_one(customer_id: int):

    customer = get_customer(customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


# UPDATE
@app.put("/customers/{customer_id}")
def update_one(
    customer_id: int,
    customer: CustomerUpdate
):

    existing = get_customer(customer_id)

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return update_customer(
        customer_id,
        customer.customer_name
    )

 
# DELETE
@app.delete("/customers/{customer_id}")
def delete_one(customer_id: int):

    existing = get_customer(customer_id)

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return delete_customer(customer_id)