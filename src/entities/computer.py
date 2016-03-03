from .entity import Entity

class Computer(Entity):
    def __init__(self, *args, **kwargs):
        self.model = kwargs['model']
        self.bits = kwargs['bits']
        self.ram = kwargs['ram']
        self.rom = kwargs['rom']

    def __repr__(self):
        return "entities.Computer: {}".format(self.model)

    def toJSONDict(self):
        return super(Computer, self).toJSONDict(["model", "bits", "ram", "rom"])
