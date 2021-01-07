from flask import Blueprint, jsonify, abort
from werkzeug.exceptions import HTTPException


bp = Blueprint('errors', __name__)


@bp.app_errorhandler(HTTPException)
def handle_exception(e):
    return jsonify(code=e.code,
                   name=e.name,
                   description=e.description), e.code
