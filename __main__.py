from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.topo import MinimalTopo
from mininet.topolib import TreeTopo
from mininet.cli import CLI

from mininet.topo import Topo

hosts=[]
switches=[]

class LinearTopo (Topo):

    #
    #   s1------s2
    #    |       |
    #    h1      h2
    #

    def __init__( self ):
        
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

        hosts.append(leftHost)
        hosts.append(rightHost)

        switches.append(leftSwitch)
        switches.append(rightSwitch)

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
        h1 = self.addHost( 'h1' , ip = "127.0.0.1")
        h2 = self.addHost( 'h2' , ip = "127.0.0.2")
        h3 = self.addHost( 'h3' , ip = "127.0.0.3")
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s2 )
        self.addLink( h3, s3 )

        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s1 )

class StarTopo (Topo):

    #
    #              h1
    #              |
    #             s1          
    #             |                      
    #             s4          
    #            /  \         
    #           /    \        
    #     h2---s2    s3---h3      
    #      
    #  
    
    def __init__( self ):
        
        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s2 )
        self.addLink( h3, s3 )

        self.addLink( s1, s4 )
        self.addLink( s2, s4 )
        self.addLink( s3, s4 )

      




def main():
    print("Start")  
    topo = LinearTopo()
    net = Mininet(topo=topo)

    h3=net.addHost('h3')
    print(h3)
    it=net.items()
    print(it[3])
    
    link=h3.connectionsTo(switches[0])
    net.addLink(link)

    net.start()
    net.pingAll()
    #CLI(net)
    net.stop()  
    
    

if(__name__=='__main__'):
    main()