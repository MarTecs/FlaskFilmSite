# 用来存放数据模型
from datetime import datetime
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 配置参考http://www.pythondoc.com/flask-sqlalchemy/config.html
# 用于连接数据的数据库
# 格式：mysql://username:password@server/db
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/movie"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
# 这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 实例化SQLAlchemy ,并传入app对象
db = SQLAlchemy(app)


# 注册的会员数据模型，也就是会员表
class User(db.Model):
    # 对应的数据库表名
    __tablename__ = "user"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 昵称
    name = db.Column(db.String(100), unique=True)
    # 密码
    pwd = db.Column(db.String(100))
    # 邮箱
    email = db.Column(db.String(100), unique=True)
    # 手机号
    phone = db.Column(db.String(11), unique=True)
    # 个性简介
    info = db.Column(db.Text)
    # 头像
    face = db.Column(db.String(255), unique=True)
    # 注册时间
    addtime = db.Column(db.DateTime(), index=True, default=datetime.now)
    # 唯一标志符
    uuid = db.Column(db.String(255), unique=True)

    # 会员日志外键关系关联
    userlog = db.relationship('Userlog', backref='user')
    # 评论外键关系关联
    comments = db.relationship("Comment", backref="user")
    # 电影收藏表外键关系关联
    moviecols = db.relationship("Moviecol", backref="user")

    def __repr__(self):
        return "<User %s>" % self.name
    

# 会员登录日志表
class Userlog(db.Model):
    __tablename__ = "userlog"
    # 编号
    id = db.Column(db.Integer, unique=True, primary_key=True)
    # user_id是一个外键，意思是所属会员
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 登录ip
    ip = db.Column(db.String(100))
    # 登录时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        # %r是占位符
        return "<Userlog %r>" % self.id


# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    name = db.Column(db.String(100), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    # 电影外键关系的关联
    movies = db.relationship("Movie", backref="tag")

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # 电影播放地址
    url = db.Column(db.String(255), unique=True)
    # 电影介绍
    info = db.Column(db.Text)
    # 封面
    logo = db.Column(db.String(255), unique=True)
    # 星级
    star = db.Column(db.SmallInteger)
    # 播放量
    playnum = db.Column(db.BigInteger)
    # 评论量
    commentnum = db.Column(db.BigInteger)
    # 所属标签
    tag_id = db.Column(db.ForeignKey("tag.id"))
    # 地区
    area = db.Column(db.String(255))
    # 上映时间
    release_time = db.Column(db.Date)
    # 播放电影的长度
    length = db.Column(db.String(100))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    # 评论关系关联
    comments = db.relationship("Comment", backref="movie")
    # 电影收藏关系关联
    moviecols = db.relationship("Moviecol", backref="movie")

    def __repr__(self):
        return "<Movie %r>" % self.title


# 上映预告模型
class Preview(db.Model):
    __tablename__ = "preview"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # logo
    logo = db.Column(db.String(255), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
    __tablename__ = "comment"

    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 评论内容
    content = db.Column(db.Text)
    # 所属电影
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    # 所属用户
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Comment %s>" % self.id
    

# 电影收藏表
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    # 所属电影
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    # 所属用户
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(255), unique=True)
    # URL地址
    url = db.Column(db.String(255), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Auth %r>" % self.name


# 定义角色数据模型
# 如果路由地址和角色查出来的地址不匹配，说明没有权限，反之有权限
class Role(db.Model):
    __tablename__ = "role"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 角色名称
    name = db.Column(db.String(100), unique=True)
    # 权限列表
    auths = db.Column(db.String(600), unique=True)
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 账号
    name = db.Column(db.String(255), unique=True)
    # 密码
    pwd = db.Column(db.String(255))
    # 是否是超级管理员,0为超级管理员
    is_super = db.Column(db.SmallInteger)
    # 所处角色关联
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    # 外键关联
    # 管理员登录日志关联
    adminlogs = db.relationship("Adminlog", backref="admin")
    # 管理员操作关联
    oplogs = db.relationship("Oplog", backref="admin")

    def __repr__(self):
        return "<Admin %r>" % self.name


# 管理员登录日志模型
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属管理员
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # 登录ip地址
    ip = db.Column(db.String(100))
    # 操作时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 管理员操作日志数据模型
class Oplog(db.Model):
    __tablename__ = "oplog"
    # 编号
    id = db.Column(db.Integer, primary_key=True)
    # 所属管理员
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # 登录IP
    ip = db.Column(db.String(100))
    # 原因
    reason = db.Column(db.String(600))
    # 添加时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Oplog %r>" % self.id


if __name__ == "__main__":
    # 根据模型生成表
    # db.create_all()
    
    # role = Role(
    #     name="超级管理员",
    #     auths=""
    # )
    # db.session.add(role)
    # db.session.commit()

    from werkzeug.security import generate_password_hash
    admin = Admin(
        name="imoocmovie",
        pwd=generate_password_hash("imoocmovie"),
        is_super=0,
        role_id=1
    )
    db.session.add(admin)
    db.session.commit()
