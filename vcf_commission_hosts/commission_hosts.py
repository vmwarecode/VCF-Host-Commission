import requests
import json

def get_request(url,username,password):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers,auth=(username, password))
    if(response.status_code == 200):
        data = json.loads(response.text)
    else:
        print("Error reaching the server.")
        exit(1)
    return data

def post_request(data,url,username,password):
    headers = {'Content-Type': 'application/json'}
    #username = 'admin'
    #password = 'VMwareInfra@1'
    response = requests.post(url, headers=headers, data=data, auth=(username, password))
    if(response.status_code == 202):
        request_id = json.loads(response.test)['id']
        print("Execution in progress.")
        status = get_request(url+request_id)['executionStatus']
        while(status == 'IN_PROGRESS'):
            status = get_request(hostname+request_id)['executionStatus']
            time.sleep(5)
        if(status == 'COMPLETED'):
            print("Execution of task is successful.")
        else:
            print("Error in executing the task.")
            
def delete_request(data,url):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url, headers=headers, data=data, auth=('admin', 'VMwareInfra@1'))
    
    
def comission_hosts(data):
    data = read_input('')['Hosts']
    hostname =  'https://sddc-manager.sfo01.rainpole.local/v1/hosts/validations/'
    post_request(data,hostname)

def decomission_hosts(data):
     delete_request(data,'https://sddc-manager.sfo01.rainpole.local/v1/hosts')

def read_input(path):
    with open(path+'data.json') as json_file:
        data = json.loads(json_file)
        return data

print("This script is intended for commissioning hosts.")