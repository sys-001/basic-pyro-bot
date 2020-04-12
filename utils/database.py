import typing
from .entities import *


# noinspection PyShadowingNames
class DatabaseManager:
    db = None

    def __init__(self, db: Database):
        self.db = db

    @db_session
    def get_user(self, id: int) -> typing.Optional[User]:
        try:
            return User.get(id=id)
        except ObjectNotFound:
            return None

    @db_session
    def save_user(self, id: int, is_admin: bool = False) -> User:
        user = self.get_user(id)
        if user is None:
            return User(id=id, is_admin=is_admin)
        user.is_admin = is_admin
        return user

    @db_session
    def get_admins(self) -> list:
        query = User.select(lambda u: u.is_admin)
        return select(u.id for u in query)[:]

    @db_session
    def get_chat(self, id: int) -> typing.Optional[Chat]:
        try:
            return Chat.get(id=id)
        except ObjectNotFound:
            return None

    @db_session
    def save_chat(self, id: int, is_authorized: bool = False) -> Chat:
        chat = self.get_chat(id)
        if chat is None:
            return Chat(id=id, is_authorized=is_authorized)
        chat.is_authorized = is_authorized
        return chat

    @db_session
    def get_authorized_chats(self) -> list:
        query = Chat.select(lambda c: c.is_authorized)
        return select(c.id for c in query)[:]
