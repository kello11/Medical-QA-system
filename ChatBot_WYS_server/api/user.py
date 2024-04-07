from operation.user import User_Operation
from flask import request
import json
from exts import mail
import string
import random
from flask_mail import Message


# 用户登录API
def User_login_api():
    result = {}
    # 从请求数据中获取用户名和密码
    data = json.loads(request.data)
    username = data['u_username']
    password = data['u_password']

    # 创建用户操作对象
    u = User_Operation()

    # 调用用户登录操作
    data = u.user_login_operation(username)

    if data is None:
        result['code'] = 401
        result['msg'] = "没有账户信息"
    elif data.u_password == password:
        if data.u_permission == 0:  # 判断是否是管理员（0为管理员）
            result['code'] = 201
            result['msg'] = "管理员登录"
        else:
            result['code'] = 200
            result['msg'] = "用户登录"
            result['u_id'] = data.u_id
            result['u_username'] = data.u_username
            result['u_email'] = data.u_email
    else:
        result['code'] = 400
        result['msg'] = "密码错误!"

    return result


# 发送邮箱验证码API
def Mail_captcha_api():
    u = User_Operation()

    # 从请求数据中获取邮箱
    data = json.loads(request.data)
    email = data['u_email']
    choice = data['choice']  # 0是注册， 1是找回密码
    # 生成随机的6位验证码
    source = string.digits * 6
    captcha = random.sample(source, 6)
    captcha = ''.join(captcha)

    # 创建邮件消息对象，发送验证码邮件
    message = Message(subject="医药问答邮箱验证码", recipients=[email], body=f"您的验证码是:{captcha}")
    mail.send(message)

    # 调用保存验证码的操作
    data = u.mail_captcha_operation(email, captcha, choice)

    return data


# 用户注册API
def User_register_api(username, email, password, gender):
    result = {}
    u = User_Operation()

    # 调用用户注册操作
    data = u.user_register_operation(username=username, email=email, gender=gender, password=password)

    if data:
        result['code'] = 300
        result['msg'] = "注册成功"
    else:
        result['code'] = 301
        result['msg'] = "注册失败"

    return result


# 用户历史记录API
def History_api():
    data = json.loads(request.data)
    u = User_Operation()

    # 调用获取用户历史记录的操作
    result = {'history': u.get_history_operation(data.get('u_id'))}

    return result

def forget_password_api():
    data = json.loads(request.data)
    u = User_Operation()
    email = data.get('email')
    new_password = data.get('new_password')
    captcha = data.get('captcha')
    result = u.forget_password_operation(email=email, captcha=captcha, new_password=new_password)
    return result






