
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Host
from mininet.node import Controller
from mininet.node import OVSKernelSwitch
from mininet.link import TCLink
from mininet.log import info
import time

net = Mininet( topo=None,
                build=False,
                link=TCLink,
                ipBase='10.0.0.0/8')

info( '*** Adding controller\n' )
con1=net.addController(name='con1',
                    ip='127.0.0.1',
                    protocol='tcp',
                    port=6633)

info( '*** Add switches\n')
s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

info( '*** Add hosts\n')
c1 = net.addHost('c1', cls=Host, ip='10.0.0.1', defaultRoute=None, cpu=0.2, listenPorts=80)
c2 = net.addHost('c2', cls=Host, ip='10.0.0.2', defaultRoute=None, cpu=0.2)
c3 = net.addHost('c3', cls=Host, ip='10.0.0.3', defaultRoute=None, cpu=0.2)
c4 = net.addHost('c4', cls=Host, ip='10.0.0.4', defaultRoute=None, cpu=0.2)

serv1 = net.addHost('serv1', cls=Host, ip='10.0.0.5', defaultRoute=None)
serv2 = net.addHost('serv2', cls=Host, ip='10.0.0.6', defaultRoute=None)

info( '*** Add links\n')
net.addLink(c3, s1, 80, 82)
net.addLink(c2, s1, 80, 81)
net.addLink(c1, s1, 80, 81)

net.addLink(c4, s1, bw=10)
net.addLink(s1, serv1, bw=4)
net.addLink(s1, serv2, bw=4)

info( '*** Starting network\n')
net.build()
info( '*** Starting controllers\n')
for controller in net.controllers:
    controller.start()

info( '*** Starting switches\n')
net.get('s1').start([con1])

info( '*** Post configure switches and hosts\n')

s1.cmd('ovs-ofctl add-flow s1 dl_type=0x800,nw_proto=6,tp_src=82,actions=drop')

net.pingAll()

print('Pingando -> 81')

net.iperf(
    hosts  = [c1, c3],
    l4Type  = 'TCP',
    udpBw  = '10M',
    fmt  = None,
    seconds  = 5,
    port = 81
)

print('Pingando -> 80')
net.iperf(
    hosts  = [c1, c3],
    l4Type  = 'TCP',
    udpBw  = '10M',
    fmt  = None,
    seconds  = 5,
    port = 82
)

CLI(net)

net.stop()