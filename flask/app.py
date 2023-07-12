from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return 'get'
    if request.method == 'POST':
        return 'post'

@app.route('/book/<name>/author')
def author(name):
    return name


# 转换器为int
@app.route('/book/<int:id>/price')
def price(id):
    return str(id)


# 转换器为float
@app.route('/book/price-ge/<float:price>')
def books_by_price(price):
    return str(price)


# 转换器为path
@app.route('/book/<path:book_info>')
def books_by_path(book_info):
    return book_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)