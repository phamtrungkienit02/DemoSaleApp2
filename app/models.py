# chua cac tap tin, lop doi tuong


# dai dien cho bang anh xa xuong csdl
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
# moi quan he
from sqlalchemy.orm import relationship
#
from app import db, app

# tuong tac voi ngay gio
from datetime import datetime


# lop chung
class BaseModel(db.Model):
    # lenh nay nham khong tao bang trong csdl
    __abstract__ = True
    # kieu int, khoa chinh, tu dong tang
    id = Column(Integer, primary_key=True, autoincrement=True)


# ke thua lai tu lop BaseModel
# lop dai dien cho bang du lieu duoi csdl tao ra bang category
class Category(BaseModel):
    # chi dinh ten bang du lieu
    __tablename__ = 'category'
    # bat buoc phai co ten
    name = Column(String(20), nullable=False)
    # moi quan he, 1 danh muc co nhieu san pham
    # backref='category', doi tuong cua product them category
    # dai dien cho category ma san pham dang phu thuoc vao
    # lazy lay dung thong tin danh muc, khong keu thi khong lam, tang hieu nang
    # lazy = 'subquery' khong join, nhung lay duoi dang cau truy van con
    products = relationship('Product', backref='category', lazy=False)

    # chuoi dai dien doi tuong
    def __str__(self):
        return self.name


# lop dai dien cho bang san pham
class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.now())
    # thiet lap khoa ngoai, ten lop duoc dat ('bo vao day')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


# thuc thi chay csdl, anh xa xuong chay csdl
if __name__ == '__main__':
    # thuc hien
    with app.app_context():
        db.create_all()

        # day len server
        db.session.commit()
