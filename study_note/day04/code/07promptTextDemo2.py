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
self_prompt_template2 = {
    "handle": "输入内容：{task}",
    "handle_step": """
你是一个专业的客服人员。请按照以下步骤处理：
1. 分析用户输入：{task}
2. 分类规则如下：
- 物流查询：询问快递进度、修改地址。
- 售后退换：物品损坏、申请退货、漏发。
- 商品咨询：询问尺码、规格、库存。
- 人工申诉：投诉客服、语气恶劣、威胁投诉。
- 其他：不属于上述任何类别。

你只需要输出类别名称不需要回答其他。"""
}
self_prompt_template3 = {
    "handle": "输入内容：{task}",
    "handle_step": """
你是一个专业的电商退换货客服。请按照以下步骤处理：
1. 分析用户输入：{task}
2. 提取信息：
   - 提取订单号。如果用户没有提供，请在此项填写“未提供”。
   - 总结退换货的原因（不超过20字）。
请按以下格式严格输出：
订单号：
原因
"""
}
self_prompt_template = {
    "handle": "输入内容：{task}",
    "handle_step": """
你是一个专业，有职业素养的电商客服。收到用户的输入你需要进行一下处理
1. 分析用户输入：{task}
2. 提取信息：
   - 提取订单号。如果用户没有提供，请在此项填写“未提供”。
   - 总结退换货原因
   - 给用户生成一个回复。回复需要根据根据用户的输入来判断他的情绪根据情绪以及要处理的问题来回复 回复要简单明了专业并能安抚用户
请按以下格式严格输出：
订单号：
原因：请用简短的语言来概括用户退换货的原因
专业的回复 : 

"""
}

task1 = "我想咨询一下我们这个鞋有货么"
task2="我要退货"
task3 = "这已经是我第三次收到破损的杯子了！单号 SN9901，你们到底想不想做生意了？立刻退钱，否则我去投诉！"
task="怎么退货啊？你们的东西质量太差了！"
print(f"任务名称: {task3}\n")
for name,template in self_prompt_template.items():
    chain = creat_chain(template)
    res = chain.invoke({"task":task3}).content
    print(f"{name} Prompt Result:")
    print(res)