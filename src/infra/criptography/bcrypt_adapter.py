import bcrypt

from src.data.protocols.encrypter import Encrypter


class BcryptAdapter(Encrypter):

    def __init__(self, salt: int):
        self.salt = salt

    def encrypt(self, value: str) -> str:
        return bcrypt.hashpw(value.encode(), self.salt)
