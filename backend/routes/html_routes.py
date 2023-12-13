from flask import Blueprint, render_template

import os

html_routes = Blueprint('html_routes', __name__)

# Home page
@html_routes.route('/')
def home():
    qr = os.path.isfile('static/qrcode.png') # True or False
    return render_template('index.html', qr=qr)

@html_routes.route('/eda')
def eda():
    return render_template('report.html')