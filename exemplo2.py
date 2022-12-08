from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info
from mininet.node import Controller, OVSKernelSwitch, RemoteController

def myNetwork():

    net = Mininet( topo=None,controller=RemoteController)    
    
    info( '*** Adding controller\n' )
    c0 = net.addController('c0', controller=RemoteController, ip="127.0.0.1") 
    

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip="10.0.0.1")
    h2 = net.addHost('h2', ip="10.0.0.2")
    h3 = net.addHost('h3',ip="10.0.0.3")
    h4 = net.addHost('h4',ip="10.0.0.4")
    h5 = net.addHost('h5',ip="10.0.0.5")
    h6 = net.addHost('h6',ip="10.0.0.6")

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(s1, s3)
    net.addLink(s2, s3)
    net.addLink(h4, s2)
    net.addLink(h5, s2)
    net.addLink(h6, s2)

    info( '*** Starting network\n')
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()


    #!/usr/bin/python
#https://gist.github.com/shreyakupadhyay/63c676cd41fcf3ff07ba15019d736c1f

#Sem controller
#sh ovs-ofctl add-flow s1 action=normal adicionar na tabela de fluxo
#sh ovs-ofctl del-flows s1 deletar da tabela de fluxo

#Com controller e openflow

#Aplicando regras na camada 2 (enlace)
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:05,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:06,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:05,actions=drop
#sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:06,actions=drop

#sh ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood

#Aplicando regras na camada 3 (rede)

#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.1,nw_dst=10.0.0.4,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.1,nw_dst=10.0.0.5,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.1,nw_dst=10.0.0.6,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.2,nw_dst=10.0.0.4,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.2,nw_dst=10.0.0.5,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.2,nw_dst=10.0.0.6,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.3,nw_dst=10.0.0.4,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.3,nw_dst=10.0.0.5,actions=drop
#sh ovs-ofctl add-flow s3 priority=500,ip,nw_src=10.0.0.3,nw_dst=10.0.0.6,actions=drop
#h1 ping -c5 h4