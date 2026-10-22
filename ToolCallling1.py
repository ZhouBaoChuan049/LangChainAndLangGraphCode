from langchain.tools import tool
@tool
def Add(a:int,b:int)->int:
    """Tool For Add Two Ints
    Args:
        a: The First Int
        b: The Second Int
    Returns:
        The Answer of a Add b 
    """
    return a + b

print(Add.invoke({"a":1,"b":2}))
print(Add.args)
print(Add.name)
print(Add.description)