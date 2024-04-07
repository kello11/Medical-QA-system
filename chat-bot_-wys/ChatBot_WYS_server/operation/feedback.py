from exts import db
from models.user import Feedback_Model


class Feedback_Operation:

    def create_feedback_operation(self, f_type, f_content, u_id, f_result):
        # 添加反馈操作，接受反馈类型、内容、用户ID和结果作为参数
        try:
            # 创建新的反馈记录并将其提交到数据库
            new_feedback = Feedback_Model(f_type=f_type, f_content=f_content, u_id=u_id, f_result=f_result)
            db.session.add(new_feedback)
            db.session.commit()
            return {'msg': '反馈添加成功', 'code': 2000}
        except Exception as e:
            db.session.rollback()
            return {'msg': f'反馈添加失败：{str(e)}', 'code': 2001}

    def get_all_feedback_operation(self):
        # 获取所有反馈操作，返回所有反馈记录的列表
        try:
            # 查询所有反馈记录
            feedbacks = Feedback_Model.query.all()

            if feedbacks:
                # 将反馈信息转换为字典列表
                feedback_list = [
                    {'f_id': f.f_id, 'f_type': f.f_type, 'f_username': f.u_username, 'f_content': f.f_content,
                     'f_result': f.f_result, 'f_time': f.f_time}
                    for f in feedbacks]
                return {'data': feedback_list, 'code': 2100}

            return {'msg': '没有找到任何反馈信息', 'code': 2101}
        except Exception as e:
            return {'msg': f'无法获取反馈信息列表：{str(e)}', 'code': 2102}

    def get_user_feedback_operation(self, f_username):
        # 获取特定用户反馈操作，接受用户名作为参数，返回特定用户的反馈记录列表
        try:
            # 查询特定用户的反馈记录
            feedbacks = Feedback_Model.query.filter_by(f_username=f_username).all()

            if feedbacks:
                # 将反馈信息转换为字典列表
                feedback_list = [
                    {'f_id': f.f_id, 'u_username': f.u_username, 'f_content': f.f_content, 'f_result': f.f_result}
                    for f in feedbacks]
                return {'data': feedback_list, 'code': 2200}

            return {'msg': '没有找到匹配用户的反馈信息', 'code': 2201}
        except Exception as e:
            return {'msg': f'无法获取用户反馈信息：{str(e)}', 'code': 2202}

    def update_feedback_operation(self, f_id, f_result):
        # 更新解决状态操作，接受反馈ID和结果作为参数，更新反馈的解决状态
        try:
            # 查询特定反馈记录
            feedback = Feedback_Model.query.get(f_id)
            if not feedback:
                return {'msg': '反馈信息不存在', 'code': 2300}

            # 更新反馈的解决状态并提交到数据库
            feedback.f_result = f_result
            db.session.commit()
            return {'msg': '反馈信息更新成功', 'code': 2301}
        except Exception as e:
            db.session.rollback()
            return {'msg': f'反馈信息更新失败：{str(e)}', 'code': 2302}

    def delete_feedback_operation(self, f_id):
        # 删除反馈信息操作，接受反馈ID作为参数，删除特定反馈记录
        try:
            # 查询特定反馈记录
            feedback = Feedback_Model.query.get(f_id)
            if not feedback:
                return {'msg': '反馈信息不存在', 'code': 2400}

            # 删除反馈记录并提交到数据库
            db.session.delete(feedback)
            db.session.commit()
            return {'msg': '反馈删除成功', 'code': 2401}
        except Exception as e:
            db.session.rollback()
            return {'msg': f'反馈删除失败：{str(e)}', 'code': 2402}
