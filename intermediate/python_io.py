# Mode	Description
# r	To read a file (default)
# w	To write a file; Creates a new file if it doesn’t exist, truncates if it does
# x	Exclusive creation; fails if file already exists
# a	To append at the end of file; create if doesn’t exist
# t	Text mode (default)
# b	Binary mode
# +	To open a file for updating (reading or writing)

import os
import sys_logging

sys_logging.info(f'current work directory: {os.getcwd()}')
sys_logging.info(f'file list {os.listdir()}')

# read file
with open('build_in.py') as file:
    # sys_logging.info(file.read(5))
    # sys_logging.info(file.tell())
    # sys_logging.info(file.seek(0))
    # sys_logging.info(file.read())
    # for line in file:
    #     sys_logging.info(line)
    sys_logging.info(file.readline())
    sys_logging.info(file.tell())
    sys_logging.info(file.readlines())

# write file
writeFile = open('write.txt', 'w')
writeFile.write('Hi, nice to meet you Mr White')
writeFile.close()
