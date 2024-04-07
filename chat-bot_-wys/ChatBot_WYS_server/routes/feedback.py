from flask import Blueprint
from api.feedback import *


feedback = Blueprint('feedback', __name__)


@feedback.route('/create', methods=['POST'])
def create_feedback_route():
    return create_feedback_api()


# 获取所有反馈
@feedback.route('/get_all', methods=['GET'])
def get_all_feedback_route():
    return get_all_feedback_api()


# 获取特定用户
@feedback.route('/get_feedback', methods=['GET'])
def get_user_feedback_route():
    return get_user_feedback_api()


# 更新解决状态
@feedback.route('/update_feedback', methods=['POST'])
def update_feedback_route():
    return update_feedback_api()


# 删除反馈信息
@feedback.route('/delete_feedback', methods=['POST'])
def delete_feedback_route():
    return delete_feedback_api()
