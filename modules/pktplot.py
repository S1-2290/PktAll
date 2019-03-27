import os, sys, matplotlib
from scapy.all import *

"""
Plotter module
"""

class Plotter:

    def __init__(self, host_addr, max_port_count):
        self.host = host_addr
        self.mxport = max_port_count

    def simple_plot(self):
        a, b = sr(IP(dst=self.host)/TCP(sport=[RandShort()] * self.mxport))
        a.plot(lambda x:x[1].id)
