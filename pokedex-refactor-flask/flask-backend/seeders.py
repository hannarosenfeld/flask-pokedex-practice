from app.models import Pokemon, db, Item
from app import app
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    # db.drop_all()
    # print("All tables tables")
    # db.create_all()
    # print("Created all tables")


    pokemon1 = Pokemon(
        number = 1,
        attack = 1,
        defense = 2,
        imageUrl = "/images/pokemon_snaps/1.svg",
        name = "Pikachu",
        type = "electric",
        moves = "tackle",
        encounterRate = 2.00,
        catchRate = 1.00,
        captured = True,
        createdAt = datetime.now(),
        updatedAt = datetime.now()
    )

    pokemon2 = Pokemon(
        number = 10,
        attack = 10,
        defense = 20,
        imageUrl = "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png",
        name = "Pikachu123",
        type = "electric",
        moves = "vine whip",
        encounterRate = 3.00,
        catchRate = 3.00,
        captured = False,
        createdAt = datetime.now(),
        updatedAt = datetime.now()
    )

    db.session.add(pokemon1)
    db.session.add(pokemon2)
    db.session.commit()


    item1 = Item(
        happiness = 1,
        imageUrl = "https://www.giantbomb.com/a/uploads/scale_small/0/6087/2437349-pikachu.png",
        name = "potion",
        price = 500,
        pokemonId = 1,
        createdAt = datetime.now(),
        updatedAt = datetime.now()
    )

    item2 = Item(
        happiness = 1,
        imageUrl = "https://static.wikia.nocookie.net/vsbattles/images/0/04/025Pikachu_XY_anime_4.png/revision/latest/scale-to-width-down/280?cb=20180310153929",
        name = "potion",
        price = 500,
        pokemonId = 1,
        createdAt = datetime.now(),
        updatedAt = datetime.now()
    )


    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
