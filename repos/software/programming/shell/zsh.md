# zsh

## 简介

**Recommended Readings**

[vim or emacs?](https://www.zhihu.com/question/19836903)

[org-mode](https://www.cnblogs.com/holbrook/archive/2012/04/12/2444992.html)

## Install

> windows 请安装 [MSYS2](./msys2)

```shell
pacman -S zsh # windows
brew install zsh # mac
apt install zsh # ubuntu
yum install zsh # centos
# 切换 shell 为 zsh，记得重启 shell
echo 'exec zsh' >> ~/.bashrc
```

## Config

> 出现 zsh 卡顿的问题
> 因为 zsh 会自动获取 git 信息

`git config --global oh-my-zsh.hide-status 1`

```shell
# zsh 初始化配置
autoload -Uz zsh-newuser-install
zsh-newuser-install -f
# 配置 autocompletion
autoload -Uz compinstall
compinstall
```

## Plugins

### oh-my-zsh

[官网](https://ohmyz.sh/)
[wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)
[CheatSheet](https://github.com/ohmyzsh/ohmyzsh/wiki/Cheatsheet)

```shell
# 网速快的用这句更简单
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"

# 下载安装脚本，这里用的 gitee 镜像
wget https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh
# 下载之后打开 install.sh 修改
- REMOTE=${REMOTE:-https://github.com/${REPO}.git}
+ REMOTE=${REMOTE:-https://gitee.com/mirrors/oh-my-zsh.git}
# 然后执行
chmod -x install.sh && ./install.sh
```
