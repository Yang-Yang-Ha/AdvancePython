import sys_logging

# addition(+)
addition = 3 + 4
sys_logging.info("3 + 4 = " + str(addition))

# subtraction
subtraction = 3 - 4
sys_logging.info("3 - 4 = " + str(subtraction))

# multiplication
multiplication = 3 * 4
sys_logging.info("3 * 4 = " + str(multiplication))

# division
division = 3 / 4
sys_logging.info("3 / 4 = " + str(division))

# exponentiation
exponentiation = 3 ** 4
sys_logging.info("exponentiation: 3 ** 4 = " + str(exponentiation))

# floor division
floor_division_one = 3 // 4
floor_division_two = 4 // 3
sys_logging.info("floor division: 3 // 4 = " + str(floor_division_one) + ", 4 // 3 = " + str(floor_division_two))

# modulus
modulus_one = 3 % 4
modulus_two = 4 % 3
sys_logging.info("modulus: 3 % 4 = " + str(modulus_one) + ", 4 % 3 = " + str(modulus_two))
