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