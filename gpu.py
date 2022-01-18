def gpu(self):
    counter = 0
    REG0 = 0
    REG1 = 0
    REG2 = 0
    REG3 = 0
    REG4 = 0
    REG5 = 0
    program = []

    def printstate():
        print("counter: " + str(counter))
        print("instruction" + bin(program[counter]))
        print("REG0: " + bin(REG0) + " | REG1:"+ bin(REG1) + " | REG2:"+ bin(REG2))
        print("REG3: " + bin(REG3) + " | REG4:"+ bin(REG4) + " | REG5:"+ bin(REG5))

    def run():
        while counter !=len(program):
            executeoperation(program[counter])

    def executeoperation(x): #do not forget to increase the counter at the end of the opperation if needed
        if x>>6 == 0:
            #immediate
            return
        if x>>6 == 1:
            #operations
            if x & int('0b00000111', 2) == 0:
                REG2 = REG0 | REG1
            if x & int('0b00000111', 2) == 1:
                REG2 = REG0 & REG1
            if x & int('0b00000111', 2) == 2:
                REG2 = REG0 ^ REG1
            if x & int('0b00000111', 2) == 3:
                REG2 = REG0 + REG1
                if (REG2).bit_length() > 6:
                    REG2 = REG2 - (REG2>>6<<6)
        if x>>6 == 2:
            #copy
            value = 0
            if x & int('0b00111000', 2) >>3 == 0:
                value = REG0
            if x & int('0b00111000', 2) >>3 == 1:
                value = REG1
            if x & int('0b00111000', 2) >>3 == 2:
                value = REG2
            if x & int('0b00111000', 2) >>3 == 3:
                value = REG3
            if x & int('0b00111000', 2) >>3 == 4:
                value = REG4
            if x & int('0b00111000', 2) >>3 == 5:
                value = REG5

            if x & int('0b00000111', 2) == 0:
                REG0 = value
            if x & int('0b00000111', 2) == 1:
                REG1 = value
            if x & int('0b00000111', 2) == 2:
                REG2 = value
            if x & int('0b00000111', 2) == 3:
                REG3 = value
            if x & int('0b00000111', 2) == 4:
                REG4 = value
            if x & int('0b00000111', 2) == 5:
                REG5 = value
        if x>>6 == 3:
            #condition
            if x & int('0b00000111', 2) == 0:
                return
