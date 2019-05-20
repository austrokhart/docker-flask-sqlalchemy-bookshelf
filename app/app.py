
from flask import Flask

from database import flask_connect
from book.router import router


app = Flask(__name__)
flask_connect(app)


app.register_blueprint(router, url_prefix="/book/")


if __name__ == "__main__":
    app.run()
