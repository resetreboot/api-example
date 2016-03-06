from anillo.http.request import Request

from controllers.computer import ComputerMethods


def test_integration_create_computer_ok():
    request = Request()
    input_data = {'model': 'Spectrum',
                  'bits': 8,
                  'ram': 48,
                  'rom': 48}
    request['body'] = input_data

    # execute
    controller = ComputerMethods()
    result = controller.post(request)

    assert result['status'] == 200


def test_integration_duplicate_computer():
    request = Request()
    input_data = {'model': 'Spectrum',
                  'bits': 8,
                  'ram': 48,
                  'rom': 48}
    request['body'] = input_data

    # execute
    controller = ComputerMethods()
    result = controller.post(request)
    result = controller.post(request)

    assert result['status'] == 400
    assert result['body']['model']['code'] == "COMPUTER_DOES_EXIST"


def test_integration_create_computer_fail():
    request = Request()
    input_data = {'model': 'Spectrum',
                  'bits': '8',
                  'ram': 48,
                  'rom': 48}
    request['body'] = input_data

    # execute
    controller = ComputerMethods()
    result = controller.post(request)

    assert result['status'] == 400
