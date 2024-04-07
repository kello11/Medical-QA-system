from sqlalchemy import func
from models.user import *


class User_Operation:

    def user_login_operation(self, username):
        # 用户登录操作，接受用户名作为参数，返回用户对象或None
        user = Users_Model.query.filter_by(u_username=username).first()
        return user

    def mail_captcha_operation(self, email, captcha, choice):
        # 存储邮箱验证码到数据库
        result = {}
        user = Users_Model.query.filter_by(u_email=email).first()
        if choice == 0:
            if not user:
                email_captcha = Mail_Model(u_email=email, u_captcha=captcha)
                db.session.add(email_captcha)
                db.session.commit()
                result['msg'] = '成功发送验证码'
                result['code'] = 630
            else:
                result['msg'] = '该邮箱已经被注册'
                result['code'] = 633
        if choice == 1:
            if user:
                email_captcha = Mail_Model(u_email=email, u_captcha=captcha)
                db.session.add(email_captcha)
                db.session.commit()
                result['msg'] = '成功发送验证码'
                result['code'] = 630
            else:
                result['msg'] = '该邮箱未被注册'
                result['code'] = 644
        return result


    def user_register_operation(self, username, email, password, gender):
        # 用户注册操作，接受用户名、邮箱、密码和性别作为参数，创建用户记录并提交到数据库
        user = Users_Model(u_username=username, u_email=email,
                           u_gender=gender, u_password=password)
        db.session.add(user)
        db.session.commit()
        if user is None:
            return False
        else:
            return True

    def get_history_operation(self, u_id):
        # 获取用户历史记录操作，接受用户ID作为参数，返回历史记录列表和对话数量
        user_histories = UserHistory_Model.query.filter_by(u_id=u_id).all()
        history = []  # 创建一个列表来存储历史记录
        results = {}
        max_dialog_id = UserHistory_Model.query.with_entities(func.max(UserHistory_Model.h_dialogID)).scalar()
        for user_history in user_histories:
            result = {
                'question': user_history.h_question,
                'answer': user_history.h_answer,
                'datetime': user_history.h_time.strftime('%Y/%m/%d %H:%M:%S'),
                'dialogID': user_history.h_dialogID
            }
            history.append(result)
        results['code'] = 808
        results['history'] = history
        results['dialog_count'] = max_dialog_id
        return results

    def forget_password_operation(self, email, captcha, new_password):
        # 重置用户密码操作
        captcha_model = Mail_Model.query.filter_by(u_email=email, u_captcha=captcha).first()
        result = {}
        if not captcha_model:
            result['msg'] = '验证码错误'
            result['code'] = 770
        else:
            user = Users_Model.query.filter_by(u_email=email).first()
            user.u_password = new_password
            db.session.commit()
            result['msg'] = '密码重置成功'
            result['code'] = 771
        return result
