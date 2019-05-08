# 3. 调用蓝图
from . import home
# 导入渲染模板的文件，可以帮助我们渲染网页
# url_for 是路由生成器
from flask import render_template, redirect, url_for 



@home.route("/login/")
def login():
    return render_template("home/login.html")

# 退出其实就是跳转到登录页面
@home.route("/logout/")
def logout():
    # 跳转到home模块下的login视图
    return redirect(url_for("home.login"))

@home.route("/regist/")
def regist():
    return render_template("home/regist.html")

# 会员中心页面
@home.route("/user/")
def user():
    return render_template("home/user.html")

# 修改密码
@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")

# 评论记录
@home.route("/comments/")
def comments():
    return render_template("home/comments.html")

# 登录记录
@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")

# 电影收藏
@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")


@home.route("/")
def index():
    return render_template("home/index.html")

# 轮播图
@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

# 搜索页面搭建
@home.route("/search/")
def search():
    return render_template("home/search.html")

# 电影详情页面搭建
@home.route("/play/")
def play():
    return render_template("home/play.html")

