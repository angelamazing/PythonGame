"""
视图函数
@app.route('/hello')
def hello():
    return 'hello'

通过route装饰器，将一个url /hello 与 函数hello 关联在一起，我们称这个函数就是视图函数。
另外还有类视图
"""

from flask import Flask, request
from flask.views import View,MethodView

app = Flask(__name__)

"""
继承flask.views.View，必须实现dispatch_request方法以处理请求，下面是一个简单的示例
"""


class UserView(View):
    """
    继承flask.views.View
    """
    methods = ['GET']

    def dispatch_request(self):
        print(request.method)
        return 'not ok'


app.add_url_rule('/users', view_func=UserView.as_view('users'))


class UserView(MethodView):
    """
    View类里，如果一个资源支持多种请求方式，get，post,put,delete等等，
    那么你不得不在dispatch_request方法里根据request.method对他们进行区分，然后调用不同的处理方法进行响应，对各种请求的路由是由你自己完成的。
    而MethodView则帮你做好了路由，不同的请求，会被路由到不同的处理方法上
    """
    def get(self):
        return "收到get请求"

    def post(self):
        return '收到post请求'

app.add_url_rule('/books', view_func=UserView.as_view('books'))

if __name__ == '__main__':
    app.run(debug=True)
