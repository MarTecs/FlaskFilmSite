# 第1个参数是蓝图，第2个参数是URL地址的前缀，通过地址的前缀来划分前后台地址的路由
from flask import Flask, render_template
app = Flask(__name__)
app.debug = True
# 2.下面4行代码实现注册蓝图
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(home_blueprint, url_prefix="/")

# 404页面搭建
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404