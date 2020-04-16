import sys_logging


# list data
def create_list():
    # python list can hold different types of values
    sys_logging.info(f'------start create list------')
    colors = ['red', 'green', 'blue']
    days = ['Monday', 'Tuesday', 'Wednesday', 4, 5, 6, 7]
    sys_logging.info(colors)
    sys_logging.info(f'create days {days} id = {id(days)}')
    return days


def access_list(days):
    sys_logging.info(f'------start access days {id(days)}------')
    sys_logging.info(f'days[0] {days[0]}')


def reassign_list(days):
    sys_logging.info(f'------reassign a single element of days {id(days)}------')
    days[3] = 'Thursday'
    sys_logging.info(f'reassign a single element {days} id = {id(days)}')
    sys_logging.info(f'------reassign a few elements------')
    days[3:] = ['Thursday']
    sys_logging.info(f'reassign a few elements {days} id = {id(days)}')
    days[2:3] = [1, 3]
    sys_logging.info(f'days[2:3] = {days} id = {id(days)}')
    days[2:2] = [1]
    sys_logging.info(f'days[2:2] = {days} + id(days) {id(days)}')
    sys_logging.info(f'------reassign the whole list------')
    days = [1, 2, 3, 4, 5, 6, 7]
    sys_logging.info(f'reassign all the list {days} + id(days) = {id(days)}')


def delete_list(days):
    sys_logging.info(f'-------delete element in days {id(days)}------')
    sys_logging.info(f'use del to delete a single elements in {days}')
    del days[2]
    sys_logging.info(f'after delete days[2] {days}')
    sys_logging.info(f'use del days to delete all the list')


def concatenate_list():
    sys_logging.info(f'------concatenate list------')
    a, b = [3, 1, 2], [4, 5, 6]
    sys_logging.info(f'a + b = {a + b}')


def list_operations():
    sys_logging.info(f'------list operations------')
    sys_logging.info(f'first one: multiplication')
    a = [3, 1, 2]
    sys_logging.info(f'a = {a} a*3 = {a * 3}')
    sys_logging.info(f'second one: Iterating on a list')
    for i in [1, 2, 3]:
        if i % 2 == 0:
            sys_logging.info(f'i = {i}')
    sys_logging.info(f'third one: list comprehension')
    even = [i for i in range(1, 11) if i % 2 == 0]
    sys_logging.info(f'even = {even}')


def built_in_functions():
    sys_logging.info(f'------built in function-------')
    a = [2, 3, 4, 65, 7, 8, 9, 0]
    sys_logging.info(f'len() = {len(a)}')
    sys_logging.info(f'max() = {max(a)}, this list must be in the same type')
    sys_logging.info(f'min() = {min(a)}, this list must be in the same type')
    sys_logging.info(f'sum() = {sum(a)}, this list must hold all numeric values')
    sys_logging.info(f'sorted() = {sorted(a, reverse=False)}, a = {a} this list must be in the same type')
    sys_logging.info(f"list('abc') = {list('adb')} just can convert iterables")
    sys_logging.info(f"any(['', '', '1'] = {any(['', '', '1'])}")
    sys_logging.info(f"all(['', '', '1'] = {all(['', '', '1'])}")


def built_in_method():
    sys_logging.info(f'------built in method------')
    a = [2, 3, 4, 5, 7, 6, 9]
    sys_logging.info(f'original a = {a}')
    a.append(2)
    sys_logging.info(f'a.append(2) = {a}')
    a.insert(2, 5)
    sys_logging.info(f'a.insert(2, 5) = {a}')
    a.remove(2)
    sys_logging.info(
        f'a.remove(2) = {a} the parameter is value, if we have two same values, it will del the first one')
    a.pop(3)
    sys_logging.info(f'a.pop(3) = {a}, the parameter is the index')
    sys_logging.info(f'a.index(3) = {a.index(3)}')
    sys_logging.info(f'a.count(3) = {a.count(3)}')
    a.sort()
    sys_logging.info(f'a.sort() = {a}')
    a.reverse()
    sys_logging.info(f'a.reverse() = {a}')
    a.clear()
    sys_logging.info(f'a.clear() = {a}')


def list_data():
    days = create_list()
    access_list(days)
    reassign_list(days)
    delete_list(days)
    concatenate_list()
    list_operations()
    built_in_functions()
    built_in_method()


def logical_tuple():
    sys_logging.info(f'------logical tuple------')
    # tuple comparison just compare the first elements, if they are equal, then the next one.
    a = (1, 123, 234, 23)
    b = (3, 2, 1)
    sys_logging.info(f'a<b {a < b}')


def tuple_data():
    sys_logging.info(f'------tuple data------')
    logical_tuple()


def delete_set():
    sys_logging.info(f'------delete set-------')
    numbers = {3, 2, 1, 4, 5, 6, 7}
    sys_logging.info(f'numbers set {numbers}')
    numbers.discard(3)  # would not raise a KeyError if the value doesn't exist
    sys_logging.info(f'numbers.discard(3) {numbers}')
    numbers.remove(2)  # would raise a KeyError if the value exist
    sys_logging.info(f'numbers.remove(3) {numbers}')
    a = numbers.pop()
    sys_logging.info(f'numbers.pop() a = {a}, numbers = {numbers}')


def update_set():
    sys_logging.info(f'------update set------')
    numbers = {1, 3, 4, 5, 8}
    numbers.add(3.5)
    sys_logging.info(f'numbers.add(3.5). numbers = {numbers}')
    numbers.update({1, 3, 4, 9}, {'a', 'b'})
    sys_logging.info(f'numbers.update() method. numbers = {numbers}')


