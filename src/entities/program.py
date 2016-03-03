from .entity import Entity

class Program(Entity):
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.version = kwargs['version']

    def __repr__(self):
        return "entities.Program: {}".format(self.name)

    def toJSONDict(self):
        return super(Program, self).toJSONDict(["name", "version"])
