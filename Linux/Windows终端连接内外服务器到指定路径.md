## Windows终端连接内外服务器到指定路径
### prb采集服务器
```Linux
ssh  -t root@10.95.123.109 "cd /home/test/prbcollect/result历史文件/ && exec bash -l"
```
### yitong服务器
```Linux
ssh -t yitong@10.87.44.22  "cd /mnt/data/yitongdata/qinxuan/script/  && exec bash -l"
```
### Nokia服务器
```Linux
ssh  -t  nokia@10.87.44.22  "cd /home/nokia/work/qx/ && exec bash -l"
```