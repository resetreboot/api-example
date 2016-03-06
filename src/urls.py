from anillo.handlers.routing import optionized_url as url, context


from controllers.index import Index
from controllers.user import Login, Register, List
from controllers.computer import ComputerList, ComputerMethods
from controllers.program import ProgramList, ProgramMethods

urls = [
    context("/api/v1", [
        url("/", Index(), methods=["get", "post"]),
        url("/login", Login(), methods=["post"]),
        url("/users", Register(), methods=["post"]),
        url("/users", List(), methods=["get"]),
        url("/computer", ComputerMethods(), methods=["get", "post", "put", "delete"]),
        url("/computers", ComputerList(), methods=["get"]),
        url("/program", ProgramMethods(), methods=["get", "post", "put", "delete"]),
        url("/programs", ProgramList(), methods=["get"]),
    ]),
]
