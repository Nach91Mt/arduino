from flask import Flask


applicatio = Flask(__name__)

@application.route('/')

def index():
    return 'hellow word'
    
if __name__ =='__main__':
    application.run(host="0.0.0.0.",port=80,debug True)
