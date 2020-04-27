from flask import Flask
from json_gen.test_data_gen import create_streets_db


app = Flask(__name__)


@app.route('/')
def display_streets():
    return create_streets_db()


if __name__ == "__main__":
    app.run()

