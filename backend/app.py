from flask import Flask
from flask_cors import CORS
from routes.main_routes import routes

app = Flask(__name__)

# CORS
CORS(app)

# Init db
app.register_blueprint(routes)