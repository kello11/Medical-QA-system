from flask import Blueprint
from api.hotissue import *

hotissue = Blueprint('hotissue', __name__)


# 疾病计数
@hotissue.route('/illness', methods=['POST'])
def count_illness_route():
    return count_illness_api()


# 疾病排行榜
@hotissue.route('/i_list', methods=['POST'])
def list_illness_route():
    return list_illness_api()
