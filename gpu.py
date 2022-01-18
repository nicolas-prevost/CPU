import time

def tobinary(x):
    str = ''
    if x & 128 == 0:
        str += '0'
    else:
        str += '1'
    if x & 64 == 0:
        str += '0'
    else:
        str += '1'
    if x & 32 == 0:
        str += '0'
    else:
        str += '1'
    if x & 16 == 0:
        str += '0'
    else:
        str += '1'
    if x & 8 == 0:
        str += '0'
    else:
        str += '1'
    if x & 4 == 0:
        str += '0'
    else:
        str += '1'
    if x & 2 == 0:
        str += '0'
    else:
        str += '1'
    if x & 1 == 0:
        str += '0'
    else:
        str += '1'

    return str


class gpu:

    def __init__(self, instructions = []):
        self.counter = 0
        self.REG0 = 0
        self.REG1 = 0
        self.REG2 = 0
        self.REG3 = 0
        self.REG4 = 0
        self.REG5 = 0
        if len(instructions) != 0:
            self.program = instructions
        else:
            self.program = []


    def printstate(self):
        print()
        print("counter: " + str(self.counter))
        if self.counter < len(self.program):
            print("instruction: " + tobinary(self.program[self.counter]))
        else:
            print("instruction: END_OF_PROGRAM")
        print("REG0: " + tobinary(self.REG0) + " | REG1:"+ tobinary(self.REG1) + " | REG2:"+ tobinary(self.REG2))
        print("REG3: " + tobinary(self.REG3) + " | REG4:"+ tobinary(self.REG4) + " | REG5:"+ tobinary(self.REG5))

    def run(self):
        print('=== init ===')
        self.printstate()
        print('=== run ====')
        while self.counter != len(self.program):
            time.sleep(2)
            self.executeoperation(self.program[self.counter])
            self.printstate()

    def executeoperation(self, x): #do not forget to increase the counter at the end of the opperation if needed
        if x>>6 == 0:
            #immediate

            self.REG2 = x - (x >> 6 << 6)

            self.counter +=1

        if x>>6 == 1:
            #operations
            if x & int('0b00000111', 2) == 0:
                self.REG2 = self.REG0 | self.REG1
            if x & int('0b00000111', 2) == 1:
                self.REG2 = self.REG0 & self.REG1
            if x & int('0b00000111', 2) == 2:
                self.REG2 = self.REG0 ^ self.REG1
            if x & int('0b00000111', 2) == 3:
                self.REG2 = self.REG0 + self.REG1
                if (self.REG2).bit_length() > 6:
                    self.REG2 = self.REG2 - (self.REG2>>6<<6)

            self.counter += 1

        if x>>6 == 2:
            #copy
            value = 0
            if x & int('0b00111000', 2) >>3 == 0:
                value = self.REG0
            if x & int('0b00111000', 2) >>3 == 1:
                value = self.REG1
            if x & int('0b00111000', 2) >>3 == 2:
                print('form reg2')
                value = self.REG2
                print('form reg2')
            if x & int('0b00111000', 2) >>3 == 3:
                value = self.REG3
            if x & int('0b00111000', 2) >>3 == 4:
                value = self.REG4
            if x & int('0b00111000', 2) >>3 == 5:
                value = self.REG5

            if x & int('0b00000111', 2) == 0:
                self.REG0 = value
            if x & int('0b00000111', 2) == 1:
                print('ou')
                self.REG1 = value
            if x & int('0b00000111', 2) == 2:
                self.REG2 = value
            if x & int('0b00000111', 2) == 3:
                self.REG3 = value
            if x & int('0b00000111', 2) == 4:
                self.REG4 = value
            if x & int('0b00000111', 2) == 5:
                self.REG5 = value

            self.counter += 1

        if x>>6 == 3:
            #condition
            if x & int('0b00000111', 2) == 0:
                return
