from pprint import pprint
from datetime import datetime
from hashlib import md5 as __md__
import pymongo, requests, sys, time
sys.setrecursionlimit(60)

COEFF = 4


client = pymongo.MongoClient()

coins = client.jkoin.coins  # type: pymongo.collection.Collection
log = client.jkoin.log  # type: pymongo.collection.Collection


def __clear_db__():
    coins.delete_many({"user": "$user"})
    log.delete_many({"user": "$user"})


def md5(string, encoding="utf-8"):
    return str(__md__(str(string).encode(encoding)).hexdigest())


def err_recursion(return_value=None):
    def err_decorate(func):
        def err(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except RecursionError:
                return return_value
        return err
    return err_decorate


@err_recursion(return_value={})
def get_user(id, name_case="nom"):
    url = "https://api.vk.com/method/users.get"
    params = {
        "name_case": name_case,
        "user_ids": id,
        'v': 5.74
    }
    try:
        user = requests.get(url, params).json()
    except Exception as err:
        return get_user(id, name_case)
    if 'error' in user:
        return {}
    try:
        user = user['response'][0]  # type: dict
    except IndexError:
        return {}

    return {} if user.get('deactivated') else user


def create_coin(text: str):
    if len(text.split('-')) == 2 and get_user(text.split('-')[0]):
        user = text.split('-')[0]
        if md5(text)[:COEFF] == md5(user)[:COEFF]:
            if not coins.find({"string": text}).count():
                coins.insert_one(
                    {
                        "string": text,
                        "user": get_user(user)['id'],
                        "datetime": datetime.utcnow(),
                        "time": time.time()
                    }
                )
            return {"status": True, "user": get_user(user)}
    return {"status": False, "user": (get_user(text.split('-')[0]) if len(text.split('-')) == 2 else {})}


def get_count_coins(user_id):
    user = get_user(user_id)
    return {"count": coins.find({"user": user.get('id', -1)}).count(), "user": user}


if __name__ == '__main__':
    print(create_coin("id1-OdKmnRPbNr"))
    for i in coins.find():
        pprint(i)
    print(get_count_coins("id1"))
    print(get_count_coins("jag_k58"))
    print(get_count_coins("2131g13g44tc3"))
