const path = require('path')

module.exports = (options) => ({
  base: '/software/',
  host: '0.0.0.0',
  port: '80',
  title: '',
  description: '',
  evergreen: true,
  head: [],
  configureWebpack: {},
  themeConfig: {
    sidebarDepth: 3,
    searchMaxSuggestions: 10,
    nav: [
      {
        text: 'Programming',
        items: [
          { text: 'Shell', link: '/programming/shell/' },
          { text: 'VCS', link: '/programming/vcs/' },
          { text: 'IDE', link: '/programming/ide/' },
          { text: 'Languages', link: '/programming/languages/' },
          { text: 'Others', link: '/programming/others/' },
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
      { align: 'top' },
    ],
  ],
})
