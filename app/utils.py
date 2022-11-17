# tap tin chuyen tuong tac voi du lieu
# them os khi dan duong dan tuyet doi
import json, os

from app import app

# file doc chung
def read_json(path):
    # f = open(path, "")
    # data = json.load(f)
    # f.close()
    # return data
# su dung khi co dong tap tin
    with open(path, "r") as f:
        return json.load(f)

def load_categories():
    #duong dan tuong doi, chi hoat dong khi o cung package, ngang cap
    #return read_json('data/categories.json')
    #bien app
    return read_json(os.path.join(app.root_path, 'data/categories.json'))
def load_products(cate_id=None, kw=None, from_price=None, to_price=None):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))
    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    if from_price:
        products = [p for p in products if p['price'] >= float(from_price)]
    if to_price:
        products = [p for p in products if p['price'] <= float(to_price)]
    return products

def get_product_by_id(product_id):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))
    for p in products:
        if p['id'] == product_id:
            return p
    # khong co san pham, trong Python mac dinh
    # return None