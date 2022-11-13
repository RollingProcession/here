from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__,
    template_folder='../templates',  # 表示在当前目录 (myproject/A/) 寻找模板文件
    static_folder='../static',  # 表示为上级目录 (myproject/) 开通虚拟资源入口
    static_url_path='',  # 这是路径前缀, 个人认为非常蛋疼的设计之一, 建议传空字符串, 可以避免很多麻烦
)

app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models
