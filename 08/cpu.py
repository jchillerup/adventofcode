STATE_IDLE = 0
STATE_RUNNING = 1
STATE_FINISHED = 2
STATE_ERROR = 3

class CPU(object):
    ip = 0
    acc = 0
    state = STATE_IDLE
    program = None
    instruction = None
    argument = None

    def __init__(self, program):
        self.reset()
        self.program = program

    def reset(self):
        self.ip = 0
        self.acc = 0
        self.state = STATE_IDLE
        self.instruction = None
        self.argument = None

    def load_instruction(self):
        self.instruction, self.argument = self.program[self.ip]

    def step(self):
        self.load_instruction()

        if self.instruction == "acc":
            self.acc += self.argument
            self.ip += 1
        elif self.instruction == "jmp":
            self.ip += self.argument
        elif self.instruction == "nop":
            self.ip += 1
        else:
            self.state = STATE_ERROR
            raise NotImplementedError("Unsupported instruction %s" % self.instruction)

    def print_state(self):
        print("%03d | %12s | %8d" % (self.ip, self.program[self.ip], self.acc))

    def run(self):
        self.state = STATE_RUNNING

        while self.ip < len(instructions):
            step()
        
        self.state = STATE_FINISHED