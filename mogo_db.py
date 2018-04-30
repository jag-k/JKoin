from pprint import pprint
from bson.dbref import DBRef
from datetime import datetime
from hashlib import md5 as __md__
import pymongo, requests, sys, time
sys.setrecursionlimit(60)

COEFF = 4


client = pymongo.MongoClient()

coins = client.jkoin.coins  # type: pymongo.collection.Collection
log = client.jkoin.log  # type: pymongo.collection.Collection


def __clear_db__():
    log.remove()
    coins.remove()


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
                        "time": time.time()
                    }
                )
                return {"status": True, "user": get_user(user)}
            return {"status": "IDB", "user": get_user(user)}
    return {"status": False, "user": (get_user(text.split('-')[0]) if len(text.split('-')) == 2 else {})}


def get_count_coins(user_id):
    user = get_user(user_id)
    return {"count": coins.find({"user": user.get('id', -1)}).count(), "user": user}


def get_top_users(count=10):
        top = coins.aggregate([
            {
                "$group": {
                    "_id": "$user",
                    "count": {
                        "$sum": 1
                    },
                }
            },
            {
                "$sort": {
                    "count": -1
                }
            }
        ])
        return list(map(lambda x: {"user": get_user(x['_id']), "count": x['count']}, top))[:count]


def transfer_coins(from_user, to_user, count=1):
    err = False
    fr, to = get_user(from_user), get_user(to_user)
    transfer_count = 0
    if fr == to:
        err = "You can't transfer JKoin to yourself!"

    elif 0 >= get_count_coins(fr['id'])['count'] < coins:
        err = "Insufficient JKoin to complete the transfer"

    elif fr and to:
        coins_count = get_count_coins(fr['id'])['count']
        while coins_count and count:
            count -= 1
            coins_count -= 1
            transfer_count += 1
            id = coins.find_one({'user': fr['id']})["_id"]
            coins.replace_one({'_id': id}, {'user': to['id']})

            log.insert_one(
                {
                    "coin": DBRef("coins", id),
                    "user": fr['id'],
                    "to": to['id'],
                    "time": time.time()
                }
            )
    else:
        err = "IDs is incorrect! Please, try again."

    return {"transfer": transfer_count,
            "err": err,
            "from": {"user": fr, "balance": get_count_coins(fr['id'])['count']},
            "to": {"user": to, "balance": get_count_coins(to['id'])['count']}}


if __name__ == '__main__':
    __clear_db__()
