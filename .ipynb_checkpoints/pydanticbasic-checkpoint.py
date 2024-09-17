from pydantic import BaseModel

# Define a data model using Pydantic
class User(BaseModel):
    name: str
    age: int
    email: str

# Example data
data = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

# Create a user object from the data
user = User(**data)

print(user)
