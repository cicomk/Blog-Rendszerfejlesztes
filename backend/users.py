from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

try:

    engine = create_engine('mysql+mysqlconnector://root:@localhost/beadando')
    Session = sessionmaker(bind=engine)
    conn = engine.connect()
    print("Sikeresen csatlakoztál az adatbázishoz!")
except Exception as e:
    print("Nem sikerült csatlakozni az adatbázishoz. A hiba oka:")
    print(e)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    name = Column(String(255))
    password = Column(String(255))
    admin = Column(Integer)
    

class UsersManager:
    def __init__(self):
        self.session = Session()

    def add_user(self, user_data):
        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        print(f"User {new_user.name} added successfully.")

    def getNameById(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            return user.name
        else:
            return None

    def getUserID(self, username, password):
        user = self.session.query(User).filter_by(username=username, password=password).first()
        if user:
            return user.id
        else:
            return -1

    def auth(self,data,jsonify):
        username = data['username']
        password = data['password']
        return str(self.getUserID(username,password))
    
    def role(self, uid):
        role = self.session.query(User).filter_by(id = uid).first()
        if str(role.admin) == "1":
           return "1"
        else:
            return "0"


    


    
    


users_data = [
    {"id": 1, "username": "randuser", "name": "RandomUser", "password": ""},
    {"id": 2, "username": "EricCartman", "name": "Eric Cartman", "password": ""},
    {"id": 3, "username": "LocalUser", "name": "LocalUser", "password": ""}
]

# users_manager = UsersManager('mysql+mysqlconnector://root:@localhost/beadando')
# for user_data in users_data:
#     users_manager.add_user(user_data)

# user_id = 2
# user_name = Session.getNameById(user_id)
# print(f"Name of user with ID {user_id}: {user_name}")