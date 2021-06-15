#!/usr/bin/env python

" Custom Topology to use ONOS Controller"

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create MyTopo topology..."
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host

        info( '*** Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')
        s16 = self.addSwitch('s16')
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')
        s19 = self.addSwitch('s19')
        s20 = self.addSwitch('s20')
        s21 = self.addSwitch('s21')
        s22 = self.addSwitch('s22')
        s23 = self.addSwitch('s23')
        s24 = self.addSwitch('s24')
        s25 = self.addSwitch('s25')
        s26 = self.addSwitch('s26')
        s27 = self.addSwitch('s27')
        s28 = self.addSwitch('s28')
        s29 = self.addSwitch('s29')
        s30 = self.addSwitch('s30')
        s31 = self.addSwitch('s31')
        s32 = self.addSwitch('s32')
        s33 = self.addSwitch('s33')
        s34 = self.addSwitch('s34')
        s35 = self.addSwitch('s35')


        info( '*** Add hosts\n')
        h1 = self.addHost('h1', ip='10.1.0.1')
        h2 = self.addHost('h2', ip='10.1.0.2')
        h3 = self.addHost('h3', ip='10.2.0.3')
        h4 = self.addHost('h4', ip='10.2.0.4')
        h5 = self.addHost('h5', ip='10.3.0.5')
        h6 = self.addHost('h6', ip='10.3.0.6')
        h7 = self.addSwitch('h7', ip='10.3.0.7')
        h8 = self.addSwitch('h8', ip='10.3.0.8')
        h9 = self.addSwitch('h9', ip='10.3.0.9')
        h10 = self.addSwitch('h10', ip='10.3.0.10')
        h11 = self.addSwitch('h11', ip='10.3.0.11')
        h12 = self.addSwitch('h12', ip='10.3.0.12')
        h13 = self.addSwitch('h13', ip='10.3.0.13')
        h14 = self.addSwitch('h14', ip='10.3.0.14')
        h15 = self.addSwitch('h15', ip='10.3.0.15')
        h16 = self.addSwitch('h16', ip='10.3.0.16')
        h17 = self.addSwitch('h17', ip='10.3.0.17')
        h18 = self.addSwitch('h18', ip='10.3.0.18')
        h19 = self.addSwitch('h19', ip='10.3.0.19')
        h20 = self.addSwitch('h20', ip='10.3.0.20')
        h21 = self.addSwitch('h21', ip='10.3.0.21')
        h22 = self.addSwitch('h22', ip='10.3.0.22')

        info( '*** Add links\n')
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s3, h5)
        self.addLink(s3, h6)
        self.addLink(s1, h7)
        self.addLink(s1, h8)
        self.addLink(s2, h9)
        self.addLink(s2, h10)
        self.addLink(s3, h11)
        self.addLink(s3, h12)
        self.addLink(s1, h13)
        self.addLink(s1, h14)
        self.addLink(s2, h15)
        self.addLink(s2, h16)
        self.addLink(s3, h17)
        self.addLink(s3, h18)
        self.addLink(s1, h19)
        self.addLink(s1, h20)
        self.addLink(s2, h21)
        self.addLink(s2, h22)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s5, s2)
        self.addLink(s2, s6)
        self.addLink(s3, s6)
        self.addLink(s3, s4)
        self.addLink(s4, s6)
        self.addLink(s4, s5)
        self.addLink(s5, s6)

topos = { 'mytopo': ( lambda: MyTopo() ) }
    
if __name__ == '__main__':
    from onosnet import run
    run( MyTopo() )
