comments = [
    {"id" : "1", "user_id":"1","topic_id":"1","body":"Nagyon jó","timestamp":"2024-03-29 12:20:07"},
    {"id" : "2", "user_id":"1","topic_id":"2","body":"Megesik","timestamp":"2024-02-18 12:20:07"},
    {"id" : "3", "user_id":"2","topic_id":"1","body":"Oszva és környéke","timestamp":"2024-03-16 12:20:07"},
    {"id" : "4", "user_id":"2","topic_id":"1","body":"Ez miez?","timestamp":"2024-03-21 12:20:07"}
]

from datetime import datetime



class Comments:
        

    def getComments(self, topic_id):
        temp = []
        for i in comments:
            if i["topic_id"] == topic_id:
                temp.append(i)
        temp = sorted(temp, key=lambda x: x['timestamp'],reverse=True)
        return temp

    def newComment(self, new_comment):
        new_comment['id'] = str(len(comments)+1)
        timestamp = datetime.now()
        timenow = str(timestamp).split(".")[0]
        new_comment['timestamp'] = timenow
        comments.append(new_comment)
        print(new_comment)
        return "OK"
    
    def sumCommentsByTopic(self, topic_id):
        return str(len(self.getComments(topic_id)))