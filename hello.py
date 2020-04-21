from flask import Flask, render_template
from test_data_gen import create_streets_db
import json


app = Flask(__name__)


@app.route('/')
def display_streets():
    return create_streets_db()