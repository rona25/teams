from functools import wraps

from flask import jsonify


def json_response(fn):
    """"Returns a JSON response for decorated functions that return a dict.
    """
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        ctx = fn(*args, **kwargs)
        return jsonify(ctx)

    return decorated_view
