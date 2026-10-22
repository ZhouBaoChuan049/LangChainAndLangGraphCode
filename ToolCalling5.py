from langchain_core.tools import StructuredTool
from pydantic import Field , BaseModel
from typing import Tuple, List
class AddInput(BaseModel):
    a:int = Field(description="第一个整数")
    b:int = Field(description="第二个整数")

def add(a:int,b:int)->Tuple[str,List[int]]:
    num = [a,b]
    content = f"{num}相加的结果是:{a+b}"
    return content , num

addtools = StructuredTool.from_function(
    func=add,
    name="ADD",
    description="数值相加",
    args_schema=AddInput ,
    response_format="content_and_artifact"
)

print(addtools.invoke(
    {
        "name": "ADD",
        "args": {"a":10, "b":20},
        "type": "tool_call",
        "id": "123"
    }
))
print(addtools.name)
print(addtools.description)
print(addtools.args)