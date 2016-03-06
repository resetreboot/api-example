from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from services.program import list, create, update, get_program, delete
from utils.authorization import login_required
from validators.validator import with_validators
from validators.program import ProgramCreateValidator

from urllib.parse import parse_qs

class ProgramList(Controller):
    @login_required
    def get(self, request):
        success, result, errors = list()

        if errors:
            return BadRequest(errors)

        return Ok({'programs': [u.toJSONDict() for u in result['programs']]})


class ProgramMethods(Controller):
    @login_required
    def get(self, request):
        query = parse_qs(request["query_string"])
        names = query.get(b'name')

        if names is not None:
            if len(names) > 0: 
                name = names[0].decode()
                success, result, errors = get_program(name)

            else:
                return BadRequest()

        else:
            return BadRequest()

        if errors:
            return BadRequest(errors)

        return Ok({'program': result['program'].toJSONDict()})

    @login_required
    @with_validators([ProgramCreateValidator])
    def put(self, request, data):
        success, result, errors = update(
            data["program_data"].name,
            data["program_data"].version,
            data["program_data"].computer_model
        )

        if errors:
            return BadRequest(errors)

        return Ok()

    @login_required
    def delete(self, request):
        query = parse_qs(request["query_string"])
        names = query.get(b'name')

        if names is not None:
            if len(names) > 0: 
                name = names[0].decode()
                success, result, errors = delete(name)

            else:
                return BadRequest()

        else:
            return BadRequest()

        if errors:
            return BadRequest(errors)

        return Ok()

    @login_required
    @with_validators([ProgramCreateValidator])
    def post(self, request, data):
        success, result, errors = create(
            data["program_data"].name,
            data["program_data"].version,
            data["program_data"].computer_model,
        )
