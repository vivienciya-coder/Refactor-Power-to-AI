# 导入必要的库 介入 ollama
# os py  Python 访问操作系统功能的标准库。 可以读取文件 读取环境变量 指挥外勤。管文件、管路径、管系统变量。：
# sys：指挥内勤。管 Python 运行环境、管程序启动参数、管模块搜索路径。
# dotenv 读取环境变量
import os
#是一个标准的网络协议环境变量。它告诉所有的网络库（如 requests, urllib 等）：“遇到以下地址时，绝对不要走任何代理服务器（VPN），直接去连接目标地址。”
#由于本地开了vpn 需要强制这个地址不走vpn 遇到这个地址就直接连接
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'
import sys
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#load_dotenv()：负责“写入”（从硬盘 -> 系统内存）。
# os.getenv()：负责“读取”（从系统内存 -> 代码变量）。
load_dotenv()
print(os.getenv('MY_NAME'))
# 1. 适配 Ollama 的核心导入
from langchain_ollama import ChatOllama 
# 初始化本地模型
# 初始化你本地的 Google Gemma 3 模型
# 必须和 ollama list 里的名字完全一致
# 学习阶段建议设为 0，让 AI 说话更稳，不乱发挥
llm = ChatOllama(
    model="gemma3:4b",  
    base_url="http://127.0.0.1:11434",
    temperature=0        
)
# 验证连接是否成功的代码块
# inputwords = "你好请介绍一下自己"
# inputwords = "请用一句话来解释一下提示工程的核心概念"  这是最基本的提问 得到的回答是：提示工程的核心概念是**通过精心设计和优化输入提示，引导大型语言模型生成更准确、更有用的输出**。
# 这是直接提问 得到的是一个最普通的回答
# 接下来我们用结构化的方法来对这个提示词进行优化
structured_prompt = PromptTemplate(
    input_variables=["topic"],
    template="为{topic}做出一个合理的解释 解释他的重要性并且列举出他的3个优势"
)
# chain = structured_prompt|llm
#input_variables = {"topic":'前端单元测试'}
input_variables = {"topic":'提示工程'}
#针对同一个主题，不同的提示词是如何导出截然不同的输出结果的
prompts=[
    "列出 3 个 AI 在医疗领域的应用","解释 AI 如何正在变革医疗行业，并给出 3 个具体的例子。","你是一名医生。请描述 AI 在医院中改善你日常工作的 3 种方式。"
]
# try:    
#     for i,prompt in enumerate(prompts,1):
#         print("--- 正在呼叫本地 Gemma 3 模型 ---")
#         #response = llm.invoke(inputwords)
#         print(f"\nPrompt {i}:")
#         print(prompt)
#         print("\nResponse:")
#         #response = chain.invoke(input_variables)
#         response = chain.invoke(prompt)
#         print(f"AI 的回答是：\n{response.content}")
# except Exception as e:
#     print(f"连接失败！错误详情: {e}")

#接下来的代码来演示如何保证ai输出的正确性
# try: 
#     fact_check_prompt = PromptTemplate(
#     input_variables=["statement"],
#     template="""请评估以下陈述的事实准确性。如果内容错误，请提供正确的信息请用中文回答：
#     Statement:{statement}
#     Evaluation:"""
# )
#     chain = fact_check_prompt|llm
#     response = chain.invoke("北京是伦敦的首都")
#     print(f"AI 的回答是：\n{response.content}")
# except Exception as e:
#     print(f"连接失败！错误详情: {e}")
# 接下来的代码演示如何提升解决复杂问题的能力
try:
    sloving_problem_prompt = PromptTemplate(
        input_variables=["problem"],
        template="""一步一步详细的来解决问题:
        Problem:{problem}
        solution:
        """
    )
    chain = sloving_problem_prompt|llm
    response = chain.invoke("计算 1000 美元以 5% 的年利率投资 5 年的复利（按年计息）。")
    print(f"AI 的回答是：\n{response.content}")
except Exception as e:
    print(f"连接失败！错误详情: {e}")
