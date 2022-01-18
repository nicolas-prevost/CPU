from gpu import *

def main():
    p = [int('0b0000010', 2), int('0b10010001', 2)]
    iter = gpu(p)
    iter.run()

main()
