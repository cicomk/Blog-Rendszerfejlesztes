from sqlalchemy import createengine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarativebase

Base = declarative_base()

class User(Base):
    __tablename = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    name = Column(String(255))
    password = Column(String(255))

class UsersManager:
    def init(self, connection_string):
        self.engine = create_engine(connection_string)
        Session = sessionmaker(bind=self.engine)
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


users_data = [
    {"id": 1, "username": "randuser", "name": "RandomUser", "password": ""},
    {"id": 2, "username": "EricCartman", "name": "Eric Cartman", "password": ""},
    {"id": 3, "username": "LocalUser", "name": "LocalUser", "password": ""}
]


users_manager = UsersManager('mysql+mysqlconnector://root:@localhost/beadando')
for user_data in users_data:
    users_manager.add_user(user_data)


user_id = 2
user_name = users_manager.getNameById(user_id)
print(f"Name of user with ID {user_id}: {user_name}")