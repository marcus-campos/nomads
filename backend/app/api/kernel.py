import configparser
import logging
from typing import Tuple, List

from werkzeug.local import LocalProxy
from flask import current_app, jsonify
from flask.wrappers import Response

# logger object for all views to use
logger = LocalProxy(lambda: current_app.logger)
core_logger = logging.getLogger("core")

def response(
    data: dict = None, status: int = 200
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response

    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    if (status > 300 and not status < 200) and "message" not in data.keys():
        raise TypeError("You are using the wrong method, use response_error method")

    response = {"success": 200 <= status < 300, "data": data}
    
    return jsonify(response), status

def response_error(
    message: str = "", status: int = None
) -> Tuple[Response, int]:
    return response({"message": message}, status)

# add specific Exception handlers before this, if needed
# More info at http://flask.pocoo.org/docs/1.0/patterns/apierrors/
def all_exception_handler(error: Exception) -> Tuple[Response, int]:
    """Catches and handles all exceptions, add more specific error Handlers.
    :param Exception
    :returns Tuple of a Flask Response and int
    """
    return response_error(str(error), status=500)