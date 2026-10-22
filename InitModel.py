from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.messages import SystemMessage

# 第一种定义聊天模型的方式:
# DeepseekModel = init_chat_model(
#     model="deepseek-chat", 
#     model_provider="deepseek",
#     temperature=1
#     );
# print(f"Deepseek Say:{DeepseekModel.invoke("Who You Are?").content}")

# 第二种定义聊天模型的方式:
# ConfigModel = init_chat_model(temperature=1)

# message=[
#     SystemMessage(content="请为我根据以下开头，补写一段故事，一百字左右"),
#     HumanMessage(content="一只猫正在____?")
# ]

# response = ConfigModel.invoke(
#     input=message,
#     config={"configurable": {"model": "deepseek-chat"}}
# )
# print(f"This Model Say:{response.content}")

# 第三种定义聊天模型的方式:
model = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    temperature=2,
    max_tokens=1024,
    configurable_fields={"max_tokens","temperature"},
    config_prefix="First",
)
message=[
    SystemMessage(content="Hello Please Fullfill This Story!"),
    HumanMessage(content="A Cat is laying in the sky ______do what?")
]
result = model.invoke(
    input = message,
    config={
        "configurable":{
            "First_max_tokens":1000,
            "First_temperature":1,
        }
    }
)
print(result.content)