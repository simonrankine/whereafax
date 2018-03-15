from constants import MAX_LINES
from exceptions import overflowException
import config


class pageHeader:

    def __init__(self):
        self.description = ""
        self.subcode = "0000"
        self.pageStatus = "8000"
        self.cycleTime = config.defaultCycleTime

    def output(self):
        toReturn = (("DE,{}\r\n").format(self.description)
                    ("SC,{}\r\n").format(self.subcode)
                    ("PS,{}\r\n").format(self.pageStatus)
                    ("CT,{},T\r\n").format(self.cycleTime))
        return toReturn


class page:

    def __init__(self):
        self.lines = []
        self.number = 100
        self.header = pageHeader()

    def addLine(self, line):
        if self.lines >= MAX_LINES:
            raise overflowException("Too many lines on page")
        self.lines.append(line)

    def output(self):
        
