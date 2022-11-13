from app import db


#创建数据库模型类
class Module(db.Model):
    __tablename__ = 'Modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)


class Title(db.Model):
    __tablename__ = 'Titles'
    Title_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.String(128), unique=False)
    Deadline = db.Column(db.String(128), unique=True)
    Situation = db.Column(db.Enum("Yes", "No"), unique=True)

    Module_id = db.Column(db.Integer, db.ForeignKey('Modules.id'))