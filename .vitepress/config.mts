import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Huge Ai For Evering",
  description: "A VitePress Site",
  base: '/Refactor-Power-to-AI/', // 例如：'/PromptEngineeringStudy/'
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' }
      
    ],

    sidebar: [
      {
        text: '项目',
        items: [
          { text: 'PromptEngineering项目学习笔记', link: '/pages/promptingNote.md',items:[{
            text:'Day1 intro-prompt-engineering-lesson 笔记',link:'/study_note/day01/note.html',
          },
          { text:'Day2 basic-prompt-structures.ipynb 笔记',link:'/study_note/day02/note.html'},
          { text:'Day3 advanced-prompt-techniques.ipynb 笔记',link:'/study_note/day03/note.html'},
         { text:'Day4 zero shot prompt.ipynb 笔记',link:'/study_note/day04/note.html'},]},
          
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
