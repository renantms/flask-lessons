from flask import Flask
app = Flask(__name__)

@app.route('/<int:number>', methods=['GET'])
def hello(number):
    return 'Hello World. {}'.format(number)

if __name__ == '__main__':
    app.run()