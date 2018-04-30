from bottle import Bottle, run, route, static_file, redirect, template, request
import bottle
from mogo_db import *
app = Bottle()


@app.route('/static/<filename:path>')
def st(filename):
    return static_file(filename, root="static/")


# @app.error(404)
# def err(*args, **kwargs):
#     print(args, kwargs)
#     return template("main", text="404")

@app.route('/transfer')
def transfer(page="Transfer"):
    params = request.params  # type: bottle.FormsDict
    from_user = params.getunicode("from", "").strip()
    to_user = params.getunicode("to", "").strip()
    count = params.getunicode("count", "").strip()
    count = count if str(count).isdigit() else 1
    res = transfer_coins(from_user, to_user, int(count)) if all((from_user, to_user, int(count))) else {}
    return template("main", text=page.capitalize(), res=res)


@app.route('/wallet')
def wallet(page="Wallet"):
    params = request.params  # type: bottle.FormsDict
    count = get_count_coins(params.getunicode("id", "").strip())
    count['count'] = -1 if not params.getunicode("id", "") else count['count']
    return template("main", text=page.capitalize(), count=count)


@app.route('/top')
def top(page="Top"):
    params = request.params.getunicode('count', 10)
    count = int(params) if str(params).isdigit() else 10
    top_list = get_top_users(count)
    return template("main", text=page.capitalize(), top=top_list, count=count)


@app.route('/')
def hello(page='Home'):

    params = request.params  # type: bottle.FormsDict
    hashes = dict((i, create_coin(i)) for i in filter(lambda x: x,
                                                      map(lambda x: x.strip(),
                                                          params.getunicode("hashes", "").strip().split('\n'))))
    # pprint(hashes)

    return template("main", text=page.capitalize(), hashes=hashes, ph=params.getunicode("hashes", "").strip(),
                    coef=COEFF)


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
