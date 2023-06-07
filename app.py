from dbhelpers import run_statement
from flask import Flask
import json

app = Flask(__name__)
@app.get('/api/clients')
def get_clients():
    results = run_statement('CALL get_clients()')
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again.'

app.run(debug=True, port=5001)
