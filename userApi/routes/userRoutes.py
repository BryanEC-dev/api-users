from flask import Blueprint
import json
from userApi.controllers import userController

user_routes = Blueprint('users', __name__)

with open('././config.json', 'r') as file:
    config = json.load(file)

globalPath = config[config["MODE"]["MODE"]]['GLOBAL_PATH']


@user_routes.route(globalPath + '/users', methods=["GET"])
def get_users():
    return userController.get_user()


@user_routes.route(globalPath + '/users/findByIdentificationCard/<identification>', methods=["GET"])
def get_users_identification(identification):
    return userController.get_user_identification(identification)
