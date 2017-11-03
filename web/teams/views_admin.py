from flask import Blueprint

admin = Blueprint(
    'admin',
    __name__,
)


@admin.route("/health", methods=['GET'])
def health_check():
    status = 200
    response = 'OK'

    # TODO: some logic to determine whether the service is healthy
    if 1 == 0:
        status = 500
        response = 'Error'

    return response, status


@admin.route("/quitquitquit", methods=['POST'])
def quit_app():

    # initiate graceful shutdown

    return 'OK', 200


@admin.route("/abortabortabort", methods=['POST'])
def abort_app():

    # final warning app being shutdown

    return 'OK', 200
