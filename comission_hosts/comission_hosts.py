#Comission hosts
import requests
import json
import sys
import time


def get_request(url,username,password):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers,auth=(username, password))
    data = json.loads(response.text)
    if(response.status_code != 200):
        print json.dumps(data,indent=4, sort_keys=True)
        print "Error reaching the server."
        exit(1)
    return data

def post_request(data,url,username,password):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data, auth=(username, password))
    data = json.loads(response.text)
    if(response.status_code != 202):
        print "Error reaching the server."
        exit(1)
    return data

def poll_on_id(url,username,password,task):
    completed = ''
    processing = ''
    key = ''
    if(task):
        key = 'status'
        completed = 'SUCCESSFUL'
        processing = 'In Progress'
    else:
        key = 'executionStatus'
        completed = 'COMPLETED'
        processing = 'IN_PROGRESS'
    status = get_request(url,username,password)[key]
    while(status == processing):
        status = get_request(url,username,password)[key]
        time.sleep(5)
    if(task):
        return status
    if(status == completed):
        result = get_request(url,username,password)['resultStatus']
        print 'Operations status:'+ result
        return result
    else:
        print 'Operation failed'
        exit(0)

def comission_hosts(hostname,username,password):
    data = read_input()
    url =  hostname+'/v1/hosts/validations/commissions'
    response = post_request(data,url,username,password)
    request_id = response['id']
    print "Validating the input...."
    url = hostname+'/v1/hosts/validations/'+request_id
    result = poll_on_id(url,username,password,False)
    if(result == 'SUCCEEDED'):
        print 'Validation succeeded.'
        url = hostname + '/v1/hosts'
        response = post_request(data,url,username,password)
        print 'Comissioning hosts...'
        task_id = response['id']
        url = hostname+'/v1/tasks/'+task_id
        result = poll_on_id(url,username,password,True)
        if(result != 'Failed'):
            print 'Successfully comissioned hosts.'
        else:
            print 'Comissioning of hosts failed.'
            print json.dumps(response,indent=4, sort_keys=True)
    else:
        print 'Validation failed.'
        print json.dumps(response,indent=4, sort_keys=True)
        print result

#comission_hosts_spec.json is the preconfigured spec input file.
def read_input():
    with open('commission_hosts_spec.json') as json_file:
        data = json.load(json_file)
        return data

def get_help():
    help_description = '''\n\t\t----Comission hosts----
    Usage:
    python comission_hosts.py <hostname> <username> <password>\n Refer to documentation for more detais\n'''
    print help_description


def action_performer():
    arguments = sys.argv
    if(len(arguments) < 3):
        get_help()
        return
    hostname = 'https://'+arguments[1]
    username = arguments[2]
    passwsord = arguments[3]
    comission_hosts(hostname,username,password)
    return

action_performer()

