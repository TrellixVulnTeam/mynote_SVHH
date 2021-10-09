# zsh 文件夹颜色修改
1. cd ~

2. dircolors -p > .dircolors

3. vim .dircolors
找到 OTHER_WRITABLE 34;42
修改为 OTHER_WRITABLE 34;01

4. vim .zshrc
编辑.zshrc，添加下面这段(是从.bashrc拷贝出来的)
 if [ -x /usr/bin/dircolors ]; then
     test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
        alias ls='ls --color=auto'
        alias dir='dir --color=auto'
        alias vdir='vdir --color=auto'
        alias grep='grep --color=auto'
        alias fgrep='fgrep --color=auto'
        alias egrep='egrep --color=auto'
 fi

5. source .zshrc

搞定，修改方法找到了，举一反三，调整其他颜色都so easy!