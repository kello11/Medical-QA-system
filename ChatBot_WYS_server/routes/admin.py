from flask import Blueprint
from api.admin import *


admin = Blueprint('admin', __name__)


# 创建用户
@admin.route('/users', methods=['POST'])
def create_user_route():
    return create_user_api()


# 获取所有用户
@admin.route('/users', methods=['GET'])
def get_all_users_route():
    return get_all_users_api()


# 获取特定用户
@admin.route('/get_user', methods=['GET'])
def get_user_route():
    return get_user_api()


# 更新用户
@admin.route('/update_user', methods=['POST'])
def update_user_route():
    return update_user_api()


# 删除用户
@admin.route('/delete_user', methods=['POST'])
def delete_user_route():
    return delete_user_api()


# 获取疾病
@admin.route('/illness', methods=['GET'])
def illness_route():
    return illness_api()


# 获取反馈
@admin.route('/feedback', methods=['GET'])
def feedback_route():
    return feedback_api()


# 获取词云数据
@admin.route('/ciyun', methods=['GET'])
def ciyun_route():
    return ciyun_api()


# 获取表格信息
@admin.route('/get_info', methods=['GET'])
def get_info_route():
    return get_info_api()


# 获取每日数据
@admin.route('/daily', methods=['GET'])
def daily_route():
    return daily_api()
