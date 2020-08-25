const path = require('path')

module.exports = (options) => ({
  base: '/docs/',
  host: '0.0.0.0',
  port: '80',
  title: '夏明湖的知识海',
  description: 'Dare To Try, Dare to Lose!',
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
        text: 'Languages',
        items: [
          { text: 'cpp', link: '/languages/cpp/' },
          { text: 'java', link: '/languages/java/' },
          { text: 'nodejs', link: '/languages/nodejs/' },
          { text: 'python', link: '/languages/python/' },
          { text: 'shell', link: '/languages/shell/' },
        ],
      },
    ],
  },
  plugins: [
    'beautiful-bar',
    'medium-zoom',
    [
      // 代码复制
      'code-copy',
      { align: 'top' }
    ],
  ],
})
