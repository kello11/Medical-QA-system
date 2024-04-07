from operation.admin import Admin_Operation
from flask import request, jsonify
import json


# 创建用户API
def create_user_api():
    admin = Admin_Operation()
    data = json.loads(request.data)
    u_username = data.get('u_username')
    u_password = data.get('u_password')
    u_email = data.get('u_email')
    u_gender = data.get('u_gender')
    u_permission = data.get('u_permission')

    # 调用创建用户操作
    result = admin.create_user_operation(u_username, u_password, u_email, u_gender, u_permission)

    return jsonify(result)


# 获取所有用户API
def get_all_users_api():
    admin = Admin_Operation()

    # 调用获取所有用户操作
    result, status_code = admin.get_all_users_operation()

    return jsonify(result, status_code)


# 获取特定用户API
def get_user_api():
    admin = Admin_Operation()
    data = json.loads(request.data)
    u_id = data.pop('u_id', None)

    # 调用获取特定用户操作
    result = admin.get_user_operation(u_id)

    return jsonify(result)


# 更新用户API
def update_user_api():
    admin = Admin_Operation()
    data = json.loads(request.data)
    u_email = data.pop('u_email', None)

    # 调用更新用户信息操作
    result = admin.update_user_operation(u_email, data)

    return jsonify(result)


# 删除用户API
def delete_user_api():
    admin = Admin_Operation()
    data = json.loads(request.data)
    u_email = data.pop('u_email', None)

    # 调用删除用户操作
    result = admin.delete_user_operation(u_email)

    return jsonify(result)


# 获取疾病信息API
def illness_api():
    admin = Admin_Operation()

    # 调用获取疾病信息操作
    result = admin.illness_operation()

    return result


# 获取反馈信息API
def feedback_api():
    admin = Admin_Operation()

    # 调用获取反馈信息操作
    result = admin.feedback_operation()

    return result


# 获取词云信息API
def ciyun_api():
    admin = Admin_Operation()

    # 调用获取词云信息操作
    result = admin.ciyun_operation()

    return result


# 获取详细信息API
def get_info_api():
    admin = Admin_Operation()

    # 调用获取详细信息操作
    result = admin.get_info_operation()

    return result


# 获取每日问答统计API
def daily_api():
    admin = Admin_Operation()

    # 调用获取每日问答统计操作
    result = admin.daily__operation()

    return result
