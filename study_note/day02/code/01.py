import os
import sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# 1. 解决 VPN 导致本地连接 502 的问题
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'

def init_llm():
    load_dotenv()
    # 确认运行环境
    print(f"--- 运行环境: {sys.executable} ---")
    return ChatOllama(
        model="gemma3:4b",
        temperature=0,
        base_url="http://127.0.0.1:11434"
    )

def run_task():
    llm = init_llm()
    
    # 2. 定义提示词模板
    template = """
    你是一个专业的助手。
    任务：{topic}
    """
    prompt_template = PromptTemplate.from_template(template)
    
    # 3. 组合链并运行
    chain = prompt_template | llm
    
    try:
        response = chain.invoke({"topic": "请在此输入测试主题"})
        print(f"\nAI 回复:\n{response.content}")
    except Exception as e:
        print(f"❌ 出错: {e}")

if __name__ == "__main__":
    run_task()