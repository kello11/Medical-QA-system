from flask import Flask
from routes.user import user
from routes.admin import admin
from routes.index import index
from routes.feedback import feedback
from routes.hotissue import hotissue
import config
from flask_migrate import Migrate
from exts import db, mail
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(config)  # 绑定配置文件

# 注册蓝图（Blueprint）模块
app.register_blueprint(feedback, url_prefix='/feedback')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(hotissue, url_prefix='/hotissue')

CORS(app)  # 初始化邮件扩展

db.init_app(app)  # 初始化邮件扩展
mail.init_app(app)  # 初始化邮件扩展

# 定义根路由，用于健康检查
migrate = Migrate(app, db)

# 定义根路由，用于健康检查
@app.route('/')
def ping():
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
