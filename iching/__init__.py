import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def project_root():
        return f'Try ths instead: <a href="/web/4096/1" target="_blank">click here</a>'

    # apply the blueprints to the app
    from iching import flask_api, flask_web
    app.register_blueprint(flask_api.bp)
    app.register_blueprint(flask_web.bp)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, port=80)

    return app

