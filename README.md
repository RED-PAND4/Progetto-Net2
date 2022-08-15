# Progetto-Net2

Comandi utili:


|ryu-manager controller.py & | fa partire il controller |
| sudo mn --custom network.py --controller remote --topo star,5,2 --mac | fa partire la rete |

| sudo fuser -k 6633/tcp | killa i controller nella porta 6633 |
| sudo mn -c | pulisce mininet |

http://demo.spear.narmox.com/app/?apiurl=demo#!/mininet





## Comandi morphing :

***start controller***

ryu-manager morph_controller.py

***run network***

sudo python3 morph_network.py
 
_______________

*command*

bus -> bus topology

ring -> ring topology

star -> star topology

cli -> enter mininet CLI for mininet command

quit -> end all

_______________
*help*

you need to wait the spanning tree before trying to ping the hosts, it ends when you see the "/FORWARD" at the end of the line in the controller terminal or you can wait 40-50 seconds from when you decide the topology


