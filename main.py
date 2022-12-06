from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.cli import CLI

SingleSwitchTopo()
net.start()
CLI(net)
net.stop()