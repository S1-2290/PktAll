import os, sys
from colors import NormalColors as nc, BoldColors as bc, Patterns as pt
from scapy.all import *

"""
Primary PKT_ALL module segment. This segment contains, what I like to call, level 1
segment primaries. These are also known as "basic" segments.
"""

## Variables: Colors
gs = nc.GREEN
rs = nc.RED
ys = nc.YELLOW
ws = nc.WHITE
bs = nc.BLUE
ce = nc.COLOR_END
##

class PktModules:

    def __init__(self, host_addr=None, host_addresses=[], max_ttl=20, ip_addr=None, ip_addrs=[], dst_port=80):
        self.host = host_addr
        self.hosts = host_addresses
        self.ttl = max_ttl
        self.ip = ip_addr
        self.ips = ip_addrs
        self.port = dst_port
    """
    Trace multiple host addresses
    """
    def trace_host_addresses(self):
        for x in self.hosts:
            try:
                r1, u = traceroute([x], maxttl=int(self.ttl))
                r1.show()
                pass
            except Exception, e:
                print pt.ERROR + bc.WHITE_BOLD + str(e) + bc.COLOR_END_BOLD
                sys.exit(1)
    """
    Trace a single host.
    """
    def trace_host(self):
        try:
            r1 = traceroute([self.host], maxttl=self.ttl)
        except Exception, e:
            print pt.ERROR + bc.WHITE_BOLD + str(e) + bc.COLOR_END_BOLD
            sys.exit(1)