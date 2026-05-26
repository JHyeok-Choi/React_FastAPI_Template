from pydantic import BaseModel

class CustomerCreate(BaseModel):
    customer_id: int
    customer_name: str


class CustomerUpdate(BaseModel):
    customer_name: str


class CustomerResponse(BaseModel):
    customer_id: int
    customer_name: str