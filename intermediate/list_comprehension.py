import sys_logging

myList = []
for i in 'anxiety':
    myList.append(i)

sys_logging.info(myList)

comprehensionList = [i for i in 'anxiety']
sys_logging.info(comprehensionList)

comprehensionListTwo = [i * 2 for i in {1, 2, 3}]
sys_logging.info(comprehensionListTwo)

conditionalsList = [i if i % 2 != 0 else 'none' for i in range(8)]
conditionalsListOne = [i for i in range(8) if i % 2 != 0]
sys_logging.info(conditionalsList)
sys_logging.info(conditionalsListOne)

for i in range(7, 9):
    for j in range(1, 11):
        sys_logging.info(i * j)

sys_logging.info([[i * j for j in range(1, 11)] for i in range(7, 9)])
