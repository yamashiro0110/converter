# coding : UTF-8
'''
Created on 2014/03/21
@author: yamashiro-r
'''

import sys
from conv.combined import Combined
from conv.dummy    import Dummy

class ConverterFactory(object):
    """
    Create Log Converter Factory
    Created on 2014/03/21
    """

    """
    Initialize
    """
    def __init__(self, logFormat = ""):
        self.logFormat = logFormat
        print "ConvertFactory init. format is {logFormat}".format(logFormat = self.logFormat)
#         self.printSysPath()

    def printSysPath(self):
        for line in sys.path:
            print line

    """
    Create Converter Object Factory
    """
    def createConv(self):
        print "call getConverter. logFormat is {logFormat}".format(logFormat = self.logFormat)

        if self.logFormat == "combined":
            return Combined()

        else:
            return Dummy()
