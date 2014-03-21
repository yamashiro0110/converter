'''
Created on 2014/03/21
@author: yamashiro-r
'''

import sys, os

# Set "Script Excute Directoy" To PYTHONPATH
def setPath():
    cwd = os.getcwd()
    for addDir in ['src', 'test']:
        sys.path.append("{cwd}/{dir}".format(cwd = cwd, dir = addDir))

    print "set PYTHONPATH:"
    exportPath()

# Print PYTHONPATH
def exportPath():
    for line in sys.path:
        print line

    print ""

if __name__ == '__main__':
    """
    sys.argv[1] = Input Log File Path
    sys.argv[2] = Input Log File Format
    sys.argv[3] = Output Log File Path
    """

    setPath()
    from factory.converterFactory import ConverterFactory

    inputLog = sys.argv[1]
    logFormat = sys.argv[2]
    outPath = sys.argv[3]

    print "Convert Start"
#     print "inputLog:{inputLog}".format(inputLog = inputLog)
#     print "logFormat:{logFormat}".format(logFormat = logFormat)

    factory = ConverterFactory(logFormat)
    conv = factory.createConv()
#     print "conv.name = {name}".format(name = conv.name)

    outLog = open(outPath, "a")
    for line in open(inputLog, "r"):
        outLog.write("{text}\n".format(text = conv.getConvertText(line)),)

    outLog.close()
