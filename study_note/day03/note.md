# Day 3: 提示模板 和 变量教程

> **学习日期**: 2026-02-11
> **学习者**: 94年前端转AI
> **状态**: 已完成

---

## 一、今日目标
- [ ]  AI 语言模型语境下，如何创建和使用带变量的提示词模板 python jinjia 类似于 jsx模板语法

## 二、核心知识概述
### 2.1 创建更高效 更能复用的结构化模板
- **定义**: 如果我们用提示词去跟ai沟通 有很多种方式我们需要通过代码来实现这种沟通 那代码怎么写就至关重要
- **核心感悟**: 
  - 通过自己封装一个模板模型函数 这就有了基础
  - 在通过py的jinja模板就可以动态的控制指令的内容 达到灵活 高效复用的目的
---

## 三、实践记录
### 3.1 核心代码实现
  - 初始化ollama补全函数
  - 在模板中添加单个变量 [demo详见](https://github.com/vivienciya-coder/Refactor-Power-to-AI/blob/main/study_note/day03/code/01_llm_client.py)
  - 在模板中添加多个变量 [ demo详见](https://github.com/vivienciya-coder/Refactor-Power-to-AI/blob/main/study_note/day03/code/02_create_propstemplate.py)
  - 在模板中添加list类型的变量  [ demo详见](https://github.com/vivienciya-coder/Refactor-Power-to-AI/blob/main/study_note/day03/code/02_create_propstemplate.py)
  - 在模板中添加动态指令  [demo详见](https://github.com/vivienciya-coder/Refactor-Power-to-AI/blob/main/study_note/day03/code/03_dynamic%20_instructions_template.py)
### 3.2 坑位与 Debug (Q&A)
| 问题现象 | 解决方案 | 核心原理 |
| :--- | :--- | :--- |
| 现象描述 | [方案名称](#solution-id) | 本质原因 |

> ### 💡 实践心得 <a id="solution-id"></a>
---
## 五、 明日计划
- 当前文章不熟悉的单词短句汇整笔记 [day3语言笔记](/study_note/day03/word_note.md)
## 六、 语言学习
- [ ] 下一步任务

---
## 参考资料
- 链接/文档名称