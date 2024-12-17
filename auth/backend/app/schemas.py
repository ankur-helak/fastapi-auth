from pydantic import BaseModel

# Define Pydantic models for request and response validation

class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class OrderSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int