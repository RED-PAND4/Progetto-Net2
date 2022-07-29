
from re import S
from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.topo import MinimalTopo
from mininet.topolib import TreeTopo
from mininet.cli import CLI
from mininet.node import RemoteController, OVSSwitch

from mininet.node import Controller, OVSBridge, OVSKernelSwitch, RemoteController
from mininet.link import TCLink

from mininet.topo import Topo

import sys

hosts=[]
switches=[]

netMask="127.0.0."

   



class LinearTopo (Topo):
    
    #
    #   s1------s2------s3
    #    |       |       |   
    #    h1      h2      h3
    #

    def __init__( self ):
        
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        for i in range(nHosts):
            hosts.append(self.addHost("h{}".format(i+1),ip=netMask+"{}".format(i+1)))
            print(hosts[i])
        for i in range(nSwitches):
            switches.append(self.addSwitch("s{}".format(i+1)))

        # Add Link between hosts and switches
        for i in range(nHosts):
            self.addLink(hosts[i],switches[i%nSwitches])
        
        # Add Link between switches and switches
        for i in range(nSwitches-1):
            self.addLink(switches[i],switches[i+1])


class RingTopo (Topo):

    #
    #            h1          
    #             |                      
    #             s1          
    #            /  \         
    #           /    \        
    #          /      \       
    #    h2---s2------s3---h3    
    #                                 
    
    def __init__( self ):
        
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        for i in range(nHosts):
            hosts.append(self.addHost("h{}".format(i+1),ip=netMask+"{}".format(i+1)))
            print(hosts[i])
        for i in range(nSwitches):
            switches.append(self.addSwitch("s{}".format(i+1)))

        # Add Link between hosts and switches
        for i in range(nHosts):
            self.addLink(hosts[i],switches[i%nSwitches])
        
        # Add Link between switches and switches
        for i in range(nSwitches-1):
            self.addLink(switches[i],switches[i+1])
        self.addLink(switches[nSwitches],switches[0])

class StarTopo (Topo):

    #
    #              h1
    #              |
    #             s1          
    #             |                      
    #             s0         
    #            /  \         
    #           /    \        
    #     h2---s2    s3---h3      
    #      
    #  
    
    def __init__( self ):
        
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        for i in range(nHosts):
            hosts.append(self.addHost("h{}".format(i+1),ip=netMask+"{}".format(i+1)))
            print(hosts[i])
        for i in range(nSwitches):
            switches.append(self.addSwitch("s{}".format(i+1)))
        switches.append(self.addSwitch("s0"))

        # Add Link between hosts and switches
        for i in range(nHosts):
            self.addLink(hosts[i],switches[i%nSwitches])
        
        # Add Link between switches and switches
        for i in range(nSwitches):
            self.addLink(switches[i],switches[nSwitches])
        


def switch(string):
    if string=="l": 
        return LinearTopo()
    elif string=="ring":
        return RingTopo()
    elif string=="star":
        return StarTopo()
    else:
        return None


def foo():
    print("foo")
    return True

def main():
    print("Start")  
    
    global nHosts,nSwitches

    nHosts = int(raw_input('Enter total number of Hosts: '))
    nSwitches = int( raw_input('Enter total number of Switches: '))

    inputOK=False
    while(not inputOK):
        topo_type = raw_input('Enter start topology [linear,ring,star]: ')
        topo = switch(topo_type)
        if(topo!=None):
            inputOK=True
        else:
            print(" ! Input not valid, try again\n")


    net = Mininet(topo)

    net.start()
    net.ping()
    CLI(net)
    net.stop()  
    
    

if(__name__=='__main__'):
    main()