from flask import Blueprint, request
from app.api.kernel import response, response_error, logger

routes = Blueprint("routes", __name__)  # initialize blueprint


# function that is called when you visit /
@routes.route("/")
def index():
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself
    return response({"teste": "teste"}, 200)