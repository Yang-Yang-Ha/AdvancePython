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


def broadcasting():
    a = np.array([1, 2, 3])
    b = np.array([[0, 0, 0], [10, 20, 30]])
    sys_logging.info(a + b)


def iterating_over_array():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    sys_logging.info(a)
    for x in np.nditer(a, flags=['c_index']):
        sys_logging.info(x)

    # broadcasting iterating
    sys_logging.info(f'start broadcasting iterating')
    b = np.array([1, 2, 3, 4])
    for x, y in np.nditer([a, b]):
        sys_logging.info(f'{x}:{y}')


def stack():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    sys_logging.info(f'hstack \n {np.hstack((a, b))}')
    sys_logging.info(f'vstack \n {np.vstack((a, b))}')
    sys_logging.info(f'stack axis = 0 \n {np.stack((a, b))}')
    sys_logging.info(f'stack axis = 1 \n {np.stack((a, b), axis=1)}')


def joining_arrays():
    # concatenate: Joins a sequence of arrays along an existing axis
    # stack: Joins a sequence of arrays along a new axis
    # hstack: Stacks array in sequence horizontally(column wise)
    # vstack: Stacks array in sequence vertically(row wise)
    concatenate()

    stack()


def concatenate():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    sys_logging.info(f'concatenate axis = 0 \n {np.concatenate((a, b))}')
    sys_logging.info(f'concatenate axis = 1 \n {np.concatenate((a, b), axis=1)}')


def splitting_arrays():
    # split(array, indices or sections, axis): splits an array into multiple sub-arrays
    # hsplit: splits an array into multiple sub-arrays horizontally,
    # is a special case of split() function
    # where axis is 1 indicating a horizontal split regardless of the dimension of the input array.
    # vsplit: splits an array into multiple sub-arrays vertically,
    # is a special case of split() function
    # where axis is 1 indicating a vertical split regardless of the dimension of the input array.
    a = np.arange(9)
    b = np.split(a, 3)
    c = np.split(a, [4, 7])
    sys_logging.info(f'b_type = {type(b)} b = {b}')
    sys_logging.info(f'c_type = {type(c)} c = {c}')
    d = np.arange(16).reshape((4, 4))
    sys_logging.info(f'np.vsplite(d, 2) = {np.vsplit(d, 2)}')


def adding_or_removing_elements():
    # resize: returns a new array with a specified shape
    # append: appends the values to the end of an array
    # insert(array, index, value, axis): inserts the values along the given axis before the given indices
    # delete: returns a new array with sub-arrays along an axis deleted
    # unique(array, return_index, return_inverse, return_counts): finds the unique elements of an array
    resize()

    append()

    insert()

    delete()

    unique()


def unique():
    sys_logging.info('np.unique')
    a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
    sys_logging.info(f'a = {a}')
    sys_logging.info(np.unique(a))
    u, indices = np.unique(a, return_index=True)
    sys_logging.info(f'u = {u}, indices = {indices}')
    u, indices = np.unique(a, return_inverse=True)
    sys_logging.info(f'u = {u}, indices = {indices}')
    sys_logging.info(f'u[indices] = {u[indices]}')
    u, indices = np.unique(a, return_counts=True)
    sys_logging.info(f'u = {u}, indices = {indices}')


def delete():
    sys_logging.info('np.delete')
    d = np.arange(12).reshape((3, 4))
    sys_logging.info(d)
    sys_logging.info(np.delete(d, 5))
    sys_logging.info(np.delete(d, 1, axis=0))
    e = np.arange(10)
    sys_logging.info(np.delete(e, np.s_[::2]))


def insert():
    sys_logging.info('np.insert')
    c = np.array([[1, 2], [3, 4], [5, 6]])
    sys_logging.info(np.insert(c, 3, [7, 8]))
    sys_logging.info(np.insert(c, 3, [7, 8], axis=0))
    sys_logging.info(np.insert(c, 2, [7, 8, 9], axis=1))


def append():
    sys_logging.info('np.append')
    b = np.array([[1, 2, 3], [4, 5, 6]])
    sys_logging.info(np.append(b, [7, 8, 9]))
    sys_logging.info(np.append(b, [[7, 8, 9]], axis=0))
    sys_logging.info(np.append(b, [[5, 5, 5], [7, 8, 9]], axis=1))


def resize():
    sys_logging.info('np.resize')
    a = np.arange(6)
    sys_logging.info(np.resize(a, (2, 8)))


def array_manipulation():
    change_shapes()

    transpose_operation()

    change_dimensions()

    joining_arrays()

    splitting_arrays()

    adding_or_removing_elements()


def change_dimensions():
    # Changing dimensions
    # broadcast: Produce an object that mimics broadcasting
    # broadcast_to: Broadcast an array to a new shape
    # expand_dims: Expands the shape of an array
    # squeeze: Removes single-dimensional entries from the shape of array
    sys_logging.info(f'Changing dimensions')
    broadcast()
    broadcast_to()
    expand_dims()
    squeeze()


def squeeze():
    h = np.arange(9).reshape((1, 3, 3))
    h_squeeze = np.squeeze(h)
    sys_logging.info(f'\n {h}')
    sys_logging.info(f'\n {h_squeeze}')


def expand_dims():
    d = np.array([[1, 2], [3, 4]])
    e = np.expand_dims(d, axis=0)
    f = np.expand_dims(d, axis=1)
    g = np.expand_dims(d, axis=2)
    sys_logging.info(f'shape = {e.shape} \n {e}')
    sys_logging.info(f'shape = {f.shape} \n {f}')
    sys_logging.info(f'shape = {g.shape} \n {g}')


def broadcast_to():
    c = np.arange(4).reshape(1, 4)
    c_broadcast = np.broadcast_to(c, (4, 4))
    sys_logging.info(c_broadcast)


def broadcast():
    x = np.array([[1], [2], [3]])
    y = np.array([4, 5, 6])
    b = np.broadcast(x, y)
    for i in b:
        sys_logging.info(i)
    sys_logging.info(x + y)


def transpose_operation():
    # transpose operation
    # transpose(): np.transpose(ndarray), permutes the dimensions of an array
    # ndarray.T: Same as self.transpose
    # rollaxis: rolls the specified axis backwards
    # swapaxis: Interchange the two axis of an array
    sys_logging.info(f'Transpose operation')
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    sys_logging.info(a.T)


def change_shapes():
    # changing shapes:
    # reshape(): Gives a new shape to an array without changing its data
    # flat: A 1-D iterator over the array
    # flatten(): returns a copy of the array collapsed into one dimension
    # ravel(): returns a contiguous flattened array
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    sys_logging.info(a)
    sys_logging.info(a.flat[3])
    sys_logging.info(a.ravel())


if __name__ == '__main__':
    # nd_array_object()
    # data_types()
    # array_attributes()
    # array_creation_routines()
    # array_from_existing_data()
    # array_from_numerical_ranges()
    # indexing_and_slicing()
    # broadcasting()
    # iterating_over_array()
    array_manipulation()
