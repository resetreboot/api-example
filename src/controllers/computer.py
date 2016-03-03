from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from services.computer import list, create, get_computer_by_id
from utils.authorization import login_required
from validators.validator import with_validators
from validators.computer import ComputerCreateValidator

class ComputerList(Controller):
    @login_required
    def get(self, request):
        success, result, errors = list()

        if errors:
            return BadRequest(errors)

        return Ok({'computers': [u.toJSONDict() for u in result['computers']]})


class Computer(Controller):
    @login_required
    def get(self, request, data):
        success, result, errors = get_computer_by_id(
            data["computer_data"].id
        )

        if errors:
            return BadRequest(errors)

        return Ok({'computer': result['computer'].toJSONDict()})
    @login_required
    @with_validators([ComputerCreateValidator])
    def post(self, request, data):
        success, result, errors = create(
            data["computer_data"].model,
            data["computer_data"].bits,
            data["computer_data"].ram,
            data["computer_data"].rom
        )
