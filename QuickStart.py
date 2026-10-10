from langchain_core.messages import HumanMessage , SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os
model = ChatOpenAI( 
    model="deepseek-chat",
    api_key= os.environ["deepseek_apikey"],
    base_url="https://api.deepseek.com"
)
messages = [
    SystemMessage(content="请帮我进行翻译,有英文翻译为中文!"),
    HumanMessage(content="My Name is XiaoMing")
]
parser = StrOutputParser()

chain = model | parser
print(chain.invoke(messages))