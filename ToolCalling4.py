from langchain_core.tools import StructuredTool
from pydantic import Field , BaseModel

class AddInput(BaseModel):
    a:int = Field(description="第一个整数")
    b:int = Field(description="第二个整数")

def add(a:int,b:int)->int:
    return a+b

addtools = StructuredTool.from_function(
    func=add,
    name="ADD",
    description="数值相加",
    args_schema=AddInput
)

print(addtools.invoke({"a":10,"b":20}))
print(addtools.name)
print(addtools.description)
print(addtools.args)