#!/usr/bin/python3


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink,Link

hosts=[]
switches=[]

# definition for test topology class
class test_topology(Topo):


    def build(self):
        #Add Switches
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch,stp=True)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch,stp=True)
        s5 = self.addSwitch('s5', cls=OVSKernelSwitch,stp=True)

        #Add Hosts
        h1 = self.addHost('h1', ip='10.0.0.1', mac="00:00:00:00:01:01")
        h2 = self.addHost('h2', ip='10.0.0.2', mac="00:00:00:00:01:02")
        h3 = self.addHost('h3', ip='10.0.0.3', mac="00:00:00:00:01:03")
        h4 = self.addHost('h4', ip='10.0.0.4', mac="00:00:00:00:02:04")
        h5 = self.addHost('h5', ip='10.0.0.5', mac="00:00:00:00:02:05")
        h6 = self.addHost('h6', ip='10.0.0.6', mac="00:00:00:00:02:06")
        h7 = self.addHost('h7', ip='10.0.0.7', mac="00:00:00:00:03:07")
        h8 = self.addHost('h8', ip='10.0.0.8', mac="00:00:00:00:03:08")
        h9 = self.addHost('h9', ip='10.0.0.9', mac="00:00:00:00:03:09")
        
        # Add Link between hosts and switches
        self.addLink(h1,s1,1,1,bw=10,delay="1ms", cls=TCLink)
        self.addLink(h2,s1,1,2,bw=10,delay="1ms", cls=TCLink)
        self.addLink(h3,s1,1,3,bw=10,delay="1ms", cls=TCLink)

        self.addLink(h4,s2,1,4,bw=10,delay="1ms", cls=TCLink)
        self.addLink(h5,s2,1,5,bw=10,delay="1ms", cls=TCLink)
        self.addLink(h6,s2,1,6,bw=10,delay="1ms", cls=TCLink)

        self.addLink(h7,s3,1,7,bw=10,delay="1ms", cls=TCLink)
        self.addLink(h8,s3,1,8,bw=10,delay="1ms", cls=TCLink)
        self.addLink(h9,s3,1,9,bw=10,delay="1ms", cls=TCLink)

        # Add Link between switches and switches
        self.addLink(s1,s4,14,11,bw=100,delay="5ms", cls=TCLink)
        self.addLink(s4,s5,15,14,bw=100,delay="5ms", cls=TCLink)
        self.addLink(s5,s3,13,15,bw=100,delay="5ms", cls=TCLink)
        self.addLink(s5,s2,12,15,bw=100,delay="5ms", cls=TCLink)
        self.addLink(s2,s4,14,12,bw=100,delay="5ms", cls=TCLink)
        

topos = { 
          'test' : test_topology
        }

# main function
def main():
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
