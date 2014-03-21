# coding : UTF-8
'''
Created on 2014/03/21
@author: yamashiro-r
'''
import re

# ******************************************
class Combined(object):
    """
    Combined is Apache Log Format
        LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %D" combined
    @date 2014/03/21
    """

    def __init__(self):
        print "Combined init"
        self.name = "Combined"

    def getConvertText(self, line):
        pattern = re.compile(
                 r'^([0-9\.]+?) (.+?) (.+?) \[(.+?) \+[0-9]+\] \"(.+?) (.+?) (.+?)\" ([0-9]+?) ([0-9]+?) \"(.+?)\" \"(.+?)\"'
            )

        match = pattern.match(line)

        if match:
            csv = "\"{arg1}\",\"{arg2}\",\"{arg3}\",\"{arg4}\",\"{arg5}\",\"{arg6}\",\"{arg7}\",\"{arg8}\",\"{arg9}\",\"{arg10}\",\"{arg11}\""
            return csv.format(
                arg1 = match.group(1),
                arg2 = match.group(2),
                arg3 = match.group(3),
                arg4 = match.group(4),
                arg5 = match.group(5),
                arg6 = match.group(6),
                arg7 = match.group(7),
                arg8 = match.group(8),
                arg9 = match.group(9),
                arg10 = match.group(10),
                arg11 = match.group(11)
            )

        else:
            return ""

