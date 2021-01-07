from flask import Blueprint, jsonify


bp = Blueprint('oauth', __name__)


@bp.route('/login')
def login():
    return jsonify(message="OAuth login page")

