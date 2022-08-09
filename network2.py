#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, Ryu
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def deleteLinks(net, sw_list):
    for s in sw_list :
        for sw in sw_list:
            if s != sw:
                if s.connectionsTo(sw):
                    net.delLinkBetween(s,sw)

def myNet():

    net = Mininet( controller=RemoteController, topo=None, build=False)

    #controller
    # Add Controllers
    c0 = net.addController( 'c0',  port=6633)   

    #number of host
    host_num=10
    switch_num = 5

    # Create switches
    sw_list=[ net.addSwitch( 's%d' % n ) for n in range ( 0,switch_num ) ]
    print(sw_list)


    # Create host
    hs_list = [net.addHost( 'h%d' % n) for n in range ( 0,host_num )]
    

    # Create Links
    i=0
    c=1
    for h in hs_list:
        net.addLink(sw_list[i], h)
        if c==0:
            i=i+1
        c=not c

    # a=1
    # for s in sw_list:
        # if a  == switch_num:
            # break
        # prova = net.addLink(s, sw_list[ a ])
        # a =a+ 1 
            

    net.build()
    c0.start()

    for s in sw_list:
        s.start([ c0 ])

    
    while 1 : 
        name = input("Enter your name: ")

        if name == "bus":
            print("*** BUS TOPOLOGY ***")
            c0.stop()
            #delete links
            deleteLinks(net, sw_list)

            #add bus links
            a=1
            for s in sw_list:
                if a  == switch_num:
                    break
                net.addLink(s, sw_list[ a ])
                print(" %s\n  |" % s.name)
                a += 1 
            net.build()
            c0.start()
            net.start()
            


        if name =="ring":
            print("*** RING TOPOLOGY ***")



        if name == "star":
            print("*** STAR TOPOLOGY ***")
            c0.stop()
            #delete links
            deleteLinks(net, sw_list)

            #add star links
            for s in sw_list:
                if s != sw_list[0]:
                    net.addLink(sw_list[0],s)
                    print("  | \n  |__%s" % s.name)
                else:
                    print("  %s" % s.name)
            print("\n")
            net.build()
            c0.start()
            net.start()


        if name == "view":
            print(net.switches)
            print(net.links)
            print(net.controllers)

        if name == "cli":
            CLI( net )

        if name == "quit":
            break
        
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    myNet()