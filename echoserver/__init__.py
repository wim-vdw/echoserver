from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return {
            'name': 'Wim Van den Wyngaert',
        }

    return app
