from exts import db
from models.user import Users_Model, Illness_Model, UserHistory_Model
from datetime import datetime, timedelta

class Admin_Operation:

    # 创建用户操作，接受用户名、密码、邮箱、性别和权限作为参数
    def create_user_operation(self, u_username, u_password, u_email, u_gender, u_permission):
        try:
            new_user = Users_Model(u_username=u_username, u_password=u_password,
                                   u_email=u_email, u_gender=u_gender, u_permission=u_permission)
            db.session.add(new_user)
            db.session.commit()
            return {'msg': '用户创建成功', 'code': 501},
        except Exception as e:
            db.session.rollback()
            return {'msg': f'用户创建失败：{str(e)}', 'code': 500}

    # 获取所有用户
    def get_all_users_operation(self):
        try:
            users = Users_Model.query.all()
            user_list = [{'u_username': user.u_username, 'u_email': user.u_email, 'u_password': user.u_password}
                         for user in users]
            return user_list, {'code': 601}
        except Exception as e:
            return {'msg': f'无法获取用户列表：{str(e)}', 'code': 600}

    # 获取特定用户
    def get_user_operation(self, user_id):
        try:
            user = Users_Model.query.get(user_id)
            if user:
                return {'u_username': user.u_username,
                        'u_email': user.u_email, 'u_password': user.u_password, 'code': 701}
            return {'msg': '用户不存在', 'code': 404}
        except Exception as e:
            return {'msg': f'无法获取用户信息：{str(e)}', 'code': 700}

    # 更新用户
    def update_user_operation(self, u_email, data):
        try:
            user = Users_Model.query.filter_by(u_email=u_email).first()
            if not user:
                return {'msg': '用户不存在', 'code': 404}

            for key, value in data.items():
                setattr(user, key, value)

            db.session.commit()
            return {'msg': '用户信息更新成功', 'code': 801}
        except Exception as e:
            db.session.rollback()
            return {'msg': f'用户信息更新失败：{str(e)}', 'code': 800}

    # 删除用户
    def delete_user_operation(self, u_email):
        try:
            user = Users_Model.query.filter_by(u_email=u_email).first()
            if not user:
                return {'msg': '用户不存在', 'code': 404}

            db.session.delete(user)
            db.session.commit()
            return {'msg': '用户删除成功', 'code': 901}
        except Exception as e:
            db.session.rollback()
            return {'msg': f'用户删除失败：{str(e)}', 'code': 900}

    # 疾病操作，获取所有疾病信息并返回列表
    def illness_operation(self):
        illness_data = Illness_Model.query.all()
        illness_list = []
        for illness in illness_data:
            illness_json = {
                'i_name': illness.i_name,
                'i_count': illness.i_count
            }
            illness_list.append(illness_json)

        return illness_list

    # 反馈操作，获取所有反馈信息并返回好评和差评的总数
    def feedback_operation(self):
        feedback_data = Illness_Model.query.all()
        total_good = 0
        total_bad = 0
        for feedback in feedback_data:
            total_good += feedback.i_good_fb
            total_bad += feedback.i_bad_fb

        return {'好评': total_good, '差评': total_bad}

    # 词云操作，获取所有疾病信息并返回用于词云的数据格式
    def ciyun_operation(self):
        ciyun_data = Illness_Model.query.all()
        ciyun_list = []
        for illness in ciyun_data:
            illness_json = {
                'name': illness.i_name,
                'value': illness.i_count
            }
            ciyun_list.append(illness_json)

        return ciyun_list

    # 获取信息操作，获取疾病信息并返回好评、差评、好评率的数据格式
    def get_info_operation(self):
        info = Illness_Model.query.all()
        info_list = []
        for data in info:
            data_json = {
                'name': data.i_name,
                'good': data.i_good_fb,
                'bad': data.i_bad_fb,
                'good_rate': data.i_good_fb/(data.i_good_fb+data.i_bad_fb)
            }
            info_list.append(data_json)

        return info_list

    # 每日问答操作，计算最近5天的每日问答数量并返回字典格式的统计数据
    def daily__operation(self):
        # 计算最近5天的日期范围
        end_date = datetime.now()
        start_date = end_date - timedelta(days=4)

        # 初始化一个字典来存储每天的问答数量统计
        qa_counts_by_day = {}

        # 查询数据库获取每天的问答记录数量
        current_date = start_date
        while current_date <= end_date:
            next_date = current_date + timedelta(days=1)

            query = db.session.query(db.func.count().label('count')).filter(
                UserHistory_Model.h_time >= current_date,
                UserHistory_Model.h_time < next_date
            )

            result = query.first()
            if result:
                qa_count = result.count
            else:
                qa_count = 0

            qa_counts_by_day[current_date.strftime('%Y-%m-%d')] = qa_count
            current_date = next_date

        print(qa_counts_by_day)
        return qa_counts_by_day
