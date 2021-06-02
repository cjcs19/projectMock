# Third-party imports...

from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none,assert_list_equal,assert_is_none, assert_equal

# Local imports...
from projectMock.services import get_titles, get_todos,send_msg,geturlib

import logging
from urllib3_mock import Responses

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('TestMOCK Simple')
log.debug('Before Path')


@patch('projectMock.services.requests.get')
def test_request_response(mock_get):
    
    log = logging.getLogger('Response')

    # Call the service, which will send a request to the server.
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]
   
    todosnone = { }

    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    response = get_todos()  

    log.debug(response.json())

    assert_list_equal(response.json(), todos)

    mock_get.return_value = Mock(ok=False)      
    response = get_todos()
    assert_is_none(response)
    log.debug(response)


@patch('projectMock.services.requests.get')
def test_request_titles(mock_get):
    log = logging.getLogger('Response Title')

    # Call the service, which will send a request to the server.
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    response = get_titles()
    log.debug(response)
    assert_equal(response,todos[0]['title'])


@patch('projectMock.services.urllib3.PoolManager.request')
def test_msgHttp(mock_http):
    log = logging.getLogger('msgHttp')

    mock_http.return_value = Mock(status=200)
    geturlib()

    mock_http.return_value = Mock(status=201)
    geturlib()


