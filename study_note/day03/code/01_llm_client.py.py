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

def get_completion(prompt,model="gemma3:4b",temperature=0):
    ''' 我们从ollama得到一个补全的结果
    Args:
     propmt(str):把提示词放到api中
     model(str):使用什么模型进行补全
     temperature(int):温度参数，控制生成文本的随机程度，值越高生成的文本越随机，值越低生成的文本越确定。
    Returns:
        str:返回大模型补全的结果的结果 
    '''
    message = [{"role": "user", "content": prompt}]
    response = ChatOllama(model=model,temperature=temperature,base_url="http://127.0.0.1:11434").invoke(message)
    return response.content

get_completion("我们开始沟通吧！")