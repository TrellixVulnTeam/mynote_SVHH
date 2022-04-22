# Pycharm笔记
## autopep8设置
```text
名称：autopep8
程序：autopep8
实参：--in-place --aggressive $FilePath$
工作目录：$ProjectFileDir$
```
## QtDesigner设置
```text
名称：QtDesigner
程序：F:\PycharmProjects\pyqt5学习\venv\Lib\site-packages\QtDesigner\designer.exe
实参：无
工作目录：$ProjectFileDir$
```
## PyUIC设置
```text
名称：PyUIC
程序：F:\PycharmProjects\pyqt5学习\venv\Scripts\python.exe
实参：-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
工作目录：$FileDir$
```
## qrcTOpy设置
```text
名称：qrcTOpy
程序：F:\PycharmProjects\pyqt5学习\venv\Scripts\pyrcc5.exe
实参：$FileName$ -o $FileNameWithoutExtension$_rc.py
工作目录：$FileDir$
```
## 运行pyqt5代码失败
```text
this application failed to start because on qt platform plugin could beinitilaied reinstalling the application may fis this problem
问题原因：没有配置项目中 qt platform plugin 的环境变量 ，导致pycharm无法查找到plugin
解决方法：
添加系统变量
变量名：QT_QPA_PLATFORM_PLUGIN_PATH
变量值：F:\PycharmProjects\pyqt5学习\venv\Lib\site-packages\PyQt5\Qt5\plugins\
```
