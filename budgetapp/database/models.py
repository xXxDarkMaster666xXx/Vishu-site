from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=True)
    link = db.Column(db.String(800), index=True, unique=True)
    price = db.Column(db.Integer)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'))
    pr_brand = db.relationship('brands', backref='product', lazy='joined')
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    pr_category = db.relationship('categories', backref='product', lazy='joined')
    sock_id = db.Column(db.Integer, db.ForeignKey('socket.sock_id'), nullable = True)
    pr_socket = db.relationship('socket', backref='product', lazy='joined')
    watt_id = db.Column(db.Integer, db.ForeignKey('wattage.watt_id'), nullable = True)
    pr_watts = db.relationship('wattage', backref='product', lazy='joined')
    storage_id = db.Column(db.Integer, db.ForeignKey('storage.storage_id'), nullable = True)
    pr_storage = db.relationship('storage', backref='product', lazy='joined')
    kb_id = db.Column(db.Integer, db.ForeignKey('keyboard.kb_id'), nullable = True)
    pr_kb = db.relationship('keyboard', backref='product', lazy='joined')

class brands(db.Model):
    brand_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(50), index=True, unique=True)

    def __init__(self, brand_name):
        self.brand_name = brand_name

class categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), index=True, unique=True)

class socket(db.Model):
    sock_id = db.Column(db.Integer, primary_key=True)
    socket_type = db.Column(db.String(20), index=True, unique=True)

class wattage(db.Model):
    watt_id = db.Column(db.Integer, primary_key=True)
    watts = db.Column(db.Integer, index=True, unique=True)

class storage(db.Model):
    storage_id = db.Column(db.Integer, primary_key=True)
    storage_type = db.Column(db.String(10), index=True, unique=True)
    storage_size = db.Column(db.Integer, index=True, unique=True)

class keyboard(db.Model):
    kb_id = db.Column(db.Integer, primary_key=True)
    is_mechanical = db.Column(db.String(5), index=True, unique=True)