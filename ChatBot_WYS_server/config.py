
# 数据库类型 ip  port root  密码
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'wys_project'
USERNAME = 'root'
PASSWORD = 'lkc021217'
DB_URI   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '1210853522@qq.com'
MAIL_PASSWORD = 'vdiabwwpjpcthgad'
MAIL_DEFAULT_SENDER = '1210853522@qq.com'

SECRET_KEY = '7e648f8ca263a17f3a0ab4a9f3aa27b183b9c82ebea8941c'  # 密钥

#  连接到问答系统的url base
base_url_1 = "http://10.210.98.56:60064"
base_url_2 = "http://10.210.98.56:60065"
