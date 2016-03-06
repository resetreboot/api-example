from errors.errors import get_response_error
from repositories.program import (get_programs, add_program,
                                  get_program_by_name, 
                                  remove_program, modify_program)


def list():
    programs = get_programs()
    return True, {'programs': programs}, None


def get_program(name):
    program = get_program_by_name(name)
    return True, {'program': program}, None


def update(model, bits=None, ram=None, rom=None):
    errors = dict()
    if modify_program(model, bits, ram, rom):
        return True, {}, None

    else:
        errors["model"] = get_response_error("PROGRAM_NOT_FOUND")
        return False, None, errors


def create(name, version, computer_model):
    errors = {}

    program = get_program_by_name(name)

    if program:
        errors["name"] = get_response_error("PROGRAM_DOES_EXIST")

    if errors:
        return False, None, errors

    program = add_program(name, version, computer_model)

    return True, {"program": program}, None


def delete(name):
    errors = {}
    if remove_program(name):
        return True, {}, None

    else:
        errors["name"] = get_response_error("PROGRAM_NOT_FOUND")
        return False, None, errors
