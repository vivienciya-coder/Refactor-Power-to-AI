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
def creat_chain(prompt_template):
    """
    创建一个入参为prompt_template的链式调用函数
    Args:
        prompt_template(str):提示词模板的字符串
    Returns:
        ChatOllama:返回一个带有prompt_template的语言模型的链式调用函数
    """
    prompt = PromptTemplate.from_template(prompt_template)
    return prompt  | llm