from exts import db
from models.user import Users_Model, UserHistory_Model
import requests
from config import base_url_1, base_url_2


class Index_Operation:

    def qa_operation(self, data, user_id):
        # QA（问答）操作，接受数据和用户ID作为参数，执行与API的交互，记录历史记录
        question = data['question']
        dialog_id = data['dialog_id']
        choice = data['choice']
        # 构建完整的URL，基于配置中的基础URL和选择
        if choice == '0':
            url = f"{base_url_1}/service/api/ichat"
        else:
            url = f"{base_url_2}/service/api/rule_chat"
        response = requests.post(url, json=data)
        data = response.json()
        answer = data['reply']
        disease = data['disease']
        new_history = UserHistory_Model(h_question=question, h_answer=answer, h_dialogID=dialog_id, u_id=user_id)
        db.session.add(new_history)
        db.session.commit()
        return {'answer': answer, 'disease': disease, 'time': new_history.h_time, 'code': 800}

    def account_operation(self, user_id):
        # 查询用户模型以获取用户信息
        user = Users_Model.query.filter_by(u_id=user_id).first()
        if user:
            return {'msg': '用户信息获取成功', 'u_username': user.u_username,
                    'u_email': user.u_email, 'u_password': user.u_password, 'code': 500}
        else:
            return {'msg': '未找到用户信息', 'code': 404}

    def update_user_operation(self, user_id, data):
        # 更新用户操作，接受用户ID和数据作为参数，根据传入的数据更新用户信息
        user = Users_Model.query.filter_by(u_id=user_id).first()
        # 更新用户信息，根据传入的 data 进行更新
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return {'msg': '用户信息更新成功', 'code': 500}
