from flask import Flask, redirect, url_for, request, render_template, jsonify
from db import init_db
from model import main

app = Flask(__name__)
app.debug = True

# Configuring the database for sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db_model = init_db(app)

@app.route('localhost:5000/refreshtable', methods=['GET'])
def refresh_table():



@app.route('localhost:5000/tickerstats', methods=['GET'])
def ticker_stats():
    db_model.
