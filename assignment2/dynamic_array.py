# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 10/18/2021
# Description: Implementing Dynamic Arrays

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the underlying storage for the array elements.
        """

        if new_capacity <= 0 or new_capacity < self.length():
            return None

        # create a new static array
        newArr = StaticArray(new_capacity)
        index = 0

        # if the new_capacity is smaller than the StaticArray's current length
        if new_capacity < self.data.length():
            while index < new_capacity:
                newArr[index] = self.data[index]
                index += 1
        else:
        # transfer over the values from the previous static array
            while index < self.data.length():
                newArr[index] = self.data[index]
                index += 1

        # set new capacity to the current array's capacity
        self.capacity = new_capacity
        # set the current data to refer to the newly created Static Array
        self.data = newArr


    def append(self, value: object) -> None:
        """
        This method adds a new value at the end of the dynamic array.
        If the internal storage is already full, the capacity gets doubled.
        """
        # if no resize is necessary, then simply append
        if self.size <= self.data.length() - 1:
            self.data[self.size] = value
            self.size += 1

        # if size is equal to capacity, must double the capacity
        else:
            self.resize(self.data.length() * 2)
            self.append(value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index position in the dynamic array.
        If the internal storage is full, the capacity gets doubled before adding a new value.
        """

        if index < 0 or index > self.size:
            raise DynamicArrayException

        # handles cases when inserting into an empty array
        if self.size == index and self.size < self.data.length():
            self.data[index] = value
            self.size += 1
            return

        # handles cases when inserting at the last index in the array
        if self.size == index and self.size >= self.data.length():
            self.resize(self.data.length() * 2)
            self.data[index] = value
            self.size += 1
            return

        # move the last element in the static array to the back
        for i in range(self.size, index, -1):
            if self.size <= self.data.length() - 1:
                self.data[i] = self.data[i - 1]
            else:
                self.resize(self.data.length() * 2)
                self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the element at the specified index from the dynamic array.
        Capacity will be reduced if the number of elements in the array is strictly less than .25 of the current capacity.
        """
        if index < 0 or index > self.size - 1:
            raise DynamicArrayException

        # if number of elements is strictly less than .25 of the current capacity
        # capacity must be reduced to 2 * number of elements
        saved_capacity = self.capacity

        if self.capacity < 10:
            pass
        elif self.size < (.25 * self.capacity):
            self.capacity = self.size * 2
            # if the capacity reaches below 10, move it back up to 10
            if self.capacity < 10:
                self.capacity = (10 - self.capacity) + self.capacity
        # remove the element
        self.size -= 1
        # shift over every element after the index
        for i in range(index + 1, self.data.length()):
            self.data[i - 1] = self.data[i]


    def slice(self, start_index: int, size: int) -> object:
        """
        This method returns a new Dynamic array object that contains the requested number of elements
        from the original array, starting with the element located at the requested start index.
        """
        if start_index < 0 or size < 0 or start_index + size > self.size or start_index == self.size:
            raise DynamicArrayException

        newArr = DynamicArray()
        for i in range(start_index, start_index + size):
            newArr.append(self.data[i])

        return newArr

    def merge(self, second_da: object) -> None:
        """
        This method takes another Dynamic Array object as a parameter.
        It appends all elements from the second array to the current one. Ordering doesn't change.
        """
        for i in range(second_da.length()):
            self.append(second_da[i])

    def map(self, map_func) -> object:
        """
        This method creates a Dynamic Array where the value of each element is derived by applying a given
        map_func  to the corresponding value from the original array.
        """
        newArr = DynamicArray()
        for i in range(self.size):
            newArr.append(map_func(self.data[i]))

        return newArr

    def filter(self, filter_func) -> object:
        """
        This method creates a new Dynamic Array populated only with those elements from the original array for which
        filter_func returns True.
        """
        newArr = DynamicArray()
        for i in range(self.size):
            if filter_func(self.data[i]):
                newArr.append(self.data[i])
        return newArr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the Dynamic Array and returns the resulting
        value.
        """
        if self.size == 0:
            return initializer

        noParam = False

        if initializer is None:
            noParam = True
            initializer = self.data[0]

        value = initializer
        if noParam:
            for i in range(self.size - 1):
                value = reduce_func(value, self.data[i + 1])
        else:
            for i in range(self.size):
                value = reduce_func(value, self.data[i])

        return value

# ------------------- BASIC TESTING -----------------------------------------

#
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
