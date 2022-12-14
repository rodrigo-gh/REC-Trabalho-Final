
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
c1 = net.addController(  name='c1',
                         ip='127.0.0.1',
                         protocol='tcp',
                         port=6633)

info( '*** Add switches\n')
s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

info( '*** Add hosts\n')
h1 = net.addHost('h1', cls=None, ip='10.0.0.1', defaultRoute=None, cpu=0.2)
h2 = net.addHost('h2', cls=None, ip='10.0.0.2', defaultRoute=None, cpu=0.2)
h3 = net.addHost('h3', cls=None, ip='10.0.0.3', defaultRoute=None, cpu=0.2)
h4 = net.addHost('h4', cls=None, ip='10.0.0.4', defaultRoute=None, cpu=0.2)
h5 = net.addHost('h5', cls=None, ip='10.0.0.5', defaultRoute=None)
h6 = net.addHost('h6', cls=None, ip='10.0.0.6', defaultRoute=None)

info( '*** Add links\n')
net.addLink(h3, s1, bw=1)
net.addLink(h2, s1, bw=1)
net.addLink(h1, s1, bw=1)

net.addLink(h4, s1, bw=10)
net.addLink(s1, h5, bw=4)
net.addLink(s1, h6, bw=4)

info( '*** Starting network\n')
net.build()
info( '*** Starting controllers\n')
for controller in net.controllers:
    controller.start()

info( '*** Starting switches\n')
net.get('s1').start([c1])

info( '*** Post configure switches and hosts\n')

# s1.cmd('ovs-ofctl add-flow s1 dl_type=0x800,nw_proto=6,tp_src=82,actions=drop')

s1.cmd('sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01, priority=39000, dl_type=0x0800, nw_dst=*, idle_timeout=10, action=normal')
s1.cmd('sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01, priority=38000, dl_type=0x0800, nw_src=ANY, idle_timeout=10, tp_dst=82, action=normal')
s1.cmd('sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01, priority=38000, dl_type=0x0800, nw_src=ANY, idle_timeout=10, tp_dst=80, action=normal')
s1.cmd('sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01, priority=38000, dl_type=0x0800, nw_src=ANY, idle_timeout=10, action=drop')

net.pingAll()

print('Pingando -> 81')

net.iperf(
    hosts  = [h1, h2],
    l4Type  = 'TCP',
    udpBw  = '10M',
    fmt  = None,
    seconds  = 1,
    port = 82
)

print('Pingando -> 80')
net.iperf(
    hosts  = [h1, h3],
    l4Type  = 'TCP',
    udpBw  = '10M',
    fmt  = None,
    seconds  = 1,
    port = 81
)

CLI(net)

net.stop()