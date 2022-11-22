# chua cac tap tin, lop doi tuong


# dai dien cho bang anh xa xuong csdl
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
# moi quan he
from sqlalchemy.orm import relationship
from unicodedata import category, name

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
    # # thuc hien
    # with app.app_context():
    #     #tao bang
    #     db.create_all()
    #     # day len server
    #     db.session.commit()

    # with app.app_context():
    #     c1 = Category(name="Điện thoại Galaxy")
    #     c2 = Category(name='Đồng hồ')
    #     c3 = Category(name='Laptop')
    #
    #     db.session.add(c1)
    #     db.session.add(c2)
    #     db.session.add(c3)
    #
    #     db.session.commit()

    products = [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "images/p1.png",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image": "images/p2.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "images/p3.jpg",
        "category_id": 1
    }]

    # with app.app_context():
    #     for p in products:
    #         pro = Product(name=p['name'], price=p['price'], image=p['image'],
    #                       description=p['description'], category_id=p['category_id'])
    #         db.session.add(pro)
    #     db.session.commit()
