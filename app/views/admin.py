from flask import Blueprint



Admin_bp = Blueprint('admin', __name__)


@Admin_bp.route("/")
def admin_index():
    return "amdin"

@Admin_bp.route("/appteste")
def teste_app():
    return "teste"
