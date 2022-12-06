
from mininet.net import Mininet
from mininet.cli import CLI
import time

net = Mininet()

#Add Host
h1 = net.addHost( 'h1', ip='10.0.0.1', defaultRoute='via 10.0.1.1' )
h2 = net.addHost( 'h2', ip='10.0.0.2', defaultRoute='via 10.0.1.1' )
h3 = net.addHost( 'h3', ip='10.0.0.3', defaultRoute='via 10.0.1.1' )
h4 = net.addHost( 'h4', ip='10.0.0.4', defaultRoute='via 10.0.1.1' )
h5 = net.addHost( 'h5', ip='10.0.0.5', defaultRoute='via 10.0.1.1' )
h6 = net.addHost( 'h6', ip='10.0.0.6', defaultRoute='via 10.0.1.1' )

#Add Switch
s1 = net.addSwitch( 's1' )
s2 = net.addSwitch( 's2' )

#Add Controller
c0 = net.addController( 'c0' )

#Add Links
net.addLink( c0, s1 )

net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.addLink( h3, s1 )
net.addLink( h4, s1 )
net.addLink( h5, s1 )
net.addLink( h6, s1 )


net.start()
# t = 0
# while t < 100:
#     print( h1.cmd( 'ping -c1', h2.IP()))
#     time.sleep(3)
#     t += 1

net.pingAll()
CLI(net)
net.stop()