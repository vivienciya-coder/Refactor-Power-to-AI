import os
import sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
#占位符
from langchain_core.prompts import PromptTemplate,MessagesPlaceholder,ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
# 输出解释器 将复杂对话结果转为文字
from langchain_core.output_parsers import StrOutputParser
# 这个 ChatMessageHistory的作用是用来存储对话历史的 这样就能实现多轮对话了 因为模型每次都能看到之前的对话历史 这样就能知道之前说了什么了 这个是多轮对话的关键 需要自己维护对话历史 让模型知道之前说了什么
from langchain_community.chat_message_histories import ChatMessageHistory

# 1. 解决 VPN 导致本地连接 502 的问题
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'
model = ChatOllama(model="gemma3:4b", temperature=0, base_url="http://127.0.0.1:11434")
# 2. 定义prompt结构
## 待理解 from_messages 这个方法怎么用 这个是关键 我是个小白不太懂
# 就这个定义来看是定义了一个对话的模板 显示由系告诉ai 他是个有用的机器人 然后系统开始做准备来存储接下来的对话 接下来就是定义用户输入了什么
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI bot."), ("human", "{input}"),
    MessagesPlaceholder(variable_name="history"),#记忆插槽
    ("user","{input}")
    ])
## 3. 构建 LCEL 链 设么是LCEL链  这个链把定义的模板 还有模型allama链接起来一起工作 相当于做准备工作 准备好了才可以好好沟通
chain = prompt | model | StrOutputParser() # 这个是输出解释器 让复杂的对话结果变得简单易懂
# 4. 手动维护session状态 这个是多轮对话的关键 需要自己维护对话历史 让模型知道之前说了什么 
# 问题： 那用什么逻辑让模型知道之前说了什么呢 这个就是session_history这个变量的作用了 这个变量就是用来存储对话历史的 然后每次用户输入新的内容的时候 就把新的内容和之前的历史一起传给模型 让模型知道之前说了什么
session_history = {}
#具体保存session的方法 如果对话不存在就写入 存在就删除然后再写入 这样就能保证每次对话都是最新的 之前的历史也不会丢失
def get_session_history(session_id:str):
    if session_id not in session_history:
        session_history[session_id] = ChatMessageHistory()   
    return session_history[session_id]

# 封装带记忆的链 就是把chain 和 session_history 结合起来 让模型每次都能看到之前的对话历史 这样就能实现多轮对话了

## 接下来我们定义一个单轮提示词对话

single_prompts = ["法国的首都是哪儿", "他的人口有多少", "这座城市的地标是什么", "他最出名的歌星是谁"]

#初始化ollma
def init_llm():
    load_dotenv()
    # 确认运行环境
    print(f"--- 运行环境: {sys.executable} ---")
    return model

def run_task():
    llm = init_llm()
 
with_history_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
    )
try:
   print("===============================多轮提示词回答==============================================")
   # 这个的意思是配置一个session_id如果session_history里没有这个session_id就创建一个新的session_id 如果有就用之前的session_id 这样就能保证每次对话都是最新的 之前的历史也不会丢失
   config = {"configurable":{"session_id":"ollama_space_test"}} 
   print("第一轮回复：")
   print(with_history_chain.invoke({"input": "嗨，我正在学习关于太空的知识。你能给我讲讲行星吗？"}, config))

   print("\n第二轮回复：")
   print(with_history_chain.invoke({"input": "太阳系最大的行星是什么"}, config))

   print("\n第三轮回复：")
   print(with_history_chain.invoke({"input": "他和地球相比怎么样？"}, config))
   print("\n第四轮回复：")
   print(with_history_chain.invoke({"input": "那姚明有多高？他和地球比呢"}, config))
   print("===============================单轮提示词回答==============================================")
   print("===============================单轮提示词回答==============================================")
   # 1. 在循环外部定义好“组件” (链)
   single_template = "你是一个专业的助手。任务：{topic}"
   # 既然是单轮，加个 StrOutputParser() 让结果更干净 (不需要 .content)
   single_chain = PromptTemplate.from_template(single_template) | model | StrOutputParser()
   
   for q in single_prompts:
       print(f"单轮提问: {q}")
       # 2. 直接传入变量名 'topic'，让 LangChain 自动帮你进行 format
       response = single_chain.invoke({"topic": q})
       print(f"AI 回复: {response}\n")
   
except Exception as e:
    print(f"❌ 出错: {e}")  

if __name__ == "__main__":
    run_task()