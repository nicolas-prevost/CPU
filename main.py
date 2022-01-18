from gpu import *

def main():
    p = [
    int('0b00000010', 2),
    int('0b10010000', 2),
    int('0b10010001', 2),
    int('0b01000011', 2),
    int('0b10010000', 2),
    int('0b01000100', 2)]
    iter = gpu(p)
    iter.run()

main()
