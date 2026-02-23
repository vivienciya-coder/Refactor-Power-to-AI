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
#少样本分析案例
#为情感分析创建一个少样本提示词应用
# 情感分类的定义以及应用场景
# 情感分类定义：判断情感基调 确定语言中包含的情绪 比如积极消极中立等
# 应用场景：客服、市场调研、社交媒体分析。
#如何去实现基于代码
#1. 准备3个例子 作为样本
#2. 基于这些例子 构建提示词模板
#3. 预训练知识
# 关键点
# 提示词模板： 把样本组合成完美对模型友好的提示词模板
# 控制 提示词和大模型的交互

#定义情感分类的class
def few_shot_sentiment_analysis(input_text):
    #定义情感分类结构化模板
    few_shot_template = PromptTemplate(
        input_variables=["input_text"],
        template = """ 
            把一下情感按照 积极 消极 中立 这三类进行分类
            Examples:
            Text:我感觉自己这两天又胖了.
            Sentiment:消极

            Text:今天天气晴朗.
            Sentiment:中立

            Text:这个电影太难看了.
            Sentiment:消极

            现在请分类
            Text:{input_text}
            情绪:
            """
    )
    chain = few_shot_template | llm
    res = chain.invoke(input_text).content
    print(res)
    # strip 去掉两端多余的空行和空格
    res = res.strip()
    # 我们只需要情感判断的结果 不需要输出其他
    if ':' in res:
        res = res.split(':')[1].strip()
    return res

test_text = "这个新开的餐厅太让人不可置信了！"
result = few_shot_sentiment_analysis(test_text)
print(f"Input: {test_text}")
print(f"Predicted Sentiment: {result}")