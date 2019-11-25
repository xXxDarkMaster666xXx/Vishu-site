from flask import Flask, render_template, redirect, flash, request
from budgetapp.admin.routes import admin
from budgetapp.main.routes import main
from budgetapp.database.models import db
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__, instance_relative_config=True,
                      template_folder='templates') 

app.config.from_object(Config)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

db.init_app(app) 
migrate = Migrate(app, db)

login = LoginManager(app)
LoginManager.login_view = 'login'