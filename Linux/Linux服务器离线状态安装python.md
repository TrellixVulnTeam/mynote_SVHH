# Linux服务器离线状态安装python
##  CentOS7 离线安装gcc环境
先下载一个 gcc-c++-4.8.5-39.el7.x86_64.tar.gz
提取码：krca
放到系统中以后，解压
进入解压后的文件夹
```linux
rpm -Uvh *.rpm --nodeps --force
```
这条命令还是解释一下
-Uvh: U=升级安装 v=显示执行过程 h=套件安装时列出标记
--nodeps: 安装时不验证依赖关系
--force:强制安装
安装完成后执行 gcc -v 出现版本信息算是安装成功
## 服务器上安装python
首先第一点，安装依赖包，这一点也很重要，要不然后面会报各种错误
```linux
 yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```
上面的软件包可以在rpm网站逐个下载统一安装
然后在python官网https://www.python.org/ftp/python/用wget安装自己想要的版本。
```linux
tar -zxvf 资源包名称
cd 解压后的文件夹
./configure --prefix=/root/training/Python-3.6.5   # 指定安装目录
make
make install
```
## Python离线环境安装三方库
```linux
pip download numpy pandas
```
上面命令会下载三方库和相关依赖到本地，不会在本地安装，注意有些三方库分不同的操作系统，最好用相同的操作系统下载三方库。
下载完毕后，传到服务器，用pip命令安装三方库。
```linux
pip install --no-index pandas
```


## Linux上安装oracle和数据提取工具

home/wlyhgl/qx/process/nokia_tools
/home/wlyhgl/qx/process/instantclient_21_5
```linux
export NOKIA_HOME="/home/wlyhgl/qx/process/nokia_tools"
export ORACLE_HOME=/home/wlyhgl/qx/process/instantclient_21_5
export PATH=$NOKIA_HOME:$ORACLE_HOME:$PATH
export TNS_ADMIN=$ORACLE_HOME/network/admin
export LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH
export NLS_LANG='AMERICAN_AMERICA.AL32UTF8'
```
注意事项：
目录不能有中文
检查Linux服务器到数据库是否通
```linux
telnet 10.217.15.44 1521
```