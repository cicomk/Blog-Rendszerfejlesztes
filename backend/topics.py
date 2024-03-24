topics = [
    { "id" : "1", "name" : "Cím 1", "type_id" : "1", "description" : "Leírás"},
    { "id" : "2", "name" : "Cím 2", "type_id" : "1", "description" : "Leírás"},
    { "id" : "3", "name" : "Cím 3", "type_id" : "2", "description" : "Leírás"},
    { "id" : "4", "name" : "Cím 4", "type_id" : "3", "description" : "Leírás"},
    { "id" : "5", "name" : "Cím 5", "type_id" : "4", "description" : "Leírás"}

]

topic_types = [
    {"id" : "1", "name" : "Utazás"},
    {"id" : "2", "name" : "Gasztronómia"},
    {"id" : "3", "name" : "Könyv"},
    {"id" : "4", "name" : "Film"},
    {"id" : "5", "name" : "Lifecare"}
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
    
    def getType(self, type_id=""):
        typeName = ""
        for t in topic_types:
            if str(type_id) == t["id"]:
                typeName = t["name"]
        return str(typeName)
    
    def getTypes(self):
        return topic_types
