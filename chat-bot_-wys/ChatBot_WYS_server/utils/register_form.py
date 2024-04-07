import wtforms
from wtforms.validators import Email, Length
from models.user import Mail_Model


class RegisterForm(wtforms.Form):
    u_email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    u_captcha = wtforms.StringField(validators=[Length(min=6, max=6, message="验证码格式错误！")])

    def validate_u_captcha(self, field):
        captcha = field.data
        email = self.u_email.data
        # 查询数据库中是否存在匹配的邮箱和验证码记录
        captcha_model = Mail_Model.query.filter_by(u_email=email, u_captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="验证码错误")
