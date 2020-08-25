# Git

[git 保证 commit 为直线](https://www.cnblogs.com/weihe-xunwu/p/7392314.html) 先 stash 再 pull 再 stash pop
[git rebase 进行分支合并](https://www.cnblogs.com/LinuSiyu/p/11572739.html)

[git merge --no-ff](https://www.jianshu.com/p/eebbc79d0dc5)
[git 分支管理规范](https://www.jianshu.com/p/eebbc79d0dc5)

[git 更新本地分支信息](refs/remotes/origin/xmh-server)

已有分支之后拉取远程分支

```shell
# 获取远程仓库信息
git fetch
# 使用远程分支创建分支
git checkout -b master origin/master
```

## Git 分支管理规范

- master 分支 protected
- develop 分支可推送，保持最新
- feature 或 ${name} 分支写自己的代码

### 提交代码流程

```shell
git fetch
git checkout develop
git pull origin develop
git checkout xmh
git rebase -i develop
# 这里需要解决冲突，解决之后 develop cherry-pick 一下
git checkout develop
git log --pretty
git cherry-pick ...
git push origin develop
```


```shell
gcd # 切换到 develop 分支
gl # 拉取远程仓库
# 如果 develop 有好几个 commit，xmh 也有好几个 commit，情况会比较复杂，一下子想不清楚
# 这里就先考虑 develop 一个 commit，xmh 几个 commit的情况

```
