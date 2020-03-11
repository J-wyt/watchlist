from flask import Flask
from flask import escape
'''
用户输入的数据会包含恶意代码，所以不能直接作为响应返回，
需要使用 Flask 提供的 escape() 函数对 name 变量进行转义处理，
比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行
'''
from flask import url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return 'welcome to my watchlist'


@app.route('/user/<name>')
def user_page(name):
    return f'User {escape(name)}'


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'