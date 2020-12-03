def get_user() -> object:
    from main import mongo
    user_collection = mongo.db.users
    list_user = user_collection.find()
    return list_user


def get_user_identification(identification):
    from main import mongo
    user_collection = mongo.db.users
    user_information = user_collection.find_one({"identification_card": identification})
    print(user_information)
    return user_information
