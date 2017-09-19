from uuid import uuid4
class User(object):
    def __init__(self, username, password, confirm_password, user_id=None):
        self.user_id = uuid4() if user_id is None else user_id
        