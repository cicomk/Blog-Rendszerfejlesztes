topics = [
    { "id" : "1", "name" : "Cím 1", "type_id" : "Utazás", "description" : "Leírás"},
    { "id" : "2", "name" : "Cím 2", "type_id" : "Utazás", "description" : "Leírás"},
    { "id" : "3", "name" : "Cím 3", "type_id" : "Gasztronómia", "description" : "Leírás"},
    { "id" : "4", "name" : "Cím 4", "type_id" : "Könyv", "description" : "Leírás"},
    { "id" : "5", "name" : "Cím 5", "type_id" : "Film", "description" : "Leírás"}

]

class Topics:
    def __init__(self):
        print("Topics kapcsolva")

    def getTopics(self, topic_id=""):
        if topic_id == '':
            return topics
        else:
            temp = []
            for i in topics:
                if i["type_id"] == topic_id:
                    temp.append(i)
        return temp
    
    def addTopics(self,new_topic):
        new_topic['id'] = str(len(topics)+1)
        topics.append(new_topic)
        return "ok"