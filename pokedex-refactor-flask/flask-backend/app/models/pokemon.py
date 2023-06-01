from .db import db
import enum
from sqlalchemy import Integer, Enum


class Types(enum.Enum):
    fire = "fire"
    electric = "electric"
    normal = "normal"
    ghost = "ghost"
    psychic = "psychic"
    water ="water"
    bug ="bug"
    dragon ="dragon"
    grass ="grass"
    fighting ="fighting"
    ice = "ice"
    flying = "flying"
    poison = "poison"
    ground = "ground"
    rock = "rock"
    steel = "steel"


class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.Enum(Types), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Decimal(3, 2), nullable=False, default_value=1.00)
    catchRate = db.Column(db.Decimal(3, 2), nullable=False, default_value=1.00)
    captured = db.Column(db.Boolean, nullable=False, default_value=False)
    createdAt = db.Column(db.Date, nullable=False)
    updatedAt = db.Column(db.Date, nullable=False)

    pokemon = db.relationship(
        "Items",
        back_populates="item"
    )

    def __repr__(self):
        return f"< Pokemon Id: {self.id}>"

    def to_dict(self):
        return {
            "id" : self.id,
            "number" : self.number,
            "attack" : self.attack,
            "defense" : self.defense,
            "imageUrl" : self.imageUrl,
            "name" : self.name,
            "type" : self.type,
            "moves" : self.moves,
            "encounterRate" : self.encounterRate,
            "catchRate" : self.catchRate,
            "captured": self.captured,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            }
