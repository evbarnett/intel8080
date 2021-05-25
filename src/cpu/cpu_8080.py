import logging


class Cpu8080:

    def __init__(self, mem_size=1024, debug=False):
        self.instructions = {}
        self.mem = [0 * mem_size]
        self.stack = [0 * 16]  # TODO stack size?
        self.sp = 0
        self.pc = 0
        self.cycles = 0
        self.debug = debug
        self.logger = logging.getLogger(__name__)

        self.current_opcode = None
        self.current_operand = None

        self._build_instructions()

    def _build_instructions(self):
        # Column _0
        self.instructions[0x00] = Instruction("NOP", self.noop, self.addr_none, 4, 1)
        self.instructions[0x10] = Instruction("NOP", self.noop, self.addr_none, 4, 1, official=False)
        self.instructions[0x20] = Instruction("NOP", self.noop, self.addr_none, 4, 1, official=False)
        self.instructions[0x30] = Instruction("NOP", self.noop, self.addr_none, 4, 1, official=False)
        self.instructions[0x40] = Instruction("MOV B,B", None, self.addr_none, 5, 1)
        self.instructions[0x50] = Instruction("MOV D,B", None, self.addr_none, 5, 1)
        self.instructions[0x60] = Instruction("MOV H,B", None, self.addr_none, 5, 1)
        self.instructions[0x70] = Instruction("MOV M,B", None, self.addr_none, 7, 1)
        self.instructions[0x80] = Instruction("ADD B", None, self.addr_none, 4, 1)
        self.instructions[0x90] = Instruction("SUB B", None, self.addr_none, 4, 1)
        self.instructions[0xA0] = Instruction("ANA B", None, self.addr_none, 4, 1)
        self.instructions[0xB0] = Instruction("ORA B", None, self.addr_none, 4, 1)
        self.instructions[0xC0] = Instruction("RNZ", None, self.addr_none, 4, 1)  # TODO cycles should be 11/5
        self.instructions[0xD0] = Instruction("RNC", None, self.addr_none, 4, 1)  # TODO cycles should be 11/5
        self.instructions[0xE0] = Instruction("RPO", None, self.addr_none, 4, 1)  # TODO cycles should be 11/5
        self.instructions[0xF0] = Instruction("RP", None, self.addr_none, 4, 1)  # TODO cycles should be 11/5

    def step(self):
        """TODO"""
        opcode = self.mem[self.pc]
        self.current_opcode = opcode

        ins = self.instructions[self.mem[self.pc]]

        if self.debug:
            self.logger.debug("%s: %s", self.pc, ins.mnemonic)

        self.pc += 1

        ins.addr_mode_func()
        ins.op_func()

        self.cycles += ins.cycles

    def noop(self):
        pass  # do nothing

    def movbb(self):
        pass

    def movdb(self):
        pass

    def movhb(self):
        pass

    def movmb(self):
        pass

    def _mov(self):
        pass

    def addr_none(self):
        pass  # do nothing

    def addr_immd(self):
        pass


class Instruction:

    def __init__(self, mnemonic: str, op_func, addr_mode_func, cycles: int, length: int, official=True):
        self.mnemonic = mnemonic
        self.op_func = op_func
        self.addr_mode_func = addr_mode_func
        self.cycles = cycles
        self.official = official
