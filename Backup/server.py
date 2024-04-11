from flask import Flask, jsonify, request
from flask_cors import CORS

topics = [
    { "id" : "1", "name" : "Cím 1", "type_id" : "Utazás", "description" : "Leírás"},
    { "id" : "2", "name" : "Cím 2", "type_id" : "Utazás", "description" : "Leírás"},
    { "id" : "3", "name" : "Cím 3", "type_id" : "Gasztronómia", "description" : "Leírás"},
    { "id" : "4", "name" : "Cím 4", "type_id" : "Könyv", "description" : "Leírás"},
    { "id" : "5", "name" : "Cím 5", "type_id" : "Film", "description" : "Leírás"}

]

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def api():
    return "Üdvözlet"

@app.route('/append',methods=['POST'])
def append():
    new_topic = request.get_json()
    new_topic['id'] = str(len(topics)+1)
    topics.append(new_topic)
    return "ok"

@app.route('/topics', methods=['GET'])
def get_topics():
    topic_id = request.args.get('param')
    if topic_id == '':
        return jsonify(topics)
    else:
        temp = []
        for i in topics:
            if i["type_id"] == topic_id:
                temp.append(i)
    return jsonify(temp)


if __name__ == '__main__':
    app.run(debug=False)
