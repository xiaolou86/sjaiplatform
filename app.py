from flask import Flask
from models import db
import os
from routes import init_app

app = Flask(__name__)
app.config.from_object('config.Config')

# 初始化数据库
db.init_app(app)

# 初始化 API 路由
init_app(app)

@app.route('/')
def home():
    return "Welcome to the Management Platform"

# 运行应用
if __name__ == "__main__":
    with app.app_context():
        if not os.path.exists('database.db'):
            db.create_all()  # 创建数据库表
    app.run(debug=True, host='0.0.0.0', port=50080)

