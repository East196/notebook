# virtualenv

## install

pip install virtualenv

virtualenv test_env --no-site-packages

cd test_env/Scripts

activate 进入虚拟环境
deactivate 退出虚拟环境


## windows:

pip install virtualenvwrapper-win
设置环境变量 WORKON_HOME

使用`mkvirtual test_env`创建干净的python环境，并且自动进入

workon 得到列表
workon test_env
deactivate

## anaconda
conda的方式简单粗暴
conda -n envname install alib blib clib

## pycharm
使用pycharm在内部打开terminal就是在所在env下，无需担心，直接pip即可
