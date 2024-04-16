# topics = [
#     { "id" : "1", "name" : "Cím 1", "type_id" : "1", "description" : "Leírás"},
#     { "id" : "2", "name" : "Cím 2", "type_id" : "1", "description" : "Leírás"},
#     { "id" : "3", "name" : "Cím 3", "type_id" : "2", "description" : "Leírás"},
#     { "id" : "4", "name" : "Cím 4", "type_id" : "3", "description" : "Leírás"},
#     { "id" : "5", "name" : "Cím 5", "type_id" : "4", "description" : "Leírás"}
# ]

# topic_types = [
#     {"id" : "1", "name" : "Utazás"},
#     {"id" : "2", "name" : "Gasztronómia"},
#     {"id" : "3", "name" : "Könyv"},
#     {"id" : "4", "name" : "Film"},
#     {"id" : "5", "name" : "Lifecare"}
# ]

# class Topics:
#     def __init__(self):
#         print("Topics kapcsolva")

#     def getTopics(self, topic_id=""):
#         if topic_id == '':
#             return topics
#         else:
#             temp = []
#             for i in topics:
#                 if i["type_id"] == topic_id:
#                     temp.append(i)
#         return temp
    
#     def addTopics(self,new_topic):
#         new_topic['id'] = str(len(topics)+1)
#         topics.append(new_topic)
#         return "ok"
    
#     def getType(self, type_id=""):
#         typeName = ""
#         for t in topic_types:
#             if str(type_id) == t["id"]:
#                 typeName = t["name"]
#         return str(typeName)
    
#     def getTypes(self):
#         return topic_types
    
#     def getOne(self,id):
#         for i in topics:
#             if i["id"] == id:
#                 return i
#         print("Nincs talalat")
#         return "404"


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import _mysql_connector
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()

class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer)
    description = Column(String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class TopicType(Base):
    __tablename__ = 'topic_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

try:

    engine = create_engine('mysql+mysqlconnector://root:@localhost/beadando')
    Session = sessionmaker(bind=engine)
    conn = engine.connect()
    print("Sikeresen csatlakoztál az adatbázishoz!")
except Exception as e:
    print("Nem sikerült csatlakozni az adatbázishoz. A hiba oka:")
    print(e)


class Topics:
    def __init__(self):
        self.session = Session()

    def getTopics(self, topic_id=""):
        try:
            if topic_id == '':
                try:
                    return [topic.to_dict() for topic in self.session.query(Topic).all()]
                except SQLAlchemyError:
                    self.session.rollback()
                    raise
            else:
                return [topic.to_dict() for topic in self.session.query(Topic).filter(Topic.type_id == topic_id).all()]
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def addTopics(self,new_topic):
        topic = Topic(**new_topic)
        self.session.add(topic)
        self.session.commit()
        return "ok"

    def getType(self, type_id=""):
        try:
            type = self.session.query(TopicType).get(type_id)
            return type.name if type else ""
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def getTypes(self):
        try:
            return [type.to_dict() for type in self.session.query(TopicType).all()]
        except SQLAlchemyError:
            self.session.rollback()
            raise


    def getOne(self,id):
        topic = self.session.query(Topic).get(id)
        if topic:
            return topic
        else:
            print("Nincs talalat")
            return "404"
