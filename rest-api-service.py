from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_status_payload():
    # TODO : Paylaod Store in ES 
    return '', 201

@app.route('/healthcheck')
def get_healthcheck():
    # TODO : Get Overall Health Status UP or DOWN
    return "DOWN"

@app.route('/healthcheck/<service>')
def get_healthcheck_service(service):
    # TODO : Get Given Service Health Status either UP or DOWN
    return "UP"

