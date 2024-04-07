from flask import Blueprint
from api.user import *
from flask import request
from utils.register_form import RegisterForm
from models.user import Users_Model

user = Blueprint('user', __name__)


# 用户登录
@user.route('/login', methods=['POST'])
def login_route():
    return User_login_api()


# 邮箱获取
@user.route('/captcha/email', methods=['POST'])
def email_captcha_route():
    return Mail_captcha_api()


# 用户注册
@user.route('/register', methods=['GET', 'POST'])
def register_route():
    data = json.loads(request.data)
    u_email = data['u_email']
    u = Users_Model.query.filter_by(u_email=u_email).first()
    if u:
        return {'msg': '邮箱已被注册', 'code': 303}
    form = RegisterForm(data=data)
    if form.validate():
        data = json.loads(request.data)
        u_email = data['u_email']
        u_gender = data['u_gender']
        u_username = data['u_username']
        u_password = data['u_password']
        data = User_register_api(email=u_email, gender=u_gender,
                                 username=u_username, password=u_password)
        return data
    else:
        return {'msg': '验证码错误', 'code': 302}


# 获取历史
@user.route('/history', methods=['POST'])
def history_route():
    return History_api()


#  找回密码
@user.route('/forget_password', methods=['POST'])
def forget_password_route():
    return forget_password_api()
