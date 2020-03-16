import os
import sys_logging

# os.chdir() Python os module changes the current working directory to the path we specify.
os.chdir('/home/stephen/Documents')
# os.access(path, mode) This method uses the real uid/gid to test for access to a path. If access is allowed, it returns True. Else, it returns False.
sys_logging.info('Find temp.txt in Documents: ' + str(os.access('temp.txt', os.F_OK)))
sys_logging.info('temp.txt in Documents is readable: ' + str(os.access('temp.txt', os.R_OK)))
sys_logging.info('temp.txt in Documents is writable: ' + str(os.access('temp.txt', os.W_OK)))
sys_logging.info('temp.txt in Documents is executable: ' + str(os.access('temp.txt', os.X_OK)))
# os.open(file, flag[, mode]) will open the file ‘file’, and will set flags based on the specified flags.
fd = os.open('temp.txt', os.O_RDWR)
sys_logging.info(fd)
# closes the associated file with descriptor fd.
os.close(fd)
