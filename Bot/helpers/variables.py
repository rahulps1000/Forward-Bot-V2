from Bot.database.variables import db_variables
from Bot.config import Config


def variable_property(name, default=None):
    def getter(self):
        return self.db.get_variable(self.user_id, name) or default

    def setter(self, value):
        self.db.add_or_update_variable(self.user_id, name, value)

    return property(getter, setter)


class Variables:
    def __init__(self, user_id):
        self.db = db_variables
        if Config.MULTI_USER_MODE:
            self.user_id = user_id
        else:
            self.user_id = 1

    status = variable_property('status', default='stopped')
    time = variable_property('time')
    from_chat = variable_property('from_chat')
    to_chat = variable_property('to_chat')
    from_msg = variable_property('from_msg', default=0)
    to_msg = variable_property('to_msg', default=0)
    last_msg = variable_property('last', default=0)
    all = variable_property('all')
    photo = variable_property('photo')
    video = variable_property('video')
    audio = variable_property('audio')
    document = variable_property('document')
    text = variable_property('text')
    tag = variable_property('tag')
    count = variable_property('count', default=0)

    def reset_all(self):
        self.status = 'stopped'
        self.time = None
        self.from_chat = None
        self.to_chat = None
        self.from_msg = 0
        self.to_msg = 0
        self.last_msg = 0
        self.all = None
        self.photo = None
        self.video = None
        self.audio = None
        self.document = None
        self.text = None
        self.tag = None
        self.count = 0