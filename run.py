import os
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.root_path, 'resources\dictionary.db'),
    )
    print(os.path.join(app.root_path, 'resources\dictionary.db'))
    try:
        os.makedirs(app.root_path)
    except OSError:
        pass

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
