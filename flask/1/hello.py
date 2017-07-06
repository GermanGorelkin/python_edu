from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    header_info = ''
    for k, v in request.headers.items():
        header_info += '<p>{0}: {1}</p>'.format(k, v)
    return header_info


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}<h1>'.format(name)


@app.route('/set-cookie')
def set_cookie():
    response = make_response('<h1>body</h1>')
    response.set_cookie('answer', '42')
    response.status_code = 200
    return response


@app.route('/redir/<rtype>')
def redirect(rtype):
    if rtype == '1':
        response = make_response('')
        response.headers['Location'] = 'http://127.0.0.1:5000/'
        response.status_code = 302
        return response
    elif rtype == '2':
        return redirect('http://www.example.com')
    else:
        return ''


if __name__ == '__main__':
    app.run(debug=True)
