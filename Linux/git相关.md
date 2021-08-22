# git相关
## git Failed to connect to 127.0.0.1 port 7890: Connection refused
```
查看系统代理和git代理已经取消，但是仍然无法clone，查看 cat  ~/.gitconfig信息如下
[http]
        sslVerify = false
[http "https://github.com"]
       proxy = http://127.0.0.1:7890
[https "https://github.com"]
      proxy = https://127.0.0.1:7890

把proxy注释掉后正常
```

## 解决git中文路径显示unicode代码的问题
```linux
git config --global core.quotepath false
```
# 更新远程代码到本地仓库
## 查看本地仓库文件是否有改动
```Linux
git status
```
## 如果有改动的话使用gitGUI工具提交改动并push到远程仓库

## 查看远程仓库
```linux
git remote -v
```
## 从远程获取最新版本到本地
```linux
git fetch origin main:temp
```
git fetch origin main:temp 这句命令的意思是：从远程的origin仓库的master分支下载到本地并新建一个分支temp
## 比较本地的仓库和远程参考的区别
```Linux
git diff temp
```
命令的意思是：比较master分支和temp分支的不同

## 合并temp分支到master分支
```Linux
git merge temp
```
## 如果不想要temp分支了，可以删除此分支
```Linux
git branch -d temp
```
如果该分支没有合并到主分支会报错，可以用以下命令强制删除git branch -D <分支名>


## 使用gitignore文件忽略不需要同步的文件
```
**/vx.json
**/vx_notebook/*
**/vx_recycle_bin/*
```
## gitignore不生效的解决办法
先删除缓存，再从新添加，再提交。
```linux
git rm -r --cached .
git add .
git commit -m 'update.gitignore'
```