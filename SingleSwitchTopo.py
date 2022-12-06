
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

class SingleSwitchTopo( Topo ):
    # "Single switch connected to n hosts."
    def build( self ):
        #Add controller
        c0 = self.addController()

        #Add switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        #Add hosts
        h1 = self.addHost('h1', ip='10.0.1.2/24', defaultRoute='via 10.0.1.1')
        h2 = self.addHost('h2', ip='10.0.1.3/24', defaultRoute='via 10.0.1.1')
        h3 = self.addHost('h3', ip='10.0.2.2/24', defaultRoute='via 10.0.2.1')

        #Add links
        self.addLink (s1, h1)
        self.addLink (s1, h2)
        self.addLink (s2, h3)
        self.addLink (s1, s2)
        # switch = self.addSwitch( 's1' )
        # for h in range(h):
        #     host = self.addHost('h%s' % (h + 1))
        #     self.addLink(host, switch)


def perfTest():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( )
    net = Mininet( topo=topo,
	           host=CPULimitedHost, link=TCLink )
    net.start()
    print( "Dumping host connections" )
    dumpNodeConnections( net.hosts )
    print( "Testing network connectivity" )
    net.pingAll()
    print( "Testing bandwidth between h1 and h4" )
    h1, h3 = net.get( 'h1', 'h3' )
    net.iperf( (h1, h3) )
    net.stop()

def test():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( )
    net = Mininet( topo=topo,
	           host=CPULimitedHost, link=TCLink )
    net.start() 
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    # perfTest()
    test()