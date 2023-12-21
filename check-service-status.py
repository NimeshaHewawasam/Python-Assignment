from random import random
from datetime import datetime
import json
"""
1. Get httpd, rabbitMQ, postgreSQL Status 
2. Save to {serviceName}-status-{@timestamp}.json
3. Payload to POST:http://<< service >>/add 

"""
def is_up_or_down():
    # This method for get service status either UP Or DOWN as Radom
    random_number = random()
    if random_number > 0.5: 
        return "UP"
    else:
        return "DOWN"

def get_httpd_status() :
    return {
        "service_name":"httpd",
        "service_status": is_up_or_down(),
        "host_name":"host1"
    }

def get_rabbitMQ_status() :
    return {
        "service_name":"rabbitMQ",
        "service_status": is_up_or_down(),
        "host_name":"host2"
    }

def get_postgreSQL_status() :
    return {
        "service_name":"postgreSQL",
        "service_status": is_up_or_down(),
        "host_name":"host3"
    }

def write_json_payload(service_name, paylaod) :
    timestamp = datetime.now().isoformat()
    file_name = service_name + '-status-' + timestamp + '.json'
    with open(file_name, "w") as outfile:
        json.dump(paylaod, outfile)

write_json_payload('httpd', get_httpd_status())
write_json_payload('rabbitMQ', get_rabbitMQ_status())
write_json_payload('postgreSQL', get_postgreSQL_status())

# TODO : Step 3 Here