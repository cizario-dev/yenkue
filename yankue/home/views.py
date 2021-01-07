from flask import Blueprint, jsonify, redirect, url_for


bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    # return jsonify(message="home index")
    return redirect(url_for('oauth.login'))