def methods_set():
    sys_logging.info(f'------set method------')
    set_1, set_2, set_3 = {1, 2, 3}, {3, 4, 5}, {5, 6, 7}
    sys_logging.info(f'set_1 = {set_1}, set_2 = {set_2}, set_3 = {set_3}')
    union_set = set_1.union(set_2, set_3)
    sys_logging.info(f'set_1.union(set_2, set_3) = {union_set}')
    intersection_set = set_1.intersection(set_2)
    sys_logging.info(f'set_1.intersection(set_2) = {intersection_set}')
    difference_set = set_1.difference(set_2)
    sys_logging.info(f'set_1.difference(set_2) = {difference_set}')
    symmetric_difference = set_1.symmetric_difference(set_2)
    sys_logging.info(f'set_1.symmetric_difference(set_2) = {symmetric_difference}')
    sys_logging.info(f'add update in these methods tail, it will update the main set')
    sys_logging.info(f'set_1.isdisjoint(set_3) = {set_1.isdisjoint(set_3)}')
    sys_logging.info(f'set_1.issubset(set_2) = {set_1.issubset(set_2)}')
    sys_logging.info(f'set_1.issuperset(set_2) = {set_1.issuperset(set_2)}')


def set_data():
    sys_logging.info(f'------set data------')
    delete_set()
    update_set()
    methods_set()


def create_dictionary():
    sys_logging.info(f'------create dictionary------')
    dict_one = {'PB&J': 'Peanut Butter and Jelly', 'PJ': 'Pajamas'}
    sys_logging.info(f'dict_one = {dict_one}. Type of dict_one = {type(dict_one)}')
    dict_two = {x: x * x for x in range(8)}
    sys_logging.info(f'dict comprehension dict_two = {dict_two}')
    dict_three = {1: 'carrots', 'two': [1, 2, 3]}
    sys_logging.info(f'Mixed dictionary dict_three = {dict_three}')
    dict_four = dict(((1, 1), (2, 3)), a=2, b=3)
    sys_logging.info(f'use dict() function to create a dict. dict_four = {dict_four}')
    dict_five = dict({'a': 1, 'b': 2, 'a': 'c'})
    sys_logging.info(f'Declaring one key more than once: {dict_five}')
    dict_six = {}
    sys_logging.info(f'the empty dict_six = {dict_six}')
    dict_six[2] = 'dog'
    dict_six['six'] = 6
    sys_logging.info(f'After adding two elements dict_six = {dict_six} ')


def access_dictionary():
    sys_logging.info(f'------ access dictionary------')
    animals = {1: 'dog', 2: 'cat', 3: 'ferret'}
    sys_logging.info(f'animals = {animals}')
    sys_logging.info(f'access through key animals[1] = {animals[1]}')
    sys_logging.info(f'access through get() method animals.get(1) = {animals.get(1)}')


def reassign_dictionary():
    sys_logging.info(f'------reassign dictionary------')
    numbers = {1: 1, 2: 2, 3: 3}
    sys_logging.info(f'thr original numbers = {numbers}')
    numbers[2] = 4
    sys_logging.info(f'update numbers[2] = 4, numbers = {numbers}')
    numbers[4] = 4
    sys_logging.info(f'add a new element numbers[4] = 4, numbers = {numbers}')


def delete_dictionary():
    sys_logging.info(f'------delete dictionary------')
    numbers = {1: 1, 2: 2, 3: 3}
    del numbers[1]
    sys_logging.info(f'del numbers[1] = {numbers}')


def dict_built_in_method():
    sys_logging.info(f'------dict built-in method------')
    numbers = {1: '1', 2: '2', 3: '3', 4: '4'}
    sys_logging.info(f'numbers = {numbers}')
    sys_logging.info(f'numbers.keys() = {type(numbers.keys())} + {numbers.keys()}')
    sys_logging.info(f'numbers.values() = {type(numbers.values())} + {numbers.values()}')
    sys_logging.info(f'numbers.items() = {type(numbers.items())} + {numbers.items()}')
    sys_logging.info(f'numbers.get(3, 0) = {type(numbers.get(3, 0))} + {numbers.get(3, 0)}')
    new_dict = numbers.copy()
    sys_logging.info(
        f'new_dict = numbers.copy(), new_dict = {new_dict}, id(new_dict) = {id(new_dict)}, id(numbers) = {id(numbers)}')
    sys_logging.info(f'numbers.pop(2, 3) = {numbers.pop(2, 3)}')
    sys_logging.info(f'numbers.popitem() = {numbers.popitem()} + {type(numbers.popitem())} + {numbers.popitem()}')
    part_of_new_dict = new_dict.fromkeys((1, 3), 0)
    sys_logging.info(f'new_dict.fromkeys((1, 3), 0) = {part_of_new_dict}')
    dict_a = {1: '1', 2: '2', 3: '3'}
    dict_b = {1: '2', 4: '4', 5: '5'}
    sys_logging.info(f'dict_a = {dict_a} , dict_b = {dict_b}.')
    dict_a.update(dict_b)
    sys_logging.info(f'dict_a.update(dict_b) = {dict_a}')


def dictionary_data():
    sys_logging.info(f'------dictionary data-------')
    create_dictionary()
    access_dictionary()
    reassign_dictionary()
    delete_dictionary()
    dict_built_in_method()


if __name__ == '__main__':
    # list_data()
    # tuple_data()
    set_data()
    # dictionary_data()
