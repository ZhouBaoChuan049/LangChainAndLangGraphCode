from langchain_core.messages import HumanMessage , SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
import os
model = ChatOpenAI( 
    model="deepseek-chat",
    api_key= os.environ["deepseek_apikey"],
    base_url="https://api.deepseek.com",
    temperature=1,
    max_completion_tokens=100,
)
messages = [
    SystemMessage(content="请你为我讲一段故事,基于以下Title做补充,长度100字"),
    HumanMessage(content="一只猫在追逐_______?")
]
parser = StrOutputParser()#输出解析器

#chain = model | parser # model 的输入作为输出解析器的输入
#chain = model.pipe(parser)
chain = RunnableSequence(model,parser)
print(chain.invoke(messages))