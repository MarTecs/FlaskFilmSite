# 1.下面三行代码用来定义蓝图
# 从flask中导入Blueprint模块
from flask import Blueprint

# 传递两个参数：参数1是蓝图的名字，参数2是name
home = Blueprint("home", __name__)
import app.home.views
