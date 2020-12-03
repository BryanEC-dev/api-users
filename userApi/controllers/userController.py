from flask import jsonify

from userApi.repository import userRepository


def get_user():
    response = {}
    user = []

    try:
        list_user = userRepository.get_user()
        if list_user:
            for Users in list_user:
                user.append({
                    "_id": str(Users["_id"]),
                    "identification_card": Users["identification_card"],
                    "first_last_name": Users["first_last_name"],
                    "second_last_name": Users["second_last_name"],
                    "firs_name": Users["firs_name"],
                    "middle_name": Users["middle_name"],
                    "date_birth": Users["date_birth"],
                    "ubication": Users["ubication"],
                    "nationality": Users["nationality"],
                    "sex": Users["sex"],
                    "civil_state": Users["civil_state"]})
                response["status"] = "200"
                response["message"] = "successful "
                response["users"] = user
        else:
            response["status"] = "200"
            response["message"] = "No existen registros"
        return response
    except:
        response = jsonify({
            'message': 'Internal Error',
            'status': 500
        })
        response.status_code = 500
        return response


def get_user_identification(identification):
    response = {}

    try:
        information_user = userRepository.get_user_identification(identification)

        if information_user:
            user = {
                "_id": str(information_user["_id"]),
                "identification_card": information_user["identification_card"],
                "first_last_name": information_user["first_last_name"],
                "second_last_name": information_user["second_last_name"],
                "firs_name": information_user["firs_name"],
                "middle_name": information_user["middle_name"],
                "date_birth": information_user["date_birth"],
                "ubication": information_user["ubication"],
                "nationality": information_user["nationality"],
                "sex": information_user["sex"],
                "civil_state": information_user["civil_state"]
            }

            response["status"] = "200"
            response["message"] = "successful "
            response["users"] = user
        else:
            response["status"] = "200"
            response["message"] = "No existen registros"

        return response
    except:
        response = jsonify({
            'message': 'Internal Error',
            'status': 500
        })
        response.status_code = 500
        return response


