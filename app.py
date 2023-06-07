from dbhelpers import run_statement
from flask import Flask
import json
app = Flask(__name__)
@app.get('')
def new_function():
    return
app.run(debug=True)
