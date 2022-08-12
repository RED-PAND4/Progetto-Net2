import os
import subprocess
import requests
import time
from dijkstar import Graph, find_path

def clear_flows():

    api="http://localhost:8080/stats/flowentry/clear/1"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/2"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/3"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/4"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/5"
    response = requests.delete(api) 

def request_output(switch,dst,out_port):

    api_url="http://localhost:8080/stats/flowentry/add"

    my_json={   
        "dpid": switch,
        "cookie": 1,
        "table_id": 0,
        "priority": 0,
        "match":{
            "dl_dst": dst,
            },
        }
    my_action=[]
    my_action.append(
        {
            "type":"OUTPUT",
            "port":out_port
        }
    )
    my_json["actions"]=my_action

    response=requests.post(api_url,json=my_json)
    print(response)

# main function
def main():
    print("Start")
    p=subprocess.Popen(["ryu-manager", "ryu.app.simple_switch_13", "ryu.app.ofctl_rest"])
    
    time.sleep(8)

    clear_flows()

    #packets to s1 hosts     
    request_output(2,"00:00:00:00:01:01",14)
    request_output(2,"00:00:00:00:01:02",14)
    request_output(2,"00:00:00:00:01:03",14)

    request_output(4,"00:00:00:00:01:01",11)
    request_output(4,"00:00:00:00:01:02",11)
    request_output(4,"00:00:00:00:01:03",11)

    request_output(5,"00:00:00:00:01:01",14)
    request_output(5,"00:00:00:00:01:02",14)
    request_output(5,"00:00:00:00:01:03",14)

    request_output(3,"00:00:00:00:01:01",15)
    request_output(3,"00:00:00:00:01:02",15)
    request_output(3,"00:00:00:00:01:03",15)


    #packets to s2 hosts 
    request_output(1,"00:00:00:00:02:04",14)
    request_output(1,"00:00:00:00:02:05",14)
    request_output(1,"00:00:00:00:02:06",14)

    request_output(4,"00:00:00:00:02:04",12)
    request_output(4,"00:00:00:00:02:05",12)
    request_output(4,"00:00:00:00:02:06",12)

    request_output(5,"00:00:00:00:02:04",12)
    request_output(5,"00:00:00:00:02:05",12)
    request_output(5,"00:00:00:00:02:06",12)

    request_output(3,"00:00:00:00:02:04",15)
    request_output(3,"00:00:00:00:02:05",15)
    request_output(3,"00:00:00:00:02:06",15)


    #packets to s3 hosts 
    request_output(1,"00:00:00:00:03:07",14)
    request_output(1,"00:00:00:00:03:08",14)
    request_output(1,"00:00:00:00:03:09",14)

    request_output(4,"00:00:00:00:03:07",15)
    request_output(4,"00:00:00:00:03:08",15)
    request_output(4,"00:00:00:00:03:09",15)

    request_output(2,"00:00:00:00:03:07",15)
    request_output(2,"00:00:00:00:03:08",15)
    request_output(2,"00:00:00:00:03:09",15)

    request_output(5,"00:00:00:00:03:07",13)
    request_output(5,"00:00:00:00:03:08",13)
    request_output(5,"00:00:00:00:03:09",13)
    
    
    #s1
    request_output(1,"00:00:00:00:01:01",1)
    request_output(1,"00:00:00:00:01:02",2)
    request_output(1,"00:00:00:00:01:03",3)
    
    #s2
    request_output(2,"00:00:00:00:02:04",4)
    request_output(2,"00:00:00:00:02:05",5)
    request_output(2,"00:00:00:00:02:06",6)

    #s3
    request_output(3,"00:00:00:00:03:07",7)
    request_output(3,"00:00:00:00:03:08",8)
    request_output(3,"00:00:00:00:03:09",9)
    
    input("Enter to kill controller..")
    os.system("sudo fuser -k 6633/tcp")

    

if __name__ == '__main__':
    main()
