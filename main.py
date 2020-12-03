from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_swagger_ui import get_swaggerui_blueprint
from userApi.routes import userRoutes
import json

app = Flask(__name__)

with open('config.json', 'r') as file:
    config = json.load(file)

app.config['MONGO_URI'] = config[config['MODE']['MODE']]['MONGO_URL']
mongo = PyMongo(app)

app.register_blueprint(userRoutes.user_routes)

swaggerui_blueprint = get_swaggerui_blueprint(
    config[config['MODE']['MODE']]['SWAGGER_URL'],  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    config[config['MODE']['MODE']]['API_URL'],
    config={  # Swagger UI config overrides
        'app_name': "userApi"
    },
)
app.register_blueprint(swaggerui_blueprint)


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource not found ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(host=(config[config['MODE']['MODE']]['HOST']), port=(config[config['MODE']['MODE']]['PORT']),
            debug=(config[config['MODE']['MODE']]['DEBUG']))
