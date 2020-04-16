import sys_logging

# binary and(&) &-ing 011(3) and 100(4) results in 000(0).
binary_and_one = 2 & 3
binary_and_two = 3 & 4
sys_logging.info('2 & 3 = ' + str(binary_and_one))
sys_logging.info('3 & 4 = ' + str(binary_and_two))

# binary or(|) OR-ing 10(2) and 11(3) results in 11(3).
binary_or_one = 2 | 3
binary_or_two = 3 | 4
sys_logging.info('2 | 3 = ' + str(binary_or_one))
sys_logging.info('3 | 4 = ' + str(binary_or_two))

# binary XOR(^) XOR-ing 10(2) and 11(3) results in 01(1).
# 111(7) 11(3) 101(5) 100(4)
binary_xor_one = 2 ^ 3
binary_xor_two = 5 ^ 4
sys_logging.info('2 ^ 3 = ' + str(binary_xor_one))
sys_logging.info('5 ^ 4 = ' + str(binary_xor_two))

# binary's complement(~) It flips the bits. Binary for 2 is 00000010. Its one’s complement is 11111101.
# This is binary for -3.
binary_complement = ~3
sys_logging.info('~3 = ' + str(binary_complement))

# left shift(<<)  binary of 2 is 10. 2<<2 shifts it two places to the left. This results in 1000, which is binary for 8.
binaryLeftShift = 2 << 2
sys_logging.info('2 << 2 = ' + str(binaryLeftShift))

# right shift(>>)   binary of 3 is 11. 3>>2 shifts it two places to the right. This results in 00, which is binary for 0
binary_right_shift = 3 >> 2
sys_logging.info('3 >> 2 = ' + str(binary_right_shift))
