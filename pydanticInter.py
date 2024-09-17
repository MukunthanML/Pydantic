from typing import List, Optional
from pydantic import BaseModel, Field, conlist

# Define the Product model
class Product(BaseModel):
    name: str
    price: float
    currency: str
    tag_line: Optional[str] = None  # Optional field

# Define the Response model
class ProductResponse(BaseModel):
    products: conlist(Product, min_items=0, max_items=100)  # List of products with a max limit of 100

# Example function to validate response
def validate_response(response_data):
    try:
        response = ProductResponse(**response_data)
        return response
    except Exception as e:
        print(f"Validation error: {e}")

# Example response data
response_data = {
    "products": [
        {"name": "Laptop", "price": 999.99, "currency": "USD", "tag_line": "High performance"},
        {"name": "Smartphone", "price": 499.99, "currency": "USD"}
    ]
}

# Validate response
validated_response = validate_response(response_data)
print(validated_response)
