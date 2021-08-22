win10 Linux子系统安装流程

### 安装前准备
1、开启开发者模式
2、应用商店下载Ubuntu发行版
### 安装后设置
1、修改Ubuntu软件源
```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo vim /etc/apt/sources.list
```
替换成下面内容
```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
```
2、修改hosts文件
sudo vim /etc/hosts
```
# GitHub Start
52.74.223.119 github.com
192.30.253.119 gist.github.com
54.169.195.247 api.github.com
185.199.111.153 assets-cdn.github.com
151.101.76.133 raw.githubusercontent.com
151.101.108.133 user-images.githubusercontent.com
151.101.76.133 gist.githubusercontent.com
151.101.76.133 cloud.githubusercontent.com
151.101.76.133 camo.githubusercontent.com
151.101.76.133 avatars0.githubusercontent.com
151.101.76.133 avatars1.githubusercontent.com
151.101.76.133 avatars2.githubusercontent.com
151.101.76.133 avatars3.githubusercontent.com
151.101.76.133 avatars4.githubusercontent.com
151.101.76.133 avatars5.githubusercontent.com
151.101.76.133 avatars6.githubusercontent.com
151.101.76.133 avatars7.githubusercontent.com
151.101.76.133 avatars8.githubusercontent.com
# GitHub End
```
### 安装zsh和Oh My Zsh
#### 安装zsh：
```
sudo apt install zsh
```

#### 将 Zsh 设置为默认 Shell
```
chsh -s /bin/zsh
```
##### 可以通过 echo $SHELL 查看当前默认的 Shell，如果没有改为 /bin/zsh，那么需要重启 Shell。
第二步：安装 Oh My Zsh

#### 安装 Oh My Zsh
```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
```
#### 以上命令可能不好使，可使用如下两条命令
```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
bash ./install.sh
```
### Zsh 的配置
#### 字体的安装
推荐在终端使用 Powerline 类型的主题，该类型主题可以使用图形表示尽可能多的信息，方便用户的使用。推荐安装用户量最大的 Powerlevel9k。

Powerlevel9k 中需要使用较多的图形符号，字体大多不会自带这些符号，所以需要使用专门的 Powerline 字体。

不推荐安装官方默认的 Powerline Fonts，理由是图形符号不全，符号处会有乱码。推荐安装 Nerd-Fonts 系列字体，因为该系列字体附带有尽可能全的符号，并且更新非常频繁，项目地址在这里。例如直接下载 Ubuntu Font Family 中的 Ubuntu Nerd Font Complete.ttf ，然后直接在Ubuntu下安装。
#### 主题及字体的配置
如果要在  Oh My Zsh中安装 Powerlevel9k ，只需执行如下指令：
```
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```
#### 插件配置
#####  autojump
更快地切换目录，不受当前所在目录的限制。

安装：
```
sudo apt install autojump
```
用法：

##### 跳转到目录
```
j dir
```
##### fasd
快速访问文件或目录，功能比前一个插件强大。

安装：
```
sudo apt install fasd
```
用法：
```
alias f='fasd -f'          # 文件
alias d='fasd -d'        # 目录
alias a='fasd -a'        # 任意
alias s='fasd -si'       # 显示并选择

alias sd='fasd -sid'        # 选择目录
alias sf='fasd -sif'          # 选择文件
alias z='fasd_cd -d'       # 跳转至目录
alias zz='fasd_cd -d -i'  # 选择并跳转至目录
```
#### zsh-autosuggestions命令行命令键入时的历史命令建议插件

按照官方文档提示，直接执行如下命令安装：
```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```
#### 命令行语法高亮插件

按照官方文档提示，直接执行如下命令安装：
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
#### 插件最终配置
##### autojump 功能弱，fasd 功能强，但是没 autojump 实用
##### 值得注意的是，根据官方文档，zsh-syntax-highlighting 插件需放在最后
```
plugins=(
  git extract autojump zsh-autosuggestions zsh-syntax-highlighting
)
```
#### 「.zshrc」文件完整修改
Oh My Zsh 配置文件的完整修改结果，只有对配置文件进行如下修改，才能使上述配置生效。

#### 设置字体模式以及配置命令行的主题，语句顺序不能颠倒
```
POWERLEVEL9K_MODE='nerdfont-complete'
ZSH_THEME="powerlevel9k/powerlevel9k"
```

##### 以下内容去掉注释即可生效：
##### 启动错误命令自动更正
```
ENABLE_CORRECTION="true"
```
##### 在命令执行的过程中，使用小红点进行提示
```
COMPLETION_WAITING_DOTS="true"
```
##### 启用已安装的插件
```
plugins=(
  git extract fasd zsh-autosuggestions zsh-syntax-highlighting
)
```
#### Windows Terminal 设置
```
终端主题网站：
https://windowsterminalthemes.dev/
可以到该网站找自己喜欢的主题
"guid": "{2c4de342-38b7-51cf-b940-2309a097f518}",
                "hidden": false,
                "name": "Ubuntu",
                "colorScheme" : "Cyberdyne",
                "startingDirectory" :"/home/qinxuan",
                "fontFace" :"MesloLGS NF",
                "fontSize": 11,
                "acrylicOpacity": 0.7,
                "useAcrylic":true,
                "backgroundImageOpacity": 0.5,
                "backgroundImage": "f:\\文档\\壁纸\\1.jpg",
                "source": "Windows.Terminal.Wsl"
```

### 安装 Powerlevel10k主题
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k

```
### 打开zsh的配置文件
```bash
sudo vim ~/.zshrc
```
### 选择主题为我们下载主题
```bash
ZSH_THEME=powerlevel10k/powerlevel10k
```
### 安装字体
```
MesloLGS NF Regular.ttf
MesloLGS NF Bold.ttf
MesloLGS NF Italic.ttf
MesloLGS NF Bold Italic.ttf
```
### 配置 Powerlevel10k

#### 自动配置脚本
Powerlevel10k 提供了一个配置脚本，运行脚本后只需回答几个简单的问题即可完成配置。

直接输入 p10k configure 即可进入配置问答界面。
```
p10k configure
```

### 安装pip3
```
sudo apt-get install python3-pip
```
### 安装csvkit工具
```
sudo pip3 install csvkit
```
### 安装csvtk工具
```
网站：https://github.com/shenwei356/csvtk 下载最新版本
下载完后将文件复制到/usr/local/bin/目录下
sudo cp csvtk /usr/local/bin/
```

### 文件夹颜色显示处理
```linux
cd ~/
dircolors -p > .dircolors
vi .dircolors
```

```linux
<略>
DIR 04;34 # director.
<中略>
STICKY_OTHER_WRITABLE 04;32 # dir that is sticky and other-writable (+t,o+w)
OTHER_WRITABLE 04;34 # dir that is other-writable (o+w) and not sticky
<略>
```
```linux
vim .zshrc
eval $(dircolors -b $HOME/.dircolors)
```