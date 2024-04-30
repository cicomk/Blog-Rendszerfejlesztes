comments = [
    {"id" : "1", "user_id":"1","topic_id":"1","body":"Nagyon jó","timestamp":"2024-03-29 12:20:07"},
    {"id" : "2", "user_id":"1","topic_id":"2","body":"Megesik","timestamp":"2024-02-18 12:20:07"},
    {"id" : "3", "user_id":"2","topic_id":"1","body":"Oszva és környéke","timestamp":"2024-03-16 12:20:07"},
    {"id" : "4", "user_id":"2","topic_id":"1","body":"Ez miez?","timestamp":"2024-03-21 12:20:07"}
]

from datetime import datetime

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import _mysql_connector
from sqlalchemy.exc import SQLAlchemyError

try:

    engine = create_engine('mysql+mysqlconnector://root:@localhost/beadando')
    Session = sessionmaker(bind=engine)
    conn = engine.connect()
    print("Sikeresen csatlakoztál az adatbázishoz!")
except Exception as e:
    print("Nem sikerült csatlakozni az adatbázishoz. A hiba oka:")
    print(e)

Base = declarative_base()

class CommentModel(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    topic_id = Column(Integer)
    body = Column(String)
    timestamp = Column(String)

    def __init__(self, user_id, topic_id, body):
        self.user_id = user_id
        self.topic_id = topic_id
        self.body = body
        self.timestamp = datetime.now()

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Comments:
    def __init__(self):
        self.session = Session()    

    def getComments(self, topic_id):
        try:
            comment_objects = self.session.query(CommentModel).filter_by(topic_id=topic_id).order_by(CommentModel.timestamp.desc()).all()
            comments = [comment.to_dict() for comment in comment_objects]
            self.session.close()
            return comments
        except Exception:
            self.session.rollback()
            raise


    def newComment(self, new_comment):
        new_comment = CommentModel(user_id=new_comment['user_id'], topic_id=new_comment['topic_id'], body=new_comment['body'])
        self.session.add(new_comment)
        self.session.commit()
        print(new_comment.to_dict())
        self.session.close()
        return "OK"
    
    def sumCommentsByTopic(self, topic_id):
        return str(len(self.getComments(topic_id)))