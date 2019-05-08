# coding:utf8
from flask_wtf import FlaskForm
# 导入wtforms所需的字段
from wtforms import StringField, PasswordField, SubmitField
# 验证信息错误以后，通过ValidationError来抛出
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin

class LoginForm(FlaskForm):
    """
    管理员登录表单
    """
    account = StringField(
        label="账号",
        # 验证器
        validators=[
            DataRequired("请输入账号！")
        ],
        # 描述
        description="账号",
        # 附加的选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"

        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在！")


