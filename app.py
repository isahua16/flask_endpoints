from dbhelpers import run_statement
from flask import Flask, request
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

@app.get('/api/loyal-clients')
def get_loyal_clients():
    points = request.args.get('points')
    results = run_statement('CALL get_loyal_clients(?)', [points])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again.'

@app.post('/api/client')
def new_client():
    username = request.json.get('username')
    password = request.json.get('password')
    results = run_statement('CALL create_client(?,?)', [username, password])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again.'

@app.patch('/api/client-points')
def patch_client_points():
    username = request.json.get('username')
    points = request.json.get('points')
    results = run_statement('CALL update_points(?,?)', [username, points])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again.'

@app.delete('/api/client')
def delete_client():
    username = request.json.get('username')
    password = request.json.get('password')
    results = run_statement('CALL delete_client(?,?)', [username, password])
    return json.dumps(results, default=str)

app.run(debug=True)
