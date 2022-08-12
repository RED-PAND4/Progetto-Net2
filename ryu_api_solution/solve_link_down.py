from cgitb import reset
import os
import time
import requests

def request_modify_entry(switch,src,dst,out_port):

    api_url="http://localhost:8080/stats/flowentry/modify_strict"

    my_json={   
        "dpid": switch,
        "cookie": 1,
        "table_id": 0,
        "priority": 0,
        "match":{
            "dl_dst": dst,
            "dl_src": src
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
    print(my_json)
    print(response)


def request_modify_entry_NOsrc(switch,dst,out_port):

    api_url="http://localhost:8080/stats/flowentry/modify_strict"

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
    print(my_json)
    print(response)





# main function
def main():
    #print("Start")

    
    print(">> Morphing slices\n")


    #s2

    request_modify_entry(2,"00:00:00:00:02:04","00:00:00:00:03:07",14)

    request_modify_entry(2,"00:00:00:00:02:05","00:00:00:00:03:07",14)

    request_modify_entry(2,"00:00:00:00:02:06","00:00:00:00:03:07",14)


    request_modify_entry_NOsrc(5,"00:00:00:00:02:04",14) 
    request_modify_entry_NOsrc(5,"00:00:00:00:02:05",14) 
    request_modify_entry_NOsrc(5,"00:00:00:00:02:06",14) 

     



    
    

if __name__ == '__main__': 
    main()


#s1 ovs-vsctl -- set port s1-eth12 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- -- id=@q0 create queue other-config:min-rate=0 other-config:max-rate=50000 -- -- id=@q0 create queue other-config:min-rate=0 other-config:max-rate=10000







