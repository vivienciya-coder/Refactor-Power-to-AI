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
# 更高阶的少样本使用
# 多任务去执行情感分析和语言检测
# 多任务学习的定义和优点
# 定义 让模型去执行一个多个相关的任务
# 优点： 更高效 更泛化 后面看不懂了
# 具体实现
# 设计一个提示词模板 多任务并包含少样本
# 使用特定任务的指令，目的是为了引导/规范模型的输出行为。
# 根据输入内容的不同，来决定切换到哪个任务。


#定义多任务少样本的类 
def multi_task_few_shot(input_text,task):
    few_shot_template =PromptTemplate(
    input_vairiables =["input_text","task"],
    template = """
    为给出的内容做执行特定的任务
    例子：
    Text：现在温度35度
    Task：情感分析
    Result：中立

    Text：Bonjour, comment allez-vous?
    Task：语言检测
    Result：法语

    现在请执行下面的任务
    Text：{input_text}
    Task：{task}
    Result:""")
    chain =few_shot_template| llm
    return chain.invoke({"input_text":input_text,"task":task}).content

#测试
print(multi_task_few_shot("这个建筑太伟大了我真的那难以置信","情感分析"))

print(multi_task_few_shot("Guten Tag, wie geht es Ihnen?","语言检测"))