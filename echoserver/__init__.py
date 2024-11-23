from flask import Flask


def create_app():
    app = Flask(__name__)
    from echoserver.echoserver import echoserver_bp
    app.register_blueprint(echoserver_bp)

    return app
