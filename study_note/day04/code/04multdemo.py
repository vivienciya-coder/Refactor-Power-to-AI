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


multi_step_prompt = """请分析以下文本的核心论点、支持论据以及潜在的反向观点。
请按照以下步骤提供你的分析结果：

1. 核心论点：识别并陈述文本的主要主张或核心论题。
2. 支持论据：列出用于支持该核心论点的主干要点或证据。
3. 潜在反向观点：针对该核心论点，提出可能的反对意见或替代视角。

待分析文本: {text}

分析报告："""
multi_step_prompt_chain = creat_chain(multi_step_prompt)
text = """虽然电动汽车常被视为应对气候变化的解决方案，但其对环境的影响并不像表面上看起来那样简单。 
电动汽车电池的生产需要大量的采矿作业，这可能导致生境破坏和水污染。此外，如果用于为这些车辆充电的电力来自化石燃料，其整体碳足迹可能不会显著减少。 
然而，随着可再生能源变得更加普及以及电池技术的提高，电动汽车确实可以在对抗气候变化中发挥至关重要的作用。"""
res = multi_step_prompt_chain.invoke({"text":text}).content
print(res)