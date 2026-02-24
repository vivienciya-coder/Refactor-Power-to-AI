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

dcto_prompt = PromptTemplate(
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
standard_chain = stand_prompt| llm
dcto_chain = dcto_prompt | llm

chall_quesiton = """一个半径 1.5 米、高 4 米的圆柱形水箱目前已装满 2/3。如果以每分钟 10 升的速度加水，水箱溢出需要多长时间？请以小时和分钟为单位给出答案，并四舍五入到最近的分钟。（使用 
，
 升 = 
 立方米）
"""
#回答
sd_as = standard_chain.invoke(chall_quesiton).content
cot_as = dcto_chain.invoke(chall_quesiton).content

#回答
print("标准提问")
print(sd_as)
print("cto提问")
print(cot_as)