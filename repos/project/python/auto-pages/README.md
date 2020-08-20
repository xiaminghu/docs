# Auto Pages

## Preface

> 我在 [这里](https://gitee.com/heartaotime/gitee-pages-action) 发现了原项目，
> 并发现原作者是 [yanglbme](https://github.com/yanglbme/gitee-pages-action),
> 在原项目的基础上，我进行了一些修改，以更好地集成到 vuepress 项目中去

## Usage

> 这里我强制要求添加 .auto-pages.json 到 .gitignore 中，
> 毕竟你也一定不希望你的 账号 和 密码 被公之于众

```markdown
# create .auto-pages.json in your project, with following information
{
  "username": "",
  "password": "",
  "repo": "xiaminghu/project",
  "branch": "gh-pages",
  "directory": "",
  "https": true
}

# then add .auto-pages.json to .gitignore
.auto-pages.json

# install required python packages
pip install -r requirements.txt

# run the python scripts, the second parameter is the base_dir(relative/absolute) where .auto-pages.json is saved
python auto-pages.py
python auto-pages.py repos/docs
python auto-pages.py E:/projects/nodejs/docs/repos/docs
```
