# 3. 调用蓝图
from . import admin
# flash是消息的闪现,用于提示密码错误，如果密码正确，那么我们就要保存，用到session会话
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm
from app.models import Admin

@admin.route("/")
def index():
    return render_template("admin/index.html")


@admin.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 获取表单数据
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash("密码错误！")
            return redirect(url_for("admin.login"))
        session['admin'] = data["account"]
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


@admin.route("/logout/")
def logout():
    # 跳转到视图
    session.pop("account", None)
    return redirect(url_for("admin.login"))


@admin.route("/pwd/")
def pwd():
    # 跳转到视图
    return render_template("admin/pwd.html")


@admin.route("/tag/add/")
def tag_add():
    # 跳转到视图
    return render_template("admin/tag_add.html")


@admin.route("/tag/list/")
def tag_list():
    # 跳转到视图
    return render_template("admin/tag_list.html")


@admin.route("/movie/add/")
def movie_add():
    # 跳转到视图
    return render_template("admin/movie_add.html")


@admin.route("/movie/list/")
def movie_list():
    # 跳转到视图
    return render_template("admin/movie_list.html")


@admin.route("/preview/list/")
def preview_list():
    # 跳转到视图
    return render_template("admin/preview_list.html")


@admin.route("/preview/add/")
def preview_add():
    # 跳转到视图
    return render_template("admin/preview_add.html")


@admin.route("/user/list/")
def user_list():
    # 跳转到视图
    return render_template("admin/user_list.html")


@admin.route("/user/view/")
def user_view():
    # 跳转到视图
    return render_template("admin/user_view.html")


@admin.route("/comment/list/")
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route("/moviecol/list/")
def moviecol_list():
    return render_template('admin/moviecol_list.html')


@admin.route("/oplog/list")
def oplog_list():
    return render_template('admin/oplog_list.html')


@admin.route("/adminloginlog/list")
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route("/userloginlog/list")
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


@admin.route("/auth/add")
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route("/auth/list")
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route("/role/add")
def role_add():
    return render_template('admin/role_add.html')


@admin.route("/role/list")
def role_list():
    return render_template('admin/role_list.html')


@admin.route("/admin/add")
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route("/admin/list")
def admin_list():
    return render_template('admin/admin_list.html')
