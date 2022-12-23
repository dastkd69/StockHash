
from db import init_db
from model import main

app = Flask(__name__)
app.debug = True

# Configuring the database for sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db_model = init_db(app)


