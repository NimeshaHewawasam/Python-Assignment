# Python-Assignment
Python Code Assignment - Use Case Scenarios


### TEST 01 
#### a 

- Following Command Generate Service Status `JSON` for `httpd, rabbitMQ, postgreSQL`

```
python3 check-service-status.py
```
- NOTE : Once executed above command will generate JSON records in APP DIR

#### b

- Install dependancy
```
pip install flask
```
- Start flast Server in Dev
```
flask --app rest-api-service run
```
- NOTE Service Start on `http://127.0.0.1:5000`
- Available Endpoint

- Add `POST : http://127.0.0.1:5000/add`
- Request Paylaod either
  ```
  {
    "service_name": "httpd",
    "service_status": "UP",
    "host_name": "host1"
  }

  {
    "service_name": "rabbitMQ",
    "service_status": "UP",
    "host_name": "host2"
  }

  {
    "service_name": "postgreSQL",
    "service_status": "UP",
    "host_name": "host3"
  }
  ```
- Get Overall HealthCheck
- ` GET : http://127.0.0.1:5000/healthcheck`
- Response Paylaod
- `"UP"` or `DOWN`
- Get HealthCheck Base on Service 
- ` GET : http://127.0.0.1:5000/healthcheck/:service`
- Availbe service are `httpd`,`rabbitMQ` and `rabbitMQ`
- Response Paylaod
- `"UP"` or `DOWN`


### TEST 03
- Following Command Generated Filterd New CSV file
```
python3 sold_properties.py
```
- NOTE : `sales_data.csv` -> `filter_sales_data.csv`

### Support 
- nimesha93swj@gmail.com
