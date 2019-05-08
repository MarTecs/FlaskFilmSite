# FlaskFilmSite
慕课网上 使用Flask构建微电影网站


## 使用Flask构建微电影网站

### 学习知识点
1. 项目目录如何设计
2. from . import 为什么会存在如此的导入
3. 蓝图的作用：定义了之后可以将一个网站的开发划分为多个独立的模块，例如前台的home.route()与后台的admin.route()
4. 蓝图使用的三个步骤：定义、注册、调用
5. select * from user\G; \G是什么意思啊
6. python每个类的__repr__函数的作用
7. flask中每个类__repr__返回些什么东西
8. flask中数据库添加数据
9. flask使用类逆向生成数据库中的表
10. datetime.utcnow是什么意思，datetime.now是什么意思
11. 静态资源文件替换成url_for是什么鬼
12. url_for() 而不是 url_for=
13. {% block %}中的%与{和}不能有空格

### 前台布局搭建：
1.  静态文件引入 {{ url_for('static', filename='文件路径') }}
2.  定义路由     {{ url_for('模块名.视图名', 变量=参数) }}
3.  定义数据块   {% block 数据块名称 %}...{% endblock %}

### 代码目录
<details>
<summary>展开查看</summary>
<pre><code>
├── 使用Flask构建微电影网站
│   ├── manage.py	入口启动脚本
│   ├── app		    项目app
│   │   ├── __init__.py 初始化文件
│   │   ├── models.py   数据模型文件(前后台共用)
│   │   ├── static      存放静态资源的静态目录
│   │   ├── home        前台模块
│   │   │   │──── __init__.py   初始化脚本
│   │   │   │──── views.py      视图处理文件
│   │   │   │──── forms.py      表单处理文件
│   │   ├── admin       后台模块
│   │   │   │──── __init__.py   初始化脚本
│   │   │   │──── views.py      视图处理文件
│   │   │   │──── forms.py      表单处理文件
│   │   ├── templates   模板目录
│   │   │   │──── home          前台目录
│   │   │   │──── admin         后台目录</code></pre></details>

flask-sqlalchemy是一个企业ORM框架(对象关系映射框架)，通过面向对象的方法来操作数据库，大大提高可重用性，避免使用SQL语句执行重复操作