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
stand_prompt = PromptTemplate(
    input_variables = ["question"],
    template="简明的来回答：{question}"
)
# cto
cto_prompt = PromptTemplate(
    input_variables = ["question"],
    template="通过一步一步的思考来回答这个问题：{question}"
)
#创建一个链
standard_chain = stand_prompt| llm
cot_chain = cto_prompt | llm

#问题
question = "如果一个火车在2小时内行驶了120公里那么他的平均速度是多少"

#回答
sd_as = standard_chain.invoke(question).content
cot_as = cot_chain.invoke(question).content

#回答
print("标准提问")
print(sd_as)
print("cto提问")
print(cot_as)