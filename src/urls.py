from anillo.handlers.routing import optionized_url as url, context


from controllers.index import Index
from controllers.user import Login, Register, List
from controllers.computer import ComputerList, Computer

urls = [
    context("/api/v1", [
        url("/", Index(), methods=["get", "post"]),
        url("/login", Login(), methods=["post"]),
        url("/users", Register(), methods=["post"]),
        url("/users", List(), methods=["get"]),
        url("/computers", ComputerList(), methods=["get"]),
        url("/computer", Computer(), methods=["get", "post"])
    ]),
]
