from cgitb import reset
import os
import time
import requests

def clear_flows():

    api="http://localhost:8080/stats/flowentry/clear/1"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/2"
    response = requests.delete(api) 
    api="http://localhost:8080/stats/flowentry/clear/3"
    response = requests.delete(api) 




def request_output(switch,src,dst,out_port):

    api_url="http://localhost:8080/stats/flowentry/add"

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





# main function
def main():
    #print("Start")
    
    clear_flows()
    
    print(">> Building slices\n")

    #s1
        #h1
    request_output(1,"00:00:00:00:01:01","00:00:00:00:01:02",2)  
    request_output(1,"00:00:00:00:01:01","00:00:00:00:03:08",14)
    request_output(1,"00:00:00:00:01:01","00:00:00:00:03:09",14)

    request_output(1,"00:00:00:00:01:02","00:00:00:00:01:01",1)  
    request_output(1,"00:00:00:00:03:08","00:00:00:00:01:01",1)
    request_output(1,"00:00:00:00:03:09","00:00:00:00:01:01",1)

        #h2
    request_output(1,"00:00:00:00:01:02","00:00:00:00:01:01",1) 
    request_output(1,"00:00:00:00:01:02","00:00:00:00:03:08",14)
    request_output(1,"00:00:00:00:01:02","00:00:00:00:03:09",14)

    #request_output(1,"00:00:00:00:01:01","00:00:00:00:01:02",2)  
    request_output(1,"00:00:00:00:03:08","00:00:00:00:01:02",2)
    request_output(1,"00:00:00:00:03:09","00:00:00:00:01:02",2)

        #h3
    request_output(1,"00:00:00:00:01:03","00:00:00:00:02:04",14)
    request_output(1,"00:00:00:00:01:03","00:00:00:00:02:05",14)
    request_output(1,"00:00:00:00:01:03","00:00:00:00:02:06",14)
    request_output(1,"00:00:00:00:01:03","00:00:00:00:03:07",14)

    request_output(1,"00:00:00:00:02:04","00:00:00:00:01:03",3)
    request_output(1,"00:00:00:00:02:05","00:00:00:00:01:03",3)
    request_output(1,"00:00:00:00:02:06","00:00:00:00:01:03",3)
    request_output(1,"00:00:00:00:03:07","00:00:00:00:01:03",3)

    #s2
        #h4
    request_output(2,"00:00:00:00:02:04","00:00:00:00:02:05",5)
    request_output(2,"00:00:00:00:02:04","00:00:00:00:02:06",6)
    request_output(2,"00:00:00:00:02:04","00:00:00:00:03:07",15)
    request_output(2,"00:00:00:00:02:04","00:00:00:00:01:03",14)

    #request_output(2,"00:00:00:00:02:04","00:00:00:00:02:05",5)
    #request_output(2,"00:00:00:00:02:04","00:00:00:00:02:06",6)
    request_output(2,"00:00:00:00:03:07","00:00:00:00:02:04",4)
    request_output(2,"00:00:00:00:01:03","00:00:00:00:02:04",4)

        #h5
    request_output(2,"00:00:00:00:02:05","00:00:00:00:02:04",4)
    request_output(2,"00:00:00:00:02:05","00:00:00:00:02:06",6)
    request_output(2,"00:00:00:00:02:05","00:00:00:00:03:07",15)
    request_output(2,"00:00:00:00:02:05","00:00:00:00:01:03",14)

    #request_output(2,"00:00:00:00:02:05","00:00:00:00:02:04",4)
    #request_output(2,"00:00:00:00:02:05","00:00:00:00:02:06",6)
    request_output(2,"00:00:00:00:03:07","00:00:00:00:02:05",5)
    request_output(2,"00:00:00:00:01:03","00:00:00:00:02:05",5)

        #h6
    request_output(2,"00:00:00:00:02:06","00:00:00:00:02:04",4)
    request_output(2,"00:00:00:00:02:06","00:00:00:00:02:05",5)
    request_output(2,"00:00:00:00:02:06","00:00:00:00:03:07",15)
    request_output(2,"00:00:00:00:02:06","00:00:00:00:01:03",14)

    #request_output(2,"00:00:00:00:02:06","00:00:00:00:02:04",4)
    #request_output(2,"00:00:00:00:02:06","00:00:00:00:02:05",5)
    request_output(2,"00:00:00:00:03:07","00:00:00:00:02:06",6)
    request_output(2,"00:00:00:00:01:03","00:00:00:00:02:06",6)

    #s3
        #h7
    request_output(3,"00:00:00:00:03:07","00:00:00:00:02:04",15) 
    request_output(3,"00:00:00:00:03:07","00:00:00:00:02:05",15) 
    request_output(3,"00:00:00:00:03:07","00:00:00:00:02:06",15) 
    request_output(3,"00:00:00:00:03:07","00:00:00:00:01:03",15)  
  

    request_output(3,"00:00:00:00:01:03","00:00:00:00:03:07",7)  
    request_output(3,"00:00:00:00:02:04","00:00:00:00:03:07",7)
    request_output(3,"00:00:00:00:02:05","00:00:00:00:03:07",7)
    request_output(3,"00:00:00:00:02:06","00:00:00:00:03:07",7)

        #h8
    request_output(3,"00:00:00:00:03:08","00:00:00:00:03:09",9)  
    request_output(3,"00:00:00:00:03:08","00:00:00:00:01:01",15)
    request_output(3,"00:00:00:00:03:08","00:00:00:00:01:02",15)

    request_output(3,"00:00:00:00:01:01","00:00:00:00:03:08",8)  
    request_output(3,"00:00:00:00:01:02","00:00:00:00:03:08",8)
    request_output(3,"00:00:00:00:03:09","00:00:00:00:03:08",8)
            
        #h9
    request_output(3,"00:00:00:00:03:09","00:00:00:00:03:08",8)  
    request_output(3,"00:00:00:00:03:09","00:00:00:00:01:01",15)
    request_output(3,"00:00:00:00:03:09","00:00:00:00:01:02",15)

    request_output(3,"00:00:00:00:01:01","00:00:00:00:03:09",9)  
    request_output(3,"00:00:00:00:01:02","00:00:00:00:03:09",9)
    request_output(3,"00:00:00:00:03:09","00:00:00:00:03:09",9)


    
    

if __name__ == '__main__': 
    main()


#s1 ovs-vsctl -- set port s1-eth12 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- -- id=@q0 create queue other-config:min-rate=0 other-config:max-rate=50000 -- -- id=@q0 create queue other-config:min-rate=0 other-config:max-rate=10000







