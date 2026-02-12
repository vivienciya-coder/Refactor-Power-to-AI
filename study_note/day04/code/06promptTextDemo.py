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
# chian = PromptTemplate.from_template("请分析以下文本的情感倾向：{text}") | llm
def creat_chain(propmt_template):
    """创建一个最简单的提示词与llm交互的函数
    Args:
        propmt_template(str):提示词模板
    Returns:返回一个ChatOllama
    """
    prompt = PromptTemplate.from_template(propmt_template)
    return prompt | llm
# 定义模板
self_prompt_template = {
    "handle": """你需要将用户的{task}分解为“主体”和“意图”，以便准确判断用户输入的实际语言。
注意：用户使用的语言类型可能多种多样，包括英语、中文、西班牙语、阿拉伯语、日语、法语等。
请务必确保你的输出语言与用户输入的语言保持一致！
你的输出仅限于：(输入语言) 意图 + 主体（尽可能简短）
你的输出必须是一个有效的 JSON。

提示：当用户的问题是针对你（语言模型）时，可以添加一个表情符号让对话更有趣。

示例 1：
用户输入：hi, yesterday i had some burgers.
{{
  "Language Type": "用户的输入是纯英文",
  "Your Reasoning": "我输出的语言必须是纯英文。",
  "Your Output": "sharing yesterday's food"
}}

示例 2：
用户输入：hello
{{
  "Language Type": "用户的输入是纯英文",
  "Your Reasoning": "我输出的语言必须是纯英文。",
  "Your Output": "Greeting myself☺️"
}}

示例 3：
用户输入：why mmap file: oom
{{
  "Language Type": "用户的输入是纯英文",
  "Your Reasoning": "我输出的语言必须是纯英文。",
  "Your Output": "Asking about the reason for mmap file: oom"
}}

示例 4：
用户输入：www.convinceme.yesterday-you-ate-seafood.tv讲了什么？
{{
  "Language Type": "用户的输入是中英混合",
  "Your Reasoning": "英文部分是一个URL，主要意图仍是用中文书写的，因此我输出的语言必须使用中文。",
  "Your Output": "询问网站www.convinceme.yesterday-you-ate-seafood.tv"
}}

示例 5：
用户输入：why小红的年龄is老than小明？
{{
  "Language Type": "用户的输入是中英混合",
  "Your Reasoning": "英文部分是主观助词，主要意图是用中文书写的，且中文占据的“实际含义”大于英文，因此我输出的语言必须使用中文。",
  "Your Output": "询问小红和小明的年龄"
}}

示例 6：
用户输入：yo, 你今天咋样？
{{
  "Language Type": "用户的输入是中英混合",
  "Your Reasoning": "英文部分是主观助词，主要意图是用中文书写的，因此我输出的语言必须使用中文。",
  "Your Output": "查询今日我的状态☺️"
}}现在请处理以下输入：
用户输入：{task}"""
}

task = "I am feeling great today!"
print(f"任务名称: {task}\n")
for name,template in self_prompt_template.items():
    chain = creat_chain(template)
    res = chain.invoke({"task":task}).content
    print(f"{name} Prompt Result:")
    print(res)