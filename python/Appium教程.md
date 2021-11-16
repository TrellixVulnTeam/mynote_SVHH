# Appium教程
## 安装依赖
1、java需要安装java8版本，太高了会有问题。
2、安卓sdk下载，需要下载Android Studio软件，通过这个软件下载对应的安卓sdk。
## 环境配置
ANDROID_HOME
D:\Android\SDK
CLASSPATH
.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar
JAVA_HOME
F:\Program Files\Java\jdk1.8.0_311
PATH
%ANDROID_HOME%\platform-tools
%JAVA_HOME%\bin
%JAVA_HOME%\jre\bin

## Appium
按照默认配置即可
## Appium inspector
远程主机：
localhost
远程路径
/wd/hub
能力配置--举例
{
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "xxx",
  "appium:appPackage": "tv.danmaku.bili",
  "appium:appActivity": ".MainActivityV2",
  "appium:unicodeKeyboard": true,
  "appium:noReset": true,
  "appium:newCommandTimeout": 6000
}

## 查看需测试app的appPackage名字
```linux
adb shell
venus:/ $ pm list package |grep jingdong
package:com.jingdong.app.mall
```
## 查看
首先在手机上把其他应用全部关闭，启动待测试的应用，在powershell里面输入：
adb shell dumpsys activity > d:/1115.log
查看log信息，搜索realActivity
