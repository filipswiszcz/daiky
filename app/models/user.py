class User:

    def __init__(self, email: str, password: str) -> None:
        self.__email = email
        self.__password = password

    def get_email(self) -> str:
        return self.__email
    
    def get_password(self) -> str:
        return self.__password