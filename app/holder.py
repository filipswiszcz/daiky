from .models import *

class Memory:

    def __init__(self) -> None:
        self.__users = []

    def get_user(self, email: str) -> object:
        for user in self.__users:
            if user.get_email() == email:
                return user
        return None

    def add_user(self, user):
        self.__users.append(user)