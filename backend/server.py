from flask import Flask, jsonify, request
from flask_cors import CORS

from topics import *

topics = Topics()

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def api():
    return "Üdvözlet"

@app.route('/topics/append',methods=['POST'])
def append():
    new_topic = request.get_json()
    return topics.addTopics(new_topic)

@app.route('/topics', methods=['GET'])
def get_topics():
    topic_id = request.args.get('param')
    return topics.getTopics(topic_id)

@app.route('/topics/type_id', methods=['GET'])
def get_type():
    type_id = request.args.get('type_id')
    vissza = str()
    print(vissza)
    return topics.getType(type_id)

@app.route('/topics/types', methods=['GET'])
def get_types():
    return topics.getTypes()

if __name__ == '__main__':
    app.run(debug=False)
