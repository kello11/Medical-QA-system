    from exts import db
from datetime import datetime
import pytz

china_tz = pytz.timezone('Asia/Shanghai')


class Users_Model(db.Model):
    __tablename__ = 'user'
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_username = db.Column(db.String(45), nullable=False, unique=True)
    u_password = db.Column(db.String(255), nullable=False)
    u_email = db.Column(db.String(100), nullable=False, unique=True)
    u_gender = db.Column(db.Integer)  # 1为男性，0为女性
    u_permission = db.Column(db.Integer, default=1, nullable=False)  # 用户权限，1为普通用户，0为管理员，默认为普通用户

    # 添加与用户回答历史记录的关联关系
    user_history = db.relationship('UserHistory_Model', backref='user', lazy=True)


class Mail_Model(db.Model):
    __tablename__ = 'email_captcha'
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_email = db.Column(db.String(100), nullable=False)
    u_captcha = db.Column(db.String(100), nullable=False)


class UserHistory_Model(db.Model):
    __tablename__ = 'user_history'
    h_chatID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    h_question = db.Column(db.String(255), nullable=False)
    h_answer = db.Column(db.String(500), nullable=False)
    h_dialogID = db.Column(db.Integer, nullable=False)
    h_time = db.Column(db.DateTime, default=lambda: datetime.now(china_tz), nullable=False)
    # 添加与用户表的外键关联
    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False)


class Illness_Model(db.Model):
    # 表名
    __tablename__ = 'illness'
    # 字段名称
    i_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    i_name = db.Column(db.String(45), nullable=False, unique=True)
    i_count = db.Column(db.Integer, default=1, nullable=False)
    i_good_fb = db.Column(db.Integer, default=0, nullable=False)
    i_bad_fb = db.Column(db.Integer, default=0, nullable=False)


class Feedback_Model(db.Model):
    # 表名
    __tablename__ = 'feedback'
    # 字段名称
    f_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_type = db.Column(db.String(50), nullable=False)
    f_content = db.Column(db.String(500))
    f_result = db.Column(db.Integer, default=0)  # 默认值仍然可以存在
    f_time = db.Column(db.DateTime, default=lambda: datetime.now(china_tz), nullable=True)

    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False, unique=False)
    u_username = db.Column(db.String(45), nullable=True, unique=False)  # 添加用户名字段

    def __init__(self, f_type, f_content, u_id, f_result=0):  # 添加默认值为0的f_result参数
        self.f_type = f_type
        self.f_content = f_content
        self.u_id = u_id
        self.f_result = f_result  # 设置f_result的值
        user = Users_Model.query.get(u_id)
        if user:
            self.u_username = user.u_username
