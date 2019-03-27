import os, sys
from colors import NormalColors as nc, BoldColors as bc, Patterns as pt

"""
Utils module
"""

## Variables - Colors
gs = nc.GREEN
rs = nc.RED
ys = nc.YELLOW
ws = nc.WHITE
bs = nc.BLUE
ce = nc.COLOR_END
##

class ConsoleUtils:

    def __init__(self):
        pass

    @staticmethod
    def console(newLine, *args):
        for x in args:
            if newLine:
                print "\n" + pt.ASTK + bc.WHITE_BOLD + str(x) + bc.COLOR_END_BOLD + "\n"
                pass
            else:
                print pt.ASTK + bc.WHITE_BOLD + str(x) + bc.COLOR_END_BOLD
                pass

    @staticmethod
    def err_console(newLine, exit_on_error, *args):
        for x in args:
            if newLine:
                print "\n" + pt.ERROR + bc.YELLOW_BOLD + str(x) + bc.COLOR_END_BOLD + "\n"
            else:
                print pt.ERROR + bc.YELLOW_BOLD + str(x) + bc.COLOR_END_BOLD

            if exit_on_error:
                sys.exit(1)
            else:
                pass