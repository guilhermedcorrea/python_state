from flask import Blueprint


index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def home():
    return "index"

@index_bp.route("/produtos")
def retorna_produtos():
    return "produtos"