import apifairy
from flask import Flask, blueprints
import os

from entrypoints.flask import schemas
from domains import commands
from user_service import config

bp = blueprints.Blueprint("User Manager", __name__)

_bus = None


@bp.route("/users", methods=["POST"])
@apifairy.body(schemas.UserSchema)
def create_user(body):
    command = commands.CreateUserCommand(**body)
    _bus.handle(command)
    return "Created", 201


# @bp.route


def create_app():
    app = Flask(__name__)
    return app


def main():
    app = create_app()
    port = config["service"]["DEPLOY_PORT"]
    debug = config["service"]["DEBUG"]
    app.run(port=port, debug=debug)
