from operation.index import Index_Operation
from flask import request, jsonify
import json


# 问答API
def qa_api():
    index = Index_Operation()
    data = json.loads(request.data)
    u_id = data.get('u_id')

    # 调用问答操作
    result = index.qa_operation(data, u_id)

    return result


# 用户账户信息API
def account_api():
    data = json.loads(request.data)
    u_id = data.get('u_id')
    index = Index_Operation()

    # 获取用户账户信息
    data = index.account_operation(u_id)

    return jsonify(data)


# 更新用户信息API
def update_user_api():
    index = Index_Operation()
    data = json.loads(request.data)
    u_id = data.pop('u_id', None)  # 如果 'u_id' 存在，它将被删除并存储在 u_id 变量中，否则 u_id 将为 None

    # 调用更新用户信息操作
    data = index.update_user_operation(u_id, data)

    return jsonify(data)
