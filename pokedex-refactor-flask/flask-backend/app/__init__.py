
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask
from flask_migrate import Migrate
import os
from .config import Config
from .models.db import db
from .routes.item_routes import items
from .routes.pokemon_routes import pokemon


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(pokemon, url_prefix="/api/pokemon")
app.register_blueprint(items, url_prefix="/api/items")



# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
