from operation.feedback import Feedback_Operation
from flask import request, jsonify
import json


# 创建feedback
def create_feedback_api():
    feedback = Feedback_Operation()
    data = json.loads(request.data)
    f_type = data.get('f_type')
    f_content = data.get('f_content')
    u_id = data.get('u_id')
    f_result = data.get('f_result')
    result = feedback.create_feedback_operation(f_type, f_content, u_id, f_result)
    return jsonify(result)


# 获取所有feedback
def get_all_feedback_api():
    feedback = Feedback_Operation()
    result = feedback.get_all_feedback_operation()
    return jsonify(result)


# 获取特定用户反馈信息
def get_user_feedback_api():
    feedback = Feedback_Operation()
    data = json.loads(request.data)
    f_username = data.pop('f_username', None)
    result = feedback.get_user_feedback_operation(f_username)
    return jsonify(result)


# 更新解决状态
def update_feedback_api():
    feedback = Feedback_Operation()
    data = json.loads(request.data)
    f_id = data.get('f_id')
    f_result = data.get('f_result')
    result = feedback.update_feedback_operation(f_id, f_result)
    return jsonify(result)


# 删除反馈信息
def delete_feedback_api():
    feedback = Feedback_Operation()
    data = json.loads(request.data)
    f_id = data.get('f_id')
    result = feedback.delete_feedback_operation(f_id)
    return jsonify(result)
