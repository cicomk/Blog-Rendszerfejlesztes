from flask import Flask, jsonify, request
from flask_cors import CORS

from topics import *
from comments import *


topics = Topics()
comments = Comments()


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

@app.route('/topics/', methods=['GET'])
def get_oneTopic():
    topic_id = request.args.get('topic_id')
    return topics.getOne(topic_id)


#Comments:
@app.route('/comment', methods=['GET'])
def getComments():
    topic_id = request.args.get('topic_id')
    return comments.getComments(topic_id)

@app.route('/comment/append', methods=['POST'])
def appendComment():
    new_commend = request.get_json()
    print(new_commend)
    return comments.newComment(new_commend)

@app.route('/comment/sum', methods=['GET'])
def sumComments():
    topic_id = request.args.get('topic_id')
    return comments.sumCommentsByTopic(topic_id)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
