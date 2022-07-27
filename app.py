from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


# @app.route('/admin')
# def hello_admin():
#     return 'hello admin'
#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return f'hello{guest}'
#
# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':  # url_for函数构造特定的URL
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest',guest=name))

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(port=5555, debug=True)
