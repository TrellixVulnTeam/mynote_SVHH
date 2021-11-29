# kivy环境搭建

## 安装虚拟环境包
```python
pip install virtualenv
```


## 创建虚拟环境
```python
virtualenv kv-demo-env
```


## 安装kivy相关包
```python
python -m pip install kivy[full] kivy_examples
```
强制重新安装
```python
pip install --upgrade --force-reinstall kivy[full] kivy_examples -i https://pypi.tuna.tsinghua.edu.cn/simple
```