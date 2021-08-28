# 记一次Python解决文件编码转换问题
日常工作中，经常需要将csv文件上传到业支集群hive中，但是由于windows下大部分csv文件都是gbk、gb2312、gb18030的编码格式，这些格式在Linux下会出现中文乱码的情况。
为解决该问题可从以下几方面入手解决。
1、在windows下打开csv文件，另存为utf8格式的csv文件。这种方式只适用与比较小的csv文件，文件一旦过大，要么excel打不开，要么打开后显示不全。
2、在Linux下使用iconv命令对文件进行转码，对Linux系统命令行比较熟悉的用户可以使用。
3、使用Python语言自己编写一个专用的文本文件转utf8编码的命令行工具。

综合以上特点，我选择了第三种方法，使用cchardet、os、argparse库编写命令行工具来对文件进行utf8转码。具体代码如下：
```python
import cchardet as chardet
import os, argparse


class ToUTF8:
    def __init__(self) -> None:
        self.filename_list = self.postion_arg().file

    def get_encoding(self,filename):
        with open(filename, "rb") as f:
            msg = f.read()
            result = chardet.detect(msg)
            #对utf8 bom 、ASCII和编码可信度按情况判断，符合条件的 只返回utf-8
            if result['encoding'] == 'UTF-8-SIG' or result['encoding'] == 'ASCII' and result['confidence'] > 0.9:
                return 'UTF-8'
            #如果可信度较低，使用中文的GB18030编码
            elif result['confidence']< 0.9:
                return 'GB18030'
            else:
                return (result['encoding'])

    def conv(self):
        #循环文件名列表
        for filename in self.filename_list:
            with open(filename,'r',encoding=self.get_encoding(filename)) as f1, open('%s.bk'%filename,'w',encoding='utf8') as f2:
                for line in f1:
                    f2.write(line)
            os.rename('%s.bk'%filename,filename+'.tmp')
            os.rename(filename,filename+'.bk')
            os.rename(filename+'.tmp', filename)


    #位置参数定义
    def postion_arg(self):
        parser = argparse.ArgumentParser(description='其他编码转换为UTF8编码',prog='其他编码转换为UTF8编码')
        #可传入多个文件，生成一个文件名列表
        parser.add_argument('file',nargs='+',help='源文件')
        parser.add_argument('-v','--version', action="version", version='%(prog)s 0.0.1', help="版本信息")
        args = parser.parse_args()
        return args

    def main(self):
        self.conv()

```

通过以上代码，可windows的cmd命令行下或powershell命令行下可快速的对1个或多个文件进行转码（转为utf8编码）。
使用方法如下：
```powershell
PS F:\file\tmp> ls


    目录: F:\file\tmp


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2021/8/25     14:18       45155219 nr_1.csv
-a----         2021/8/10     17:23        1761504 nr_2.csv


PS F:\file\tmp> utf8 .\nr_1.csv .\nr_2.csv
PS F:\file\tmp> ls


    目录: F:\file\tmp


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2021/8/27     22:52       53789636 nr_1.csv
-a----         2021/8/25     14:18       45155219 nr_1.csv.bk
-a----         2021/8/27     22:52        1841129 nr_2.csv
-a----         2021/8/10     17:23        1761504 nr_2.csv.bk
```
命令执行完毕后，会把原来的文件名加.bk后缀，生成的新文件即为utf8编码格式。注意：utf8编码格式（不带bom）在Windows下打开会乱码，但在Linux下会显示正常。

最后
命令安装方法：
```
pip install python-tool-qinxuan
```