#xai file html trong template
from flask import render_template, request
#app dau tien la thu muc
from app import app
#lay het cac ham trong utils
import utils

#duong dan trang chu
@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html', categories=cates)
#tao ra duong dan qua trang moi
@app.route("/products")
def product_list():
    # lay id request cua san pham
    cate_id = request.args.get("category_id")
    # lay kw, from_price, tp_price
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")
    #load danh muc products len va tra ra ngoai, neu cate_id != None thi lay request
    products = utils.load_products(cate_id=cate_id, kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)


    return render_template('products.html', products=products)

#Hien mo ta san pham
@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)
    return render_template('product_detail.html', product=product)


if __name__ == '__main__':
    #dang phat trien thi bat len de hien loi, trien khai len server thi tat di
    app.run(debug=True)