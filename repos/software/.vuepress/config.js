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

    ],
  },
  plugins: ['beautiful-bar', 'medium-zoom'],
})
