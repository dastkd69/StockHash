from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# Configuring the database for sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)


class Ret_Mut(db.Model):
	# Id : Field which stores unique id for every row in database table.
	# ticker stores ticker name
    # returns_multiple stores returns multiple of the stock
	id = db.Column(db.Integer, primary_key=True)
	ticker = db.Column(db.String(20), unique=True, nullable=False)
	returns_multiple = db.Column(db.Double)

	def __repr__(self):
		return f"Ticker : {self.ticker}, Returns_Multiple: {self.returns_multiple}"

    def send_json(self):
        return {
            'ticker': self.ticker,
            'returns_multiple': self.returns_multiple,
        }

    def get_ticker(self, ticker):
        db.query.filter_by(ticker=ticker).first()


    
    

    
def init_db(app):
    db = SQLAlchemy(app)
    return Ret_Mut(db)


if __name__ == '__main__':
	app.run()
