from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# 防止循环引用
db = SQLAlchemy()
mail = Mail()
