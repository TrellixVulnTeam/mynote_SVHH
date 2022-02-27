# 命令行工具--typer
## 参数和默认值
```python
import typer


def main(name: str, lastname: str, formal: bool = False):
    if formal:
        typer.echo(f"Good day Ms. {name} {lastname}.")
    else:
        typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
```
解析：
name 和lastname是Arguments，formal是Options，因为formal给了默认值，就是Options了。有默认值的参数要定义在最后面。
有默认值的参数他就不是必须的参数，typer默认将他设置为Options参数。
## 对命令行程序进行说明
```python
import typer


def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        typer.echo(f"Good day Ms. {name} {lastname}.")
    else:
        typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
```
上面三引号说明部分将打印在help信息里。

## 打印信息使用颜色
```python
import typer


def main(good: bool = True):
    message_start = "everything is "
    if good:
        ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
    else:
        ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
    message = message_start + ending
    typer.echo(message)


if __name__ == "__main__":
    typer.run(main)
```
secho函数作用和上面类似，用起来更简便。
```python
import typer


def main(name: str):
    typer.secho(f"Welcome here {name}", fg=typer.colors.MAGENTA)


if __name__ == "__main__":
    typer.run(main)
```

## 终止程序
### 退出程序
```python
import typer

existing_usernames = ["rick", "morty"]


def maybe_create_user(username: str):
    if username in existing_usernames:
        typer.echo("The user already exists")
        raise typer.Exit()
    else:
        typer.echo(f"User created: {username}")


def send_new_user_notification(username: str):
    # Somehow send a notification here for the new user, maybe an email
    typer.echo(f"Notification sent for new user: {username}")


def main(username: str):
    maybe_create_user(username=username)
    send_new_user_notification(username=username)


if __name__ == "__main__":
    typer.run(main)
```
### 带错误退出
```python
import typer


def main(username: str):
    if username == "root":
        typer.echo("The root user is reserved")
        raise typer.Exit(code=1)
    typer.echo(f"New user created: {username}")


if __name__ == "__main__":
    typer.run(main)
```
感觉上面两个没啥区别呀。

### Abort退出
```python
import typer


def main(username: str):
    if username == "root":
        typer.echo("The root user is reserved")
        raise typer.Abort()
    typer.echo(f"New user created: {username}")


if __name__ == "__main__":
    typer.run(main)
```
区别就是退出的时候会打印一个Abort！单词。
## 命令行参数
### 可选的命令行参数
```python
import typer


def main(name: str = typer.Argument(...)):
# def main(name: str):和上面的效果相同。
# ...表示这个参数没有默认值，是必选参数
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
为name提供了一个默认值，name仍然是参数，不是选项。此时不再是必须参数。
```python
import typer


def main(name: str = typer.Argument(default='qin')):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```

```python
from typing import Optional

import typer


def main(name: Optional[str] = typer.Argument(None)):
# Optional[str] 和str效果一样，后面提供了默认值，和自己写的默认omc列表类似
# typer.Argument换成typer.Option name就变成可选项了。
    if name is None:
        typer.echo("Hello World!")
    else:
        typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```

### 动态默认值
```python
import random

import typer


def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


def main(name: str = typer.Argument(get_name)):
#调用上面的get_name函数
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
每次运行结果不一样。
### 命令行参数增加帮助信息
```python
import typer


def main(name: str = typer.Argument(..., help="The name of the user to greet")):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
### 定制默认字符串
```python
import typer


def main(
    name: str = typer.Argument(
        "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
    )
):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
帮助信息显示默认值的时候，显示的是show_default的信息，不是Wade Wilson。

### 帮助信息中隐藏命令行参数名
```python
import typer


def main(name: str = typer.Argument("World", hidden=True)):
    """
    Say hi to NAME very gently, like Dirk.
    """
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
目的就是不想让人看到参数的名字。
## 命令行选项介绍
### 帮助信息中隐藏默认值
```python
import typer


def main(fullname: str = typer.Option("Wade Wilson", show_default=False)):
    typer.echo(f"Hello {fullname}")


if __name__ == "__main__":
    typer.run(main)
```
### 命令行选项变成必须参数
```python
import typer


def main(name: str, lastname: str = typer.Option(...)):
    typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
