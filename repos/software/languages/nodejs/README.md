# NodeJS

> npm, cnpm, yarn, pnpm 究竟用哪个？

除了 npm 和 yarn, 还有 cnpm 和 pnpm，其中 cnpm 无非是配置了淘宝镜像而已，
而 pnpm 则是改变了 npm 的包管理模式，使用软链接来减少 node_modules 的体积，这其实本质上来说很好。
但是，由于各方对 pnpm 的支持太少，所以在后期使用的时候可能会碰到十分棘手的问题，
这种情况下你甚至无法排查到底是哪里出了问题，以至于需要重装系统来清理 node 的环境，
而这样的代价实在是太大了。因此，建议不要去节省空间使用 pnpm。

## 问题集合

[无法加载文件 C:\Program Files\nodejs\npm.ps1，因为在此系统上禁止运行脚本。](https://www.cnblogs.com/chenzhiran/p/12080349.html)
