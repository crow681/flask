from flask import Flask

app = Flask(__name__)


@app.route('/admin/<name>')
def hello_world(name):
    return '显示路由：{}'.format(name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f'编号{postID}'

@app.route('/rev/<float:revNo>')
def revsion(revNo):
    return f'版本号{revNo}'

if __name__ == '__main__':
    app.run()
