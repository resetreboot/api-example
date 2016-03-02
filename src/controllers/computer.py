from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from services.computer import list, create
from utils.authorization import login_required
from validators.user import LoginValidator, RegisterValidator
from validators.validator import with_validators

class ComputerList(Controller):
    @login_required
    def get(self, request):
        success, result, errors = list()

        if errors:
            return BadRequest(errors)

        return Ok({'computers': [u.toJSONDict() for u in result['computers']]})


class AddComputer(Controller):
    @login_required
    def post(self, request, data):
        success, result, errors = create(
            data["addcomputer_data"].model,
            data["addcomputer_data"].bits,
            data["addcomputer_data"].ram,
            data["addcomputer_data"].rom
        )
