from constants import MAX_LINES, ESCAPE
from exceptions import overflowException
import config


class PageHeader:

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


class Page:

    def __init__(self):
        self.lines = []
        self.pageNumber = 100
        self.subpageNumber
        self.header = PageHeader()

    def addLine(self, line):
        if self.lines >= MAX_LINES:
            raise overflowException("Too many lines on page")
        self.lines.append(line)

    def pageNumberString(self):
        return "PN{}+{:02}\r\n".format(
            self.pageNumber,
            self.subpageNumber
        )

    def lineString(self, lineNumber):
        return "OL,{},{}{}\r\n".format(
            lineNumber,
            ESCAPE,
            self.lines[lineNumber].output()
        )

    def output(self):
        toReturn = self.header.output()
        toReturn = self.pageNumberString()
        for x in range(0, len(self.lines) - 1):
            toReturn += self.lineString(x)
        return toReturn
