import numpy as np

import sys_logging


# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object Any object exposing the array interface method returns an array, or any (nested) sequence
# dtype desired data type of array, optional
# copy by default (true), the object is copied, optional
# order C(row major) or F(column major) or A(any)(default)
# subok by default, returned array forced to be a base class array, If true, sub-classes passed through
# ndmin specifics minimum dimensions of resultant array
def nd_array_object():
    a = np.array([1, 2, 3])
    sys_logging.info(a)
    b = np.array([[1, 2], [3, 4]])
    sys_logging.info(b)
    c = np.array([1, 2, 3, 4, 5], ndmin=2)
    sys_logging.info(c)
    d = np.array([1, 2, 3, 4], dtype=complex)
    sys_logging.info(d)


# numpy.dtype(object, align, copy)
# Object − To be converted to data type object
# Align − If true, adds padding to the field to make it similar to C-struct
# Copy − Makes a new copy of dtype object. If false, the result is reference to builtin data type object
def data_types():
    dt_a = np.dtype(np.int32)
    sys_logging.info(dt_a)

    # int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
    dt_b = np.dtype('i4')
    sys_logging.info(dt_b)

    # '<' means that encoding is little-endian; '>' means that encoding is big-endian
    dt_c = np.dtype('<i4')
    sys_logging.info(dt_c)

    dt_d = np.dtype([('age', np.int8)])
    sys_logging.info(dt_d)
    array_d = np.array([10, 20, 30], dtype=dt_d)
    sys_logging.info(array_d)

    # Each built - in data type has a character code that uniquely identifies it.
    # 'b' − boolean
    # 'i' − (signed) integer
    # 'u' − unsigned integer
    # 'f' − floating - point
    # 'c' − complex - floating point
    # 'm' − timedelta
    # 'M' − datetime
    # 'O' − (Python) objects
    # 'S', 'a' − (byte -) string
    # 'U' − Unicode
    # 'V' − raw
    # data(void)
    dt_student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    sys_logging.info(dt_student)
    students = np.array([('stephen', 10, 34), 20, 30], dtype=dt_student)
    sys_logging.info(students)


def array_attributes():
    # shape
    shape_array = np.array([[1, 2, 3], [4, 5, 6]])
    sys_logging.info(shape_array.shape)
    shape_array.shape = (3, 2)
    # shape_array.reshape(2, 3)
    sys_logging.info(shape_array)

    # ndim
    ndim_array = np.arange(24)
    sys_logging.info(f'{ndim_array} + {ndim_array.ndim}')
    ndim_array_b = ndim_array.reshape((2, 4, 3))
    sys_logging.info(f'{ndim_array_b} + {ndim_array_b.ndim}')

    # itemsize
    item_size_array = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    sys_logging.info(item_size_array.itemsize)
    item_size_array_4_byte = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    sys_logging.info(item_size_array_4_byte.itemsize)


# Shape
# Shape of an empty array in int or tuple of int
# Dtype
# Desired output data type. Optional
# Order
# 'C' for C-style row-major array, 'F' for FORTRAN style column-major array
def array_creation_routines():
    x = np.empty([3, 2], dtype=int)
    sys_logging.info(x)
    y = np.zeros(5)
    sys_logging.info(y)
    z = np.zeros([5, ], dtype=int)
    sys_logging.info(z)
    a = np.zeros([2, 2], dtype=[('x', 'i4'), ('y', 'i4')])
    sys_logging.info(a)


def array_from_existing_data():
    x = [(1, 2, 3), (2, 3, 4)]
    a = np.asarray(x, dtype=float)
    sys_logging.info(a)
    # s = 'Hello World'
    # b = np.frombuffer(s, dtype='S1')
    # sys_logging.info(b)
    list_a = range(5)
    it = iter(list_a)

    # use iterator to create ndarray
    c = np.fromiter(it, dtype=float)
    sys_logging.info(c)


def array_from_numerical_ranges():
    # np.arange(start, stop, step, dtype)
    # start: the start of an interval. If omitted, defaults to 0
    # stop: the end of an interval. (not including this number)
    # step: Spacing between values, default is 1
    # dtype: data type of resulting ndarray. If not given, data type of input is used.
    x = np.arange(5)
    sys_logging.info(x)
    y = np.arange(10, 20, 2)
    sys_logging.info(y)
    # np.linspace(start, stop, num, endpoint, retstep, dtype)
    # start: the starting value of the sequence
    # stop: the end value of the sequence, included in the sequence if endpoint set to true
    # num: the number of evenly spaced samples to be generated. Default is 50
    # endpoint: True by default, hence the stop value is included in the sequence. If false, it is not include
    # retstep: If true, returns samples and step between the consecutive numbers
    # dtype: Data type of output ndarray
    z = np.linspace(10, 20, 5)
    sys_logging.info(z)
    a = np.linspace(10, 20, 5, endpoint=False)
    sys_logging.info(a)
    # np.logspace(start, stop, num, endpoint, base, dtype)
    # start: the starting point of the sequence is start's start
    # base: base of log space, default is 10
    b = np.logspace(1, 2, num=10)
    sys_logging.info(b)


def indexing_and_slicing():
    a = np.arange(10)
    sys_logging.info(a)
    s_1 = slice(2, 7, 2)
    sys_logging.info(a[s_1])
    sys_logging.info(a[2:7:2])
    sys_logging.info(a[0])
    sys_logging.info(a[2:])
    b = np.array([[1, 2, 3], [5, 6, 7], [8, 9, 10]])
    sys_logging.info(b[..., 2])
    sys_logging.info(b[1, ...])
    sys_logging.info(b[..., 1:])


if __name__ == '__main__':
    # nd_array_object()
    # data_types()
    # array_attributes()
    # array_creation_routines()
    # array_from_existing_data()
    # array_from_numerical_ranges()
    indexing_and_slicing()
