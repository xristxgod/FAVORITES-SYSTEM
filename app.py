from flask import Flask
from src import views
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.register_blueprint(views.app)

if __name__ == '__main__':
    app.run()
