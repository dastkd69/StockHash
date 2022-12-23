from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True





# **************** Databse Model *****************

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

class Ret_Mut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(20), unique=True, nullable=False)
    RS_Rating = db.Column(db.Double)
    MA_50 = db.Column(db.Double)
    MA_150 = db.Column(db.Double)
    MA_200 = db.Column(db.Double)
    Year_Low = db.Column(db.Double)
    Year_High = db.Column(db.Double)





# **************** Helper Functions *****************

def store(export_list):
    for item in export_list:
        c = Ret_Mut(ticker=item['Stock'], 
                    RS_Rating=item['RS_Rating'], 
                    MA_50=item["MA_50"], 
                    MA_150=item["MA_150"], 
                    MA_200=item["MA_200"], 
                    Year_Low=item["Year_Low"], 
                    Year_High=item["Year_High"])
        db.session.add(c)
    db.session.commit()


def get_all():
    return Ret_Mut.query.all()


def get_top5():
    return Ret_Mut.query.order_by(Ret_Mut.RS_Rating.desc()).limit(5)


def refresh():
    try:
        num_rows_deleted = db.session.query(Ret_Mut).delete()
        db.session.commit()
        print(num_rows_deleted + " Rows Deleted Succesfully!")
    except:
        db.session.rollback()





# **************** Routing Table *****************

@app.route('localhost:5000/refreshtable', methods=['GET'])
def refresh_table():
    refresh()
    return 'OK'


@app.route('localhost:5000/tickerstats', methods=['GET'])
def ticker_stats():
    






if __name__ == '__main__':
	app.run()
