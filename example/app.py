from flask import Flask, render_template

from flask_mix import Mix

mix = Mix()


def create_app():
    """
    Create a Flask application.

    :return: Flask app
    """
    app = Flask(__name__, static_url_path='', static_folder='static')

    params = {
        'DEBUG': True,
    }

    app.config.update(params)
    mix.init_app(app)

    @app.route('/')
    def index():
        output = render_template('index.html')
        return output, 200

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
