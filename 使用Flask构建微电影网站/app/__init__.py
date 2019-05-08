# 第1个参数是蓝图，第2个参数是URL地址的前缀，通过地址的前缀来划分前后台地址的路由
from flask import Flask, render_template
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置参考http://www.pythondoc.com/flask-sqlalchemy/config.html
# 用于连接数据的数据库
# 格式：mysql://username:password@server/db
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/movie"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
# 这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 这里是后来加进去的，因为flask处理表单需要CSRF验证，也就是一个令牌
# 使用uuid.uuid4().hex
app.config['SECRET_KEY'] = "c7dae4123d9f48cebef61ec6c6c5520a"
app.debug = True


# 实例化SQLAlchemy ,并传入app对象
db = SQLAlchemy(app)


# 2.下面4行代码实现注册蓝图
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(home_blueprint, url_prefix="/")


# 404页面搭建
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
