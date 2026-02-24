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
logical_reasoning_prompt = PromptTemplate(
    input_variables=["scenario"],
    template="""请透彻分析以下逻辑谜题。在分析过程中，请严格遵循以下步骤：

1. 列出事实 (List the Facts)：
- 清晰、准确地总结所有给定的信息和陈述。
- 识别所有涉及的人物、角色或关键要素。

2. 确定潜在角色或状态 (Identify Possible Roles or Conditions)：
- 确定适用于这些人物或要素的所有可能身份、行为模式或状态（例如：真话者、谎言者、交替者等）。

3. 标注约束条件 (Note the Constraints)：
- 概述谜题中明确指定的所有规则、限制条件或逻辑关系。

4. 生成所有可能的场景 (Generate Possible Scenarios)：
- 系统地考虑人物或要素之间所有可能的角色/状态组合。
- 确保涵盖了所有的排列组合 (Permutations)，不遗漏任何可能性。

5. 测试每个场景 (Test Each Scenario)：
- 针对每一个可能的场景：
    - 假定你分配的角色或状态成立。
    - 基于这些假设，逐一分析每条陈述的真伪。
    - 检查该场景内部是否存在逻辑冲突或自相矛盾之处。

6. 排除不一致的场景 (Eliminate Inconsistent Scenarios)：
- 剔除任何导致矛盾或违反既定约束条件的场景。
- 记录排除每个场景的具体推理依据和理由。

7. 归纳结论 (Conclude the Solution)：
- 识别经过测试后依然保持逻辑一致的最终场景。
- 简要总结你的发现。

8. 提供明确答案 (Provide a Clear Answer)：
- 明确陈述每个角色或要素的最终状态/身份。
- 基于上述深度分析，解释为什么这是唯一可能的解决方案。

场景内容 (Scenario)：
{scenario}

深度分析 (Analysis)："""
)

logical_chain = logical_reasoning_prompt | llm

logical_puzzle = """房间里有三个人：艾米 (Amy)、鲍勃 (Bob) 和查理 (Charlie)。
他们当中有一个人永远说真话，一个人永远说谎，还有一个人会在真话和谎话之间交替（即第一句真、第二句假，或反之）。

艾米说：“鲍勃是个说谎者。”
鲍勃说：“查理是个真假交替者。”
查理说：“艾米和我都是说谎者。”

请判定每个人的身份（真话者、说谎者或真假交替者）。"""

#回答
logical_as = logical_chain.invoke(logical_puzzle).content

#回答
print("逻辑推理提问")
print(logical_as)