from operation.hotissue import Hotissue_Operation
from flask import request, jsonify
import json

# 疾病计入
def count_illness_api():
    hotissue = Hotissue_Operation()
    data = json.loads(request.data)
    i_name = data.get('i_name')
    i_good_fb = data.get('i_good_fb')
    i_bad_fb = data.get('i_bad_fb')
    result = hotissue.count_illness_operation(i_name, i_good_fb, i_bad_fb)
    return jsonify(result)


# 疾病热榜
def list_illness_api():
    hotissue = Hotissue_Operation()
    result = hotissue.list_illness_operation()
    return jsonify(result)



