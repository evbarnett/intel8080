import logging
import unittest

from src.cpu.cpu_8080 import Cpu8080


class TestOpcodes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)

    def test_noop(self):
        cpu = Cpu8080(debug=True)
        cpu.mem[0] = 0x00  # noop at 0x00 in mem
        cpu.pc = 0x00
        cpu.step()
        self.assertEqual(cpu.cycles, 4)
