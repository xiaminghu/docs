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
        text: 'Languages',
        items: [
          { text: 'nodejs', link: '/languages/nodejs/'},
        ]
      },
      {
        text: 'Programming',
        items: [
          { text: 'shell', link: '/programming/shell/'},
          { text: 'vcs', link: '/programming/vcs/'},
        ]
      }
    ],
  },
  plugins: ['beautiful-bar', 'medium-zoom'],
})
