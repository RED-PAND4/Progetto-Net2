from cgitb import reset
import os
import time
import requests

def clear_flows():

    api="http://localhost:8080/stats/flowentry/clear/1"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/2"
    response = requests.delete(api) 



def request(switch,in_port,src,dst,action_type,out_port,priority):

    api_url="http://localhost:8080/stats/flowentry/add"

    my_json={   
        "dpid": switch,
        "cookie": 1,
        "table_id": 0,
        "priority": priority,
        "match":{
            "in_port":in_port,
            "dl_dst": dst,
            "dl_src": src
            },
        }
    if(action_type=="output"):
        my_action=[]
        my_action.append(
            {
                "type":"OUTPUT",
                "port":out_port
            }
        )
        my_json["actions"]=my_action
    response=requests.post(api_url,json=my_json)
    print(my_json)
    print(response)


# main function
def main():
    print("Start")
    
    clear_flows()

    request(1,3,"00:00:00:00:01:03","00:00:00:00:02:04","output",12,0)
    request(1,1,"00:00:00:00:01:01","00:00:00:00:02:02","output",12,0)

    request(1,12,"00:00:00:00:02:02","00:00:00:00:01:01","output",1,0)
    request(1,12,"00:00:00:00:02:04","00:00:00:00:01:03","output",3,0)
   
    request(2,4,"00:00:00:00:02:04","00:00:00:00:01:03","output",11,0)
    request(2,2,"00:00:00:00:02:02","00:00:00:00:01:01","output",11,0)

    request(2,11,"00:00:00:00:01:01","00:00:00:00:02:02","output",2,0)
    request(2,11,"00:00:00:00:01:03","00:00:00:00:02:04","output",4,0)

if __name__ == '__main__': 
    main()