```
三个点的省略号就可以把选项参数变成必须参数。
### 命令行选项提示
```python
import typer


def main(name: str, lastname: str = typer.Option(..., prompt=True)):
    typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
```
输完参数后，如果忘了输入必须的选项参数，程序会提示让你输入，比较人性化。
```python
import typer


def main(
    name: str, lastname: str = typer.Option(..., prompt="Please tell me your last name")
):
    typer.echo(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
```
这个属于是定制化显示忘记输入的信息，使输入者更明了忘了输入什么。
### 确认提示
```python
import typer


def main(project_name: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
    typer.echo(f"Deleting project {project_name}")


if __name__ == "__main__":
    typer.run(main)
```
就是输入提示缺少的信息后，让你在输入一边确认。
### 密码提示
```python
import typer


def main(
    name: str,
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    typer.echo(f"Hello {name}. Doing something very secure with password.")
    typer.echo(f"...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    typer.run(main)
```
使用场景：输入密码时屏幕不显示信息。
### 命令行选项参数名称
```python
import typer


def main(user_name: str = typer.Option(..., "--name")):
# def main(user_name: Optional[str] = typer.Option(..., "--name")): 和上面的效果一样
    typer.echo(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
```

### 命令行选项短名
```python
import typer
from typing import Optional


def main(user_name: Optional[str] = typer.Option(..., "--name",'-n')):
# 这里可以把长名--name删掉，只留短名
    typer.echo(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
```
### 验证命令行参数
```python
import typer


def name_callback(value: str):
    if value != "Camila":
        raise typer.BadParameter("Only Camila is allowed")
    return value


def main(name: str = typer.Option(..., callback=name_callback)):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
对命令行必须选项参数进行验证，确保输入的参数符合预期。

示例：
通过callback函数对参数omc列表进行判断。
```python
import typer
from typing import List


def main_callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    typer.echo(f"校验OMC参数: {param.name}")
    if value == ():
        return 'omc10', 'omc20'
    for v in value:
        if v not in ('omc1', 'omc2', 'omc3'):
            raise typer.BadParameter(f"{v}不是一个有效的omc")
    return value


def main(
        omc_list: List[str] = typer.Argument(
            default=None, callback=main_callback),
):
    typer.echo(omc_list)


if __name__ == '__main__':
    typer.run(main)

```
### 增加版本信息
```python
from typing import Optional

import typer

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        typer.echo(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


def main(
    name: str = typer.Option("World"),
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback
    ),
):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
### 定制自动补全的值
```python
import typer


def complete_name():
    return ["Camila", "Carlos", "Sebastian"]


def main(
    name: str = typer.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    )
):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```
输入--name 按tab键可以让你从complete_name中选择。比较人性化。

## 命令简介
```python
import typer

app = typer.Typer()


@app.command()
def create():
    typer.echo("Creating user: Hiro Hamada")


@app.command()
def delete():
    typer.echo("Deleting user: Hiro Hamada")


if __name__ == "__main__":
    app()
```
用两个@app.command()可以创建两个子命令，如果只使用一个的话，没有子命令效果。
### 命令行选项
```python
import typer

app = typer.Typer()


@app.command()
def create(username: str):
    typer.echo(f"Creating user: {username}")


@app.command()
def delete(
    username: str,
    force: bool = typer.Option(..., prompt="Are you sure you want to delete the user?"),
):
    if force:
        typer.echo(f"Deleting user: {username}")
    else:
        typer.echo("Operation cancelled")


@app.command()
def delete_all(
    force: bool = typer.Option(..., prompt="Are you sure you want to delete ALL users?")
):
    if force:
        typer.echo("Deleting all users")
    else:
        typer.echo("Operation cancelled")


@app.command()
def init():
    typer.echo("Initializing user database")


if __name__ == "__main__":
    app()
```
上面例子可以对输入的信息确认，比如是否确定要删除某个账号。
```python
import typer

app = typer.Typer(help="Awesome CLI user manager.")
# 整个命令行工具的帮助信息


@app.command()
def create(username: str):
    """
    Create a new user with USERNAME.
    """
    typer.echo(f"Creating user: {username}")


@app.command()
def delete(
    username: str,
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete the user?",
        help="Force deletion without confirmation.",
    ),
):
    """
    Delete a user with USERNAME.

    If --force is not used, will ask for confirmation.
    """
    # 子命令的帮助信息
    if force:
        typer.echo(f"Deleting user: {username}")
    else:
        typer.echo("Operation cancelled")


@app.command()
# 每个子命令都可以使用帮助信息，help=''写在command()中
def delete_all(
    force: bool = typer.Option(
        ...,
        prompt="Are you sure you want to delete ALL users?",
        help="Force deletion without confirmation.",
    )
):
    """
    Delete ALL users in the database.

    If --force is not used, will ask for confirmation.
    """
    if force:
        typer.echo("Deleting all users")
    else:
        typer.echo("Operation cancelled")


@app.command()
def init():
    """
    Initialize the users database.
    """
    typer.echo("Initializing user database")


if __name__ == "__main__":
    app()
```

### 自定义命令名称
```python
import typer

app = typer.Typer()


@app.command("4")
#为函数指定命令名称
def cli_create_user(username: str):
    typer.echo(f"Creating user: {username}")


@app.command("delete")
def cli_delete_user(username: str):
    typer.echo(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
```

### callback为主命令指定参数
```python
import typer

app = typer.Typer()
state = {"verbose": False}


@app.command()
def create(username: str):
    if state["verbose"]:
        typer.echo("About to create a user")
    typer.echo(f"Creating user: {username}")
    if state["verbose"]:
        typer.echo("Just created a user")


@app.command()
def delete(username: str):
    if state["verbose"]:
        typer.echo("About to delete a user")
    typer.echo(f"Deleting user: {username}")
    if state["verbose"]:
        typer.echo("Just deleted a user")


@app.callback()
def main(verbose: bool = False):
    """
    Manage users in the awesome CLI app.
    """
    if verbose:
        typer.echo("Will write verbose output")
        state["verbose"] = True


if __name__ == "__main__":
    app()
```
### 只有一个命令行函数的子命令
```python
import typer

app = typer.Typer()


@app.command()
def create():
    typer.echo("Creating user: Hiro Hamada")

# 增加一个callback 上面的create就变成了子命令
@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
```
### callback中添加命令行说明文档
```python
import typer

app = typer.Typer()


@app.command()
def create():
    typer.echo("Creating user: Hiro Hamada")


@app.callback()
def callback():
    """
    Creates a single user Hiro Hamada.

    In the next version it will create 5 users more.
    """
    # 会在主命令的帮助文档中显示，子命令帮助文档不显示

if __name__ == "__main__":
    app()
```
### 使用上下文
```python
import typer

app = typer.Typer()


@app.command()
def create(username: str):
    typer.echo(f"Creating user: {username}")


@app.command()
def delete(username: str):
    typer.echo(f"Deleting user: {username}")


@app.callback()
def main(ctx: typer.Context):
    """
    Manage users in the awesome CLI app.
    """
    # 当执行哪个子命令时，会打印出执行哪个子命令的信息
    typer.echo(f"About to execute command: {ctx.invoked_subcommand}")


if __name__ == "__main__":
    app()
```

```python
import typer

app = typer.Typer()


@app.command()
def create(username: str):
    typer.echo(f"Creating user: {username}")


@app.command()
def delete(username: str):
    typer.echo(f"Deleting user: {username}")


@app.callback(invoke_without_command=True)
# 使用invoke_without_command=True 参数，执行主命令（不执行子命令）时也会显示echo的信息
def main():
    """
    Manage users in the awesome CLI app.
    """
    typer.echo("Initializing database")


if __name__ == "__main__":
    app()
```

```python
import typer

app = typer.Typer()


@app.command()
def create(username: str):
    typer.echo(f"Creating user: {username}")


@app.command()
def delete(username: str):
    typer.echo(f"Deleting user: {username}")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Manage users in the awesome CLI app.
    """
    # 通过逻辑判断，只有单独执行主命令（不跟子命令）时才会echo信息。更人性化
    if ctx.invoked_subcommand is None:
        typer.echo("Initializing database")


if __name__ == "__main__":
    app()
```

## 命令行参数类型
```python
import typer


def main(name: str, age: int = 20, height_meters: float = 1.89, female: bool = True):
# 起到数据验证的效果，如果输入的age不是int 会有报错提示
    typer.echo(f"NAME is {name}, of type: {type(name)}")
    typer.echo(f"--age is {age}, of type: {type(age)}")
    typer.echo(f"--height-meters is {height_meters}, of type: {type(height_meters)}")
    typer.echo(f"--female is {female}, of type: {type(female)}")


if __name__ == "__main__":
    typer.run(main)
```

```python
import typer


def main(
    id: int = typer.Argument(..., min=0, max=1000),
    age: int = typer.Option(20, min=18),
    score: float = typer.Option(0, max=100),
):
    typer.echo(f"ID is {id}")
    typer.echo(f"--age is {age}")
    typer.echo(f"--score is {score}")


if __name__ == "__main__":
    typer.run(main)
```
可以对int float类型通过min和max指定其范围。
### bool类型选项
```python
import typer


def main(force: bool = typer.Option(False, "--force")):
# force: bool = False 这样写的话帮助信息里面会显示--force/--no-force
    if force:
        typer.echo("Forcing operation")
    else:
        typer.echo("Not forcing")


if __name__ == "__main__":
    typer.run(main)
```

```python
from typing import Optional

import typer


def main(accept: Optional[bool] = typer.Option(None, "--accept/--reject")):
    if accept is None:
        typer.echo("I don't know what you want yet")
    elif accept:
        typer.echo("Accepting!")
    else:
        typer.echo("Rejecting!")


if __name__ == "__main__":
    typer.run(main)
```
为bool型的true false 指定特定的名称。
### bool类型指定短名称
```python
import typer


def main(force: bool = typer.Option(False, "--force/--no-force", "-f/-F")):
    if force:
        typer.echo("Forcing operation")
    else:
        typer.echo("Not forcing")


if __name__ == "__main__":
    typer.run(main)
```

### 枚举选择器
```python
from enum import Enum

import typer


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(network: NeuralNetwork = NeuralNetwork.simple):
# network: NeuralNetwork = typer.Option(NeuralNetwork.simple, case_sensitive=False) 可以实现大小写不敏感
    typer.echo(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    typer.run(main)
```
限定了network选项只能从simple、conv、lstm三个参数里面选择

### 路径参数
```python
from pathlib import Path
from typing import Optional

import typer


def main(config: Optional[Path] = typer.Option(None)):
    if config is None:
        typer.echo("No config file")
        raise typer.Abort()
    if config.is_file():
        text = config.read_text()
        typer.echo(f"Config file contents: {text}")
    elif config.is_dir():
        typer.echo("Config is a directory, will use all its config files")
    elif not config.exists():
        typer.echo("The config doesn't exist")


if __name__ == "__main__":
    typer.run(main)
```
可以对输入的信息进行判断，是文件还是目录 还是不存在。
## 子命令
### 从不同的文件添加子命令
items.py
```python
import typer

app = typer.Typer()


@app.command()
def create(item: str):
    typer.echo(f"Creating item: {item}")


@app.command()
def delete(item: str):
    typer.echo(f"Deleting item: {item}")


@app.command()
def sell(item: str):
    typer.echo(f"Selling item: {item}")


if __name__ == "__main__":
    app()
```

users.py
```python
import typer

app = typer.Typer()


@app.command()
def create(user_name: str):
    typer.echo(f"Creating user: {user_name}")


@app.command()
def delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
```

main.py
```python
import typer

import items
import users

app = typer.Typer()
app.add_typer(users.app, name="users")
app.add_typer(items.app, name="items")

if __name__ == "__main__":
    app()
```
每个子命令我可以单独写一个python文件，然后写一个主文件，将所有用到的子命令导入就可以了。
### 在一个文件中定义多个子命令
```python
import typer

app = typer.Typer()
items_app = typer.Typer()
app.add_typer(items_app, name="items")
users_app = typer.Typer()
app.add_typer(users_app, name="users")


@items_app.command("create")
def items_create(item: str):
    typer.echo(f"Creating item: {item}")


@items_app.command("delete")
def items_delete(item: str):
    typer.echo(f"Deleting item: {item}")


@items_app.command("sell")
def items_sell(item: str):
    typer.echo(f"Selling item: {item}")


@users_app.command("create")
def users_create(user_name: str):
    typer.echo(f"Creating user: {user_name}")


@users_app.command("delete")
def users_delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
```