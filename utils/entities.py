from pony.orm import *

db = Database()


class Chat(db.Entity):
    id = PrimaryKey(int, size=64)
    is_authorized = Optional(bool)


class User(db.Entity):
    id = PrimaryKey(int)
    is_admin = Optional(bool)


db.bind('sqlite', 'bot.db', create_db=True)
db.generate_mapping(create_tables=True)
