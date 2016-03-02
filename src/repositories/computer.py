from entities.computer import Computer
from repositories.persistence import ComputerTable
from .session import session_manager as sm

def add_computer(model, bits, ram, rom=None):
    computer = ComputerTable(
        model=model,
        bits=bits,
        ram=ram,
        rom=rom
    )
    sm.session.add(computer)
    sm.session.commit()
    return _computer_row_to_computer(computer)


def remove_computer(id):
    computer = _get_computer_row_by_filter({"id": id})
    if computer:
        sm.session.delete(computer)
        return True

    else:
        return False


def modify_computer(id, model=None, bits=None, ram=None, rom=None):
    computer = _get_computer_row_by_filter({"id": id})
    
    if computer:
        if model:
            computer.model = model

        if bits:
            computer.bits = bits

        if ram: 
            computer.ram = ram

        if rom:
            computer.rom = rom

        sm.session.commit()
        return True

    else: 
        return False


def get_computers():
    computers = sm.session.query(ComputerTable).all()
    return [_computer_row_to_computer(computer_row) for computer_row in computers]


def get_computer_by_model(model):
    computer_row = _get_computer_row_by_filter({"model": model})
    return _computer_row_to_computer(computer_row)


# The above method is boring and will prove not very useful, so
# we add this one too, that filters by likes
def get_computer_by_model_fuzzy(model):
    # Filtering by like
    computers = _get_computers_by_filter(ComputerTable.model.like('\%{}\%'.format(model)))
    return [_computer_row_to_computer(computer_row) for computer_row in computers]


def get_computers_by_bits(bits):
    computers = _get_computers_by_filter({"bits": bits})
    return [_computer_row_to_computer(computer_row) for computer_row in computers]


def get_computers_by_ram(ram):
    computers = _get_computers_by_filter({"ram": ram})
    return [_computer_row_to_computer(computer_row) for computer_row in computers]


def get_computers_by_rom(rom):
    computers = _get_computers_by_filter({"rom": rom})
    return [_computer_row_to_computer(computer_row) for computer_row in computers]


def get_computer_by_id(id):
    computer_row = _get_computer_row_by_filter({"id": id})
    return _computer_row_to_computer(computer_row)


def _computer_row_to_computer(computer_row):
    if computer_row:
        return Computer(
            model=computer_row.model,
            bits=computer_row.bits,
            ram=computer_row.ram,
            rom=computer_row.rom
        )
    return None


# Always make a method or a function when you do a copypaste
def _get_computers_by_filter(f):
    return sm.session.query(ComputerTable).filter_by(**f).all()


def _get_computer_row_by_filter(f):
    computer_row = sm.session.query(ComputerTable).filter_by(**f).one_or_none()
    return computer_row

