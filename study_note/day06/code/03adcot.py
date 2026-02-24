import os
import sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
#占位符
from langchain_core.prompts import PromptTemplate,MessagesPlaceholder 
# 输出解释器 将复杂对话结果转为蚊子
from langchain_core.output_parsers import StrOutputParser

# 1. 解决 VPN 导致本地连接 502 的问题
os.environ['NO_PROXY'] = 'localhost,127.0.0.1' 
#初始化语言大模型
llm = ChatOllama(model="gemma3:4b",temperature=0,base_url="http://localhost:11434")
# 标准提示词应用
adcto_prompt = PromptTemplate(
    input_variables = ["question"],
    template="""按照以下步骤来一步一步的回答
        1. 陈述你准备计算的内容
        2. 写出你用的公式 如何通用的话
        3. 进行计算
        4. 解释结果
        问题 ：{question}
        结果：
        """
)
adcto_chain = adcto_prompt | llm
#问题
question = "一个在以60公里每小时的速度行驶了150公里 另外一辆以50公里每小时行驶了100公里 这个旅程的平均车速是多少"
#回到
adcto_as  = adcto_chain.invoke(question).content
print("adcto提问")
print(adcto_as) 
