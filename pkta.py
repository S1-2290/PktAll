import os, sys
from optparse import OptionParser, OptionGroup
from modules.pktmodules import PktModules
from modules.utils import ConsoleUtils
from modules.pktplot import Plotter

"""
Main PktAll module. Options and groups will be linked
to different module files. All are required.

- S1lent
v1.0
"""

def main():
    # Initialize the parser
    pr = OptionParser(usage="%prog -H [OPTIONS] | -h, --help", conflict_handler="resolve", description="A tool for all your " +\
                                                                                                    "packet needs.")
    pr.add_option('-H', '--host', dest="host", default=None, help="Set the destination host address.")
    pr.add_option('--multi-host', dest="m_host", default=None, help="Specify multiple destination host addresses.")
    pr.add_option('--ip', dest="ip_addr", default="127.0.0.1", help="Set the destination IP Address.")
    pr.add_option('--multi-ip', dest="m_ip", default=None, help="Specify multiple ip addresses.")
    pr.add_option('--port', dest="dst_port", default=80, help="Set the destination port.")
    # Initialize trace option group
    optg1 = OptionGroup(pr, "Section: Trace - Use '-H' and '--ttl'", "This is the trace section, for utilities to trace " +\
                                                                     "the packet route.")
    optg1.add_option('-T', '--traceroute', dest="optg1_tracert", action="store_true", help="Initialize a traceroute " +\
                                                                                           "on the supplied host.")
    optg1.add_option('--ttl', dest="optg1_ttl", default=20, help="Set the Time To Live for the packet.")
    # Initialize the plot group
    optg2 = OptionGroup(pr, "Section: Plot", "The plotter section - Use with '-H' and '--port-count'")
    optg2.add_option('--plot-ipid', dest="plot_ipid", action="store_true", help="Plot the IP ID using plot_lib chart.")
    optg2.add_option('--port_count', dest="max_ports", help="The max port to scan.")
    # Initialize scanning group
    opt3 = OptionGroup(pr, "Scanning", "The scanning section - Use with '-H'")
    opt3.add_option('-S', '--syn-scan', dest="opt3_syn", action="store_true", help="Perform a SYN scan.")

    # Add the option group to the primary parser
    pr.add_option_group(optg1)
    pr.add_option_group(optg2)
    pr.add_option_group(opt3)

    (options, args) = pr.parse_args()

    """
    Trace a host or multiple hosts
    """
    if options.optg1_tracert and options.m_host:
        hosts = str(options.m_host).split(',')
        for x in hosts:
            X = PktModules(host_addresses=hosts, max_ttl=int(options.optg1_ttl))
            X.trace_host_addresses()
        if options.host or options.host and options.optg1_ttl:
            X = PktModules(host_addr=str(options.host), max_ttl=int(options.optg1_ttl))
            X.trace_host()
    """
    Plotter - Simple
    """
    if str(options.host) == 0 or options.host is None:
        ConsoleUtils.err_console(True, True, "Please supply a destination host or address.")
    else:
        try:
            plot = Plotter(str(options.host), int(options.max_ports))
            plot.simple_plot()
            pass
        except Exception, e:
            ConsoleUtils.err_console(True, True, str(e))
    """
    Scanner options
    """
    


if __name__ == '__main__':
    main()
