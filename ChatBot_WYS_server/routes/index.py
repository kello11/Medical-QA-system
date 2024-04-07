from flask import Blueprint
from api.index import *


index = Blueprint('index', __name__)


# 问答
@index.route('/qa', methods=['POST'])  # 问答
def qa_route():
    return qa_api()


# 我的账户管理
@index.route('/account', methods=['POST'])
def account_route():
    return account_api()


# 更新用户
@index.route('/account/update', methods=['POST'])
def update_user_route():
    return update_user_api()
