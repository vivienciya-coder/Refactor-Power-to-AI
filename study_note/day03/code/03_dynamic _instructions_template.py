import os
import sys
from jinja2 import Template
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
#占位符
from langchain_core.prompts import PromptTemplate 
load_dotenv()

# 1. 解决 VPN 导致本地连接 502 的问题
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'

def get_completion(prompt,model="gemma3:4b",temperature=0):
    ''' 我们从ollama得到一个补全的结果
    Args:
     propmt(str):把提示词放到api中
     model(str):使用什么模型进行补全
     temperature(int):温度参数，控制生成文本的随机程度，值越高生成的文本越随机，值越低生成的文本越确定。
    Returns:
        str:返回大模型补全的结果的结果 
    '''
    message = [{"role": "user", "content": prompt}]
    response = ChatOllama(model=model,temperature=temperature,base_url="http://127.0.0.1:11434").invoke(message)
    return response.content

class PromptTemplate:
    ''' 创建一个带有参数的提示词模板类
    Attributes:
        template(str):提示词模板字符串，包含占位符
        input_variables(list):在模板中需要变成变量的提示词
    '''
    #定义一个初始化方法
    def __init__(self,template,input_variables):
        self.template = Template(template) #把传入的模板字符赋值给这个类的属性template
        self.input_variables = input_variables #把传入的变量符赋值给这个类的属性input_variables
    #定义一个格式化方法
    def format(self,**kwargs):
        return self.template.render(**kwargs) #把传入的变量符替换掉模板中的占位符
#写一个点变量的提示词模板
simple_template = PromptTemplate(
    template ="请解释一下{{topic}}是什么？",
    input_variables = ["topic"] #从模板中定义为topic的提示词放入input_variables列表中
    ) 
#写一个带有动态指令的提示词模板
dynamic_instruction_template = PromptTemplate(
    template=
    "task:{{task}}\n"
    "context:{{context}}\n"
    "constraints:{{constraints}}\n"
    "请给{{task}}提供一个解决方案，要求满足以下的约束条件：{{constraints}}，并且基于以下的上下文信息：{{context}}",
    input_variables = ["task","context","constraints"] #从模板中定义为instruction的提示词放入input_variables列表中
)
#使用这个动态指令
print("================动态指令模板的返回结果========")
print(get_completion(dynamic_instruction_template.format(
    task="如何提高学习效率？",
    context="学习效率是指在单位时间内能够有效地完成学习任务的能力。提高学习效率可以帮助我们更快地掌握知识和技能。",
    constraints="1. 需要提供具体的学习方法；2. 需要考虑不同学习者的个体差异；3. 需要基于科学的研究和实践经验。"
)))