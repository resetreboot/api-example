from skame.schemas import strings as s, base as b, numeric as n

from errors.errors import get_response_error
from .validator import Validator


class ComputerCreateValidator(Validator):
    key_name = 'computer_data'
    __schema__ = b.schema({
        'model': s.NotEmpty(),
        'bits': n.IsStrictPositive(),
        'ram': n.IsStrictPositive(),
        'rom': n.IsStrictPositive(), 
    })

    def __init__(self, data: dict):
        super().__init__(data)
        if self.cleaned_data:
            self.model = self.cleaned_data['model']
            self.bits = self.cleaned_data['bits']
            self.ram = self.cleaned_data['rom']
            self.rom = self.cleaned_data['ram']


class ComputerModelValidator(Validator):
    key_name = 'computer_data'
    __schema__ = b.schema({
        'model': s.NotEmpty(),
    })

    def __init__(self, data: dict):
        super().__init__(data)
        if self.cleaned_data:
            self.model = self.cleaned_data['model']
        

