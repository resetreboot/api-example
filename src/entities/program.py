from .entity import Entity

class Program(Entity):
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.version = kwargs['version']
        self.id = kwargs['id']

    def __repr__(self):
        return "entities.Program: {}".format(self.name)

    def toJSONDict(self):
        return super(Program, self).toJSONDict(["id", "name", "version"])
