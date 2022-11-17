# file khoi dong package

from urllib.parse import quote
from flask import Flask
# database
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# chuoi ket noi den csdl mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4' % quote('Admin@123')
# #bat de khi bo sung thi no thong bao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)
