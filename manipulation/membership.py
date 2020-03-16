import sys_logging

# in: This checks if a value is a member of a sequence.
pets = ['dog', 'cat', 'ferret']
a = 'fox' in pets
sys_logging.info("fox in pets: " + str(a))
sys_logging.info('me' in 'disappointment')

# not in: checks if a value is not a member of a sequence.
b = 'fox' not in pets
sys_logging.info('fox not in pets: ' + str(b))

# is and is not
list_a = []
list_b = []
list_c = list_a
is_a = list_a == list_b
is_b = list_a is list_b
sys_logging.info('a = ' + str(is_a) + ', b = ' + str(is_b))
sys_logging.info('id a = ' + str(id(list_a)) + ', id c = ' + str(id(list_c)))
