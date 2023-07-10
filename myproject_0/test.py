from flask import Flask

# Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줌
app = Flask(__name__)

@app.route('/')
def hello():
    return f'hello, {__name__}'

@app.route('/mirim')
def hello_mirim():
    return f'hello, mirim'

@app.route('/jjanggu')
def hello_jjanggu():
    return f'<b> JJANGGU </b>'