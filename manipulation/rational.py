import sys_logging

less_than = 3 < 4
sys_logging.info("less than: 3 < 4 - " + str(less_than))

greater_than = 3 > 4
sys_logging.info("greater than: 3 > 4 - " + str(greater_than))

less_than_or_equal_to = 7 <= 7
sys_logging.info("less than or equal to: 7 <= 7 - " + str(less_than_or_equal_to))

greater_than_or_equal_to = 0 >= 0
sys_logging.info("greater than or equal to: 0 >= 0 - " + str(greater_than_or_equal_to))

equal_to_one = 3 == 3.0
equal_to_two = 1 == True
equal_to_three = 7 == True
equal_to_four = 0 == False
equal_to_five = 0.5 == False
sys_logging.info("equal to: 3 == 3.0 - " + str(equal_to_one))
sys_logging.info("equal to: 1 == True - " + str(equal_to_two))
sys_logging.info("equal to: 7 == True - " + str(equal_to_three))
sys_logging.info("equal to: 0 == False - " + str(equal_to_four))
sys_logging.info("equal to: 0.5 == False - " + str(equal_to_five))

not_equal = 1 != 1.0
sys_logging.info("not equal: 1 != 1.0 - " + str(not_equal))

