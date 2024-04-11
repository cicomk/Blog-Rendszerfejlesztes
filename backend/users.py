users = [
    {"id":"1", "username":"randuser","name":"RandomUser","password":""},
    {"id":"2", "username":"EricCartman","name":"Eric Cartman","password":""},
    {"id":"3", "username":"LocalUser","name":"LocalUser","password":""}
]

class User:
    def getNameById(self,id):
        for i in users:
            if i["id"] == id:
                user = i["name"]
                return user