from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# ES DB Object
ES = []

# Get Service Status By Given Service
def get_service_status_by_given_service(service) :
    # TODO : Should Get Latest logs base on datetime value
    found_log = next((obj for obj in ES if obj['service_name'] == service), None)
    if found_log : 
        return found_log['service_status']
    else : 
        return "DOWN"
    

@app.route('/add', methods=['POST'])
def add_status_payload():
    paylaod = request.json
    paylaod['timestamp'] = datetime.now().isoformat()
    ES.append(paylaod)
    return '', 201

@app.route('/healthcheck')
def get_healthcheck():
    httpd_status = get_service_status_by_given_service('httpd')
    rabbitMQ_status = get_service_status_by_given_service('rabbitMQ')
    postgreSQL_status = get_service_status_by_given_service('postgreSQL')
    if httpd_status == 'UP' and rabbitMQ_status == 'UP' and postgreSQL_status == 'UP':
        return 'UP'
    else :
        return 'DOWN'

@app.route('/healthcheck/<service>')
def get_healthcheck_service(service):
    service_list = ['httpd', 'rabbitMQ', 'postgreSQL']
    try:
        service_index = service_list.index(service)
        if service_index == 0:
            return get_service_status_by_given_service('httpd')
        if service_index == 1:
            return get_service_status_by_given_service('rabbitMQ')
        if service_index == 2:
            return get_service_status_by_given_service('postgreSQL')
    except ValueError:
        return 'Invalid Service' , 400
