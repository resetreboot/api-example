from entities.program import Program 
from repositories.persistence import ProgramTable, ComputerTable

from .session import session_manager as sm

def add_program(name, version, computer_model, rom=None):
    computer = sm.session.query(ComputerTable).filter_by(**{"model": computer_model}).one_or_none()
    if computer:
        program = ProgramTable(
            name=name,
            version=version,
            made_for=computer
        )
        sm.session.add(program)
        sm.session.commit()

        return _program_row_to_program(program)
    
    else:
        return False


def remove_program(name):
    program = _get_program_row_by_filter({"id": id})
    if program:
        sm.session.delete(program)
        return True

    else:
        return False


def modify_program(name, version, model=None):
    program = _get_program_row_by_filter({"name": name})
    
    if program:
        if model:
            computer = sm.session.query(ComputerTable).filter_by(**{"model": computer_model}).one_or_none()
            if computer:
                program.made_for = computer

        if version:
            program.version = version

        sm.session.commit()
        return True

    else: 
        return False


def get_programs():
    programs = sm.session.query(ProgramTable).all()
    return [_program_row_to_program(program_row) for program_row in programs]


def get_program_by_name(name):
    program_row = _get_program_row_by_filter({"name": name})
    return _program_row_to_program(program_row)


def _program_row_to_program(program_row):
    if program_row:
        return Program(
            name=program_row.name,
            version=program_row.version,
            made_for=program_row.made_for.model
        )
    return None


def get_programs_by_computer_model(model):
    computer = sm.session.query(ComputerTable).filter_by(**{"model": model}).one_or_none()
    if computer:
        programs = _get_programs_by_filter({"made_for": computer})
        return [_program_row_to_program(program_row) for program_row in programs]

    else:
        return False


def _get_program_row_by_filter(f):
    program_row = sm.session.query(ProgramTable).filter_by(**f).one_or_none()
    return program_row


def _get_programs_by_filter(f):
    return sm.session.query(ProgramTable).filter_by(**f).all()
