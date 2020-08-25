# NVM

## Install

**Windows**

[nvm-windows](https://github.com/coreybutler/nvm-windows/releases)

**MacOS**

```shell
# 安装 nvm，安装成功后路径在 ./nvm
## 方法一
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.35.2/install.sh | bash
## 方法二
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.35.2/install.sh | bash
## 使用国内镜像
export NVM_NODEJS_ORG_MIRROR=http://npm.taobao.org/mirrors/node
# 设置 nvm 环境变量
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion
```

## Config

```shell
# 设置 Node 安装镜像
nvm node_mirror https://npm.taobao.org/mirrors/node/
# 设置 NPM 安装镜像
nvm npm_mirror https://npm.taobao.org/mirrors/npm/
# 显示可安装的版本
nvm list available
# 安装 14.5.0 版本，具体版本根据自己的需求进行修改
nvm install 14.5.0
# 切换到
nvm use 14.5.0
# 配置 npm 镜像
npm config set registry https://registry.npm.taobao.org
# 安装 yarn
npm i -g yarn
# 配置 yarn 镜像
yarn config set registry http://registry.npm.taobao.org/
```

## Usage

```shell
# 设置 Node 安装镜像
nvm node_mirror https://npm.taobao.org/mirrors/node/
# 设置 NPM 安装镜像
nvm npm_mirror https://npm.taobao.org/mirrors/npm/
# 显示可安装的版本
nvm list available
nvm ls-remote
# 安裝
nvm install latest 64 # 安装 64 位最新版
nvm install v14.5.0 # 安裝指定版本
nvm install --lts node # 安装长期维护最新版本
# 查看已安装的版本
nvm ls
# 切换 node 版本
nvm use 14.5.0
# 查看当前版本
nvm current
# 设置別名，windows 无效
nvm alias default v14.5.0
```
