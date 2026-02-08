# Day1 基本环境的搭建
## 环境安装
    1. ide vscode
    2. py3.12 pip
## 模型 
    1. https://ollama.com/
## lesson1 提示工程简介
###     1. 这本书讲的是什么
 - 如何设计好的提示词去跟ai沟通 如果没有好的提示词那么也不能有效的和ai进行沟通 就像开始人们学习js 后来拥抱 vue react一样的进程一样 
### 2. 动机
- 和ai有效的沟通 才能释放大模型的全部潜力 来更好更快 来各种各样的问题 Prompt Engineering 是将 AI 从“聊天机器人”转变为“生产力引擎”的控制协议。
### 3. 核心内容
    1. 什么是提示工程 以及他的重要性
    2. 结构化提示工程  不同的提示工程得到不同的处理结果 要想得到不同的结果也就需要不同的提示工程
    3. 提示工程的重要性 提示工程是如何影响ai性能的
    4. 提示工程与ai融合有广阔的应用价值
    5. 提示工程和ai融合的实际案列
   
### 正文1. 核心概念和重要性
####      prompt engineering 是什么
 - 设计和优化喂给大语言模型的提示词 让大模型生成达到预期的结果 来解决各种各样的问题
#### prompt engineering 的重要性
````
    1. 提升ai生成的内容和质量
    2. 引导语言模型更有效的执行任务
    3. 克服ai模型的局限性和偏见
    4. 个性化 满足不同的场景和人群
````
####   **角色在ai和大模型中的重要性**
````
    1. 定制化 根据不同的需求输出不同的内容
    2. 提高准确性 让ai输出的内容更准确
    3. 处理更负责的任务
    4. 减少偏差 让ai的输出更中立更健康
````
    1. 如何让ai更中立更具有准确性
```
    1. 加入评估和修正指令 强制让ai启动逻辑核查机制而非简单的语义匹配
    2. 如果不加入评估和修正指令 ai默认输入的是事实
    3. 
```
#### 提升解决复杂问题的能力
    1. 处理涉及数学、逻辑、代码重构的任务时，必须强制 AI 输出思考过程。指令一步一步 按照逻辑推理 这种很明确的指令


## 问题整理
1. **问题1**： 网络环境防御 (Network Defense)：本地搭建的ollma 在因为开了vpn 无法访问到ollama
    ````
    解决：代码：os.environ['NO_PROXY'] = 'localhost,127.0.0.1'
    目的：解决 VPN 全局模式下，本地请求被误拦截导致的 502 错误。
    原理：强制 Python 进程在发起 HTTP 请求时跳过代理层，直接访问本地回环地址。
    老兵心得：在做本地 AI 开发（Ollama）时，这是必加的保命代码，能让你在开启翻墙查资料的同时，顺畅地运行本地模型。
    ````
2. **问题2** 在搭建 Node.js 环境或执行 npx vitepress init 时，可能会遇到 PowerShell 提示“禁止运行脚本”的错误。这是 Windows 的默认安全设置，我们可以通过调整执行策略来解决。
    - **现象**
        ```
        npm : 无法加载文件 C:\Program Files\nodejs\npm.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkI
        D=135170 中的 about_Execution_Policies。
        ```
   - **原因**
      - Windows 默认的安全级别（Restricted）阻止了本地脚本（如 npm.ps1, npx.ps1）的运行。这类似于浏览器禁止执行不安全的内联脚本。
   - **解决** 我们需要在“当前用户”范围内，将安全策略调整为 RemoteSigned，允许本地签名的脚本执行。
        ```
        # 将当前用户的执行策略修改为 RemoteSigned 
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
        ```
## googleai助教快照指令
我是 94 年前端大龄转 AI 学习者。我们已经完成了 intro-prompt-engineering-lesson 的学习并部署到了 GitHub Pages。现在的协作模式是：你负责翻译、深度分析和下一步指导。请基于此进度继续。”
## 参考资料
- [prompting官方网站](https://www.promptingguide.ai/zh/techniques/cot)
- [大厂是怎么做的](https://cookbook.openai.com/)