from bottle import Bottle, run, route, static_file, redirect, template
app = Bottle()


@app.route('/static/<filename:path>')
def st(filename):
    return static_file(filename, root="static/")


@app.route('/json/<filename:re:.*\.json>')
def json_get(filepath):
    return static_file(filepath, root='json/', mimetype='application/json')


@app.route('/')
def go_home():
    redirect('/home')


@app.route('/<text>')
def hello(text="home"):
    return template("index", text=text)


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
