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

@app.route('/wallet', method=["GET", "POST"])
def wallet(page="Wallet"):
    params = request.params  # type: bottle.FormsDict
    print(params.dict)
    return template("main", text=page.capitalize(), hashes=params.dict.get("hashes", [[]])[0])


@app.route('/', method=["GET", "POST"])
def hello(page='Home'):

    params = request.params  # type: bottle.FormsDict
    hashes = dict((i, create_coin(i)) for i in filter(lambda x: x,
                                                      map(lambda x: x.strip(),
                                                          params.getunicode("hashes", "").strip().split('\n'))))
    # pprint(hashes)

    return template("main", text=page.capitalize(), hashes=hashes, ph=params.getunicode("hashes", "").strip())


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
