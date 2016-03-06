from errors.errors import get_response_error
from repositories.computer import (get_computers, add_computer, get_computer_by_id,
                                  get_computers_by_bits, get_computers_by_ram, 
                                  get_computer_by_model_fuzzy, get_computers_by_rom, 
                                  remove_computer, get_computer_by_model, modify_computer)


def list():
    computers = get_computers()
    return True, {'computers': computers}, None


def get_computer(model):
    computer = get_computer_by_model(model)
    return True, {'computer': computer}, None


def search_by_model(term):
    computers = get_computer_by_model_fuzzy(term)
    return True, {'computers': computers}, None


def search_by_ram(amount):
    computers = get_computers_by_ram(amount)
    return True, {'computers': computers}, None


def search_by_rom(amount):
    computers = get_computers_by_rom(amount)
    return True, {'computers': computers}, None


def search_by_bits(bits):
    computers = get_computers_by_bits(bits)
    return True, {'computers': computers}, None


def update(model, bits=None, ram=None, rom=None):
    errors = dict()
    if modify_computer(model, bits, ram, rom):
        return True, {}, None

    else:
        errors["model"] = get_response_error("COMPUTER_NOT_FOUND")
        return False, None, errors


def create(model, bits, ram, rom=None):
    errors = {}

    computer = get_computer_by_model(model)

    if computer:
        errors["model"] = get_response_error("COMPUTER_DOES_EXIST")

    if errors:
        return False, None, errors

    computer = add_computer(model, bits, ram, rom)

    return True, {"computer": computer}, None


def delete(model):
    errors = {}
    if remove_computer(model):
        return True, {}, None

    else:
        errors["model"] = get_response_error("COMPUTER_NOT_FOUND")
        return False, None, errors
