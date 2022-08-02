#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

hosts=[]
switches=[]

netMask="128.0.0." # non è il nome giusto, correggere!

# definition for linear topology class
class linear_topology(Topo):

    #
    #   s1------s2------s3
    #    |       |       |   
    #    h1      h2      h3
    #

    def build(self, nSwitches, nHosts):

        
        
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

# definition for ring topology class
class ring_topology(Topo):

    #
    #              h1
    #              |
    #             s1          
    #             |                      
    #             s0         
    #            /  \         
    #           /    \        
    #    h2---s2-----s3---h3      
    #      
    
    def build(self, nSwitches, nHosts):

                
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
        #Add last link to close the ring
        self.addLink(switches[0],switches[nSwitches-1])

# definition for star topology class
class star_topology(Topo):

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

    def build(self, nSwitches, nHosts):

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

topos = { 'linear' : linear_topology,
          'ring' : ring_topology,
          'star' : star_topology
        }

# main function
def main():
    global nHosts,nSwitches
    # build topology
    topo = topology()
    # build network
    net = Mininet(
            topo = topo,
            controller = RemoteController ('c0', ip = '127.0.0.1', port = 6633)
        )
    
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__': 
    main()