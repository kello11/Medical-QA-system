from exts import db
from models.user import Illness_Model
from sqlalchemy import desc


class Hotissue_Operation:

    # 疾病计入
    def count_illness_operation(self, i_name, i_good_fb, i_bad_fb):
        # 疾病计数操作，接受疾病名称、好评数和差评数作为参数
        try:
            illness = Illness_Model.query.filter_by(i_name=i_name).first()  # 使用 filter_by 进行查询
            if i_name != '新的对话':
                if not illness:
                    new_illness = Illness_Model(i_name=i_name, i_good_fb=i_good_fb, i_bad_fb=i_bad_fb, i_count=1)
                    db.session.add(new_illness)
                else:
                    illness.i_good_fb += i_good_fb
                    illness.i_bad_fb += i_bad_fb
                    illness.i_count += 1
                db.session.commit()
                return {'msg': '疾病统计更新成功', 'code': 1001}
        except Exception as e:
            db.session.rollback()
            return {'msg': f'失败：{str(e)}', 'code': 1000}


    def list_illness_operation(self):
        # 列出热门疾病操作，返回按计数降序排列的疾病列表
        try:
            i_lists = Illness_Model.query.order_by(desc(Illness_Model.i_count)).limit(10).all()
            i_list = [{'i_name': i.i_name, 'i_count': i.i_count, 'i_good_fb': i.i_good_fb, 'i_bad_fb': i.i_bad_fb} for i
                      in i_lists]
            return {'data': i_list, 'code': 1010}
        except Exception as e:
            return {'msg': f'无法获取疾病列表：{str(e)}', 'code': 1011}