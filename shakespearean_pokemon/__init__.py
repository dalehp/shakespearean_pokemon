import json

from flask import Flask


EXAMPLE_RESPONSE = {
    'name': "charizard",
    'description': "pokemon description",
}

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return json.dumps(EXAMPLE_RESPONSE)

    return app