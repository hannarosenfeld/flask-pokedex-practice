from .db import db

class Items(db.Models):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    happiness = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.Date, nullable=False)
    updatedAt = db.Column(db.Date, nullable=False)


    item = db.relationship(
        "Pokemon",
        back_populates="pokemon"
    )

    def __repr__(self):
        return f"< Item Id: {self.id}>"

    def to_dict(self):
        return {
            "id" : self.id,
            "happiness" : self.happiness,
            "imageUrl" : self.imageUrl,
            "name" : self.name,
            "price" : self.price,
            "pokemonId" : self.pokemonId,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            }
