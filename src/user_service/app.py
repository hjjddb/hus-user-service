from entrypoints.flask import flask_app
from user_service import config


def main():
    flask_app.main()


if __name__ == "__main__":
    main()
