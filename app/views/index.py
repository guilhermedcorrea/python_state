from flask import Blueprint
from flask import render_template

index_bp = Blueprint("index", __name__)

@index_bp.route("/")
def home():
    return render_template("index.html")

@index_bp.route("/produtos")
def retorna_produtos():
    return "produtos"