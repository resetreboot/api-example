from .entity import Entity

class User(Entity):
    def __init__(self, *args, **kwargs):
        self.email = kwargs['email']
        self.password = kwargs['password']
        self.uuid = kwargs['uuid']
        # This is missing, so we cannot log in
        self.enabled = kwargs['enabled']

    def __repr__(self):
        return "entities.User: {}".format(self.email)

    def toJSONDict(self):
        return super(User, self).toJSONDict(["uuid", "email"])
