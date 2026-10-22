from langchain.tools import tool
from pydantic import BaseModel , Field

class AddServer(BaseModel):
    """两数相加"""
    a:int = Field(...,description="This Is The First Int")
    b:int = Field(...,description="This Is The Second Int")

@tool(args_schema=AddServer)
def add(a:int,b:int)->int:
    return a + b

print(add.invoke({"a":10, "b":20}))
print(add.name)
print(add.description)
print(add.args)
