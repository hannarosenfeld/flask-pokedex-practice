from flask import Blueprint
from ..models import Pokemon

pokemon = Blueprint("pokemon", __name__)


@pokemon.route("/")
def get_all_pokemon():
    all_pokemon = Pokemon.query.all()
    response = [pokemon.to_dict() for pokemon in all_pokemon]
    print("this is the response", response)
    return response
