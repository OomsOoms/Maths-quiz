from database import database_manager

class User:
    def __init__(self):
        self.name = database_manager.check_username(input("Enter your username: "))
        self.score = 0
