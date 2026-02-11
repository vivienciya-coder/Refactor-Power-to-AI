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
# 多个变量提示词模板
complex_temmplate = PromptTemplate(
    template = "请以{{role}}的身份向{{userq}}用户，解释一下{{topic}}是什么？",
    input_variables = ["role","userq","topic"] #从模板中定义为role,userq,topic的提示词放入input_variables列表中
)
#写个带有数组类型的变量的提示词
items_template = PromptTemplate(
    template="请把一下的{{items}}进行分类，并且给出每一类的名称。并且以{{role}}的角度对每一种分类进行解释。",
    input_variables = ["items","role"]
)
# 写个带有数组类型的变量的提示词
#开始使用这个模板
print("================简单模板的返回结果========")
single_prompt = simple_template.format(topic="光合作用")
print(get_completion(single_prompt))
print("================复杂模板的返回结果========")
multi_prompt = complex_temmplate.format(role="老师",userq="学生",topic="光合作用")
print(get_completion(multi_prompt))
print("================复杂模板带有数组和变量的返回结果========")
type_prompt = items_template.format(items=["苹果","香蕉","橙子","衣服","桌子","椅子","发卡"],role="水果分类专家")
print(get_completion(type_prompt))