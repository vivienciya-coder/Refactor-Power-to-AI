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
def compara_propmts(task,prompt_templates):
    print(f"任务名称: {task}\n")
    for name,template in prompt_templates.items():
        chain = creat_chain(template)
        res = chain.invoke({"task":task}).content
        print(f"{name} Prompt Result:")
        print(res)
        print("\n" + "-"*50 + "\n")
# task = "简明地解释区块链技术的概念"
# prompt_templates = {
# "Basic": "请解释什么是{task}",
# "Structured": """请通过以下几个维度来解释{task}：
# 1. 定义
# 2. 核心特征
# 3. 实际应用场景
# 4. 对相关行业的潜在影响"""
# }
# compara_propmts(task, prompt_templates)
task = "登录页面点按钮没反应，还有能不能加个微信登录的功能？"
prompt_templates = {
"Basic":"请分析用户输入：{task}，并判断这段输入包含哪些“功能开发”或“Bug修复”。",
"Structured":"""你是一个资深产品经理。按照一下结构分析用户输入的{task}：
请严格按以下结构输出：
1. 【需求分类】：判断这段输入包含哪些“功能开发”或“Bug修复”。
2. 【任务拆解】：列举需要解决的具体子问题。
3. 【优先级评估】：请根据紧急程度（高/中/低）排序，并简述理由。"""}
compara_propmts(task, prompt_templates)