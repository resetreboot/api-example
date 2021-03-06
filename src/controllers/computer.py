from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from services.computer import list, create, update, get_computer, delete
from utils.authorization import login_required
from validators.validator import with_validators
from validators.computer import ComputerCreateValidator

from urllib.parse import parse_qs

class ComputerList(Controller):
    @login_required
    def get(self, request):
        success, result, errors = list()

        if errors:
            return BadRequest(errors)

        return Ok({'computers': [u.toJSONDict() for u in result['computers']]})


class ComputerMethods(Controller):
    @login_required
    def get(self, request):
        query = parse_qs(request["query_string"])
        models = query.get(b'model')

        if models is not None:
            if len(models) > 0: 
                model = models[0].decode()
                success, result, errors = get_computer(model)

            else:
                return BadRequest()

        else:
            return BadRequest()

        if errors:
            return BadRequest(errors)

        return Ok({'computer': result['computer'].toJSONDict()})

    @login_required
    @with_validators([ComputerCreateValidator])
    def put(self, request, data):
        success, result, errors = update(
            data["computer_data"].model,
            data["computer_data"].bits,
            data["computer_data"].ram,
            data["computer_data"].rom
        )

        if errors:
            return BadRequest(errors)

        return Ok()

    @login_required
    def delete(self, request):
        query = parse_qs(request["query_string"])
        models = query.get(b'model')

        if models is not None:
            if len(models) > 0: 
                model = models[0].decode()
                success, result, errors = delete(model)

            else:
                return BadRequest()

        else:
            return BadRequest()

        if errors:
            return BadRequest(errors)

        return Ok()

    @login_required
    @with_validators([ComputerCreateValidator])
    def post(self, request, data):
        success, result, errors = create(
            data["computer_data"].model,
            data["computer_data"].bits,
            data["computer_data"].ram,
            data["computer_data"].rom
        )
