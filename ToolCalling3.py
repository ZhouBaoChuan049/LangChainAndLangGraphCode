from langchain.tools import tool
from typing_extensions import Annotated

@tool
def Add(
    a:Annotated[int,...,"The First Int"],
    b:Annotated[int,...,"The Second Int"]
)->int:
    """Tool For Add Two Ints
    Args:
        a: The First Int
        b: The Second Int
    Returns:
        The Answer of a Add b 
    """
    return a+b

print(Add.invoke({"a":1,"b":2}))
print(Add.args)
print(Add.name)
print(Add.description)