const path = require('path')

module.exports = (options) => ({
  base: '/project/',
  host: '0.0.0.0',
  port: '80',
  title: '项目文档',
  description: '这里记录了我所有的开源项目的文档说明',
  evergreen: true,
  head: [],
  configureWebpack: {
    resolve: {
      alias: {
        '@software': path.join(options.sourceDir, 'software'),
      },
    },
  },
  themeConfig: {
    sidebarDepth: 3,
    searchMaxSuggestions: 10,
    nav: [
      {
        text: 'NodeJS',
        items: [
          {
            text: 'vuepress-plugin-beautiful-bar',
            link: '/nodejs/vuepress-plugin-beautiful-bar/',
          },
        ],
      },
      {
        text: 'Python',
        items: [
          {
            text: 'auto-pages',
            link: '/python/auto-pages/'
          }
        ]
      }
    ],
  },
  plugins: ['beautiful-bar', 'medium-zoom'],
})
