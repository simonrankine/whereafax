from __future__ import absolute_import

from .constants import MAX_LINES, ESCAPE
from .exceptions import OverflowException
from .config import defaultCycleTime


class PageHeader:

    def __init__(self):
        self.description = ""
        self.subcode = "0000"
        self.pageStatus = "8000"
        self.cycleTime = defaultCycleTime

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
        self.subpageNumber = 1
        self.header = PageHeader()

    def addLine(self, line):
        if len(self.lines) >= MAX_LINES:
            raise OverflowException("Too many lines on page")
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
