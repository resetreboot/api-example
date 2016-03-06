from skame.schemas import strings as s, base as b, numeric as n

from errors.errors import get_response_error
from .validator import Validator


class ProgramCreateValidator(Validator):
    key_name = 'program_data'
    __schema__ = b.schema({
        'name': s.NotEmpty(),
        'version': s.NotEmpty(),
        'computer_model': s.NotEmpty(),
    })

    def __init__(self, data: dict):
        super().__init__(data)
        if self.cleaned_data:
            self.name = self.cleaned_data['name']
            self.version = self.cleaned_data['version']
            self.computer_model = self.cleaned_data['computer_model']


class ProgramModelValidator(Validator):
    key_name = 'program_data'
    __schema__ = b.schema({
        'name': s.NotEmpty(),
    })

    def __init__(self, data: dict):
        super().__init__(data)
        if self.cleaned_data:
            self.name = self.cleaned_data['name']
        

