import bcrypt

from src.data.protocols.encrypter import Encrypter


class BcryptAdapter(Encrypter):

    def encrypt(self, value: str) -> str:
        return bcrypt.hashpw(value.encode(), bcrypt.gensalt())
