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

        if x>>6 == 1:
            #operations

        if x>>6 == 2:
            #copy

        if x>>6 == 3:
            #condition
