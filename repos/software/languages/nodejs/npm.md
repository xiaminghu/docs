# Npm

## 用法

```shell
# 使用淘宝镜像
npm config set registry https://registry.npm.taobao.org
# 使用官方镜像
npm config set registry https://registry.npmjs.org
# 设置代理
npm config set proxy http://127.0.0.1:8080
npm config set https-proxy http://127.0.0.1:8080
# 删除代理
npm config delete proxy
npm config delete https-proxy
# 查看所有配置
npm config ls
# 删除所有包
npm uninstall *
```
