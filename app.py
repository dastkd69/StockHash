from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'




# **************** Databse Model *****************

db = SQLAlchemy(app)

class Ret_Mut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(20), unique=True, nullable=False)
    RS_Rating = db.Column(db.Float)
    MA_50 = db.Column(db.Float)
    MA_150 = db.Column(db.Float)
    MA_200 = db.Column(db.Float)
    Year_Low = db.Column(db.Float)
    Year_High = db.Column(db.Float)





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
    model.main()





# **************** Routing Table *****************

@app.route('/refreshtable', methods=['GET'])
def refresh_table():
    refresh()
    return 'OK'


@app.route('/getall', methods=['GET'])
def send_json_all():
    return jsonify(get_all())


@app.route('/gettop5', methods=['GET'])
def send_json_top5():
    return jsonify(get_top5())

    






if __name__ == '__main__':
	app.run()
