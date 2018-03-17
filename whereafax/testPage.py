import unittest
import mock

from page import Page


class TestPage(unittest.testcase):

    def setUp(self):
        self.dut = Page()
    
    def test_addline_ok(self):
        line = mock.MagicMock()
        self.dut.addLine(line)
        self.assertEqual(line, self.dut.lines[0])
