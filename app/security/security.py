import os
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()


class Security:
    def __init__(self):
        pass

    ALGORITHM = os.getenv('ALGORITHM')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, password):
        return self.pwd_context.verify(password, self.JWT_SECRET_KEY)





