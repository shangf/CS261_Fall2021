# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 7
# Due Date: 12/3/2021
# Description: HashMap Implementation


# Import pre-written DynamicArray and LinkedList classes
from a7_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        This method clears the contents of the hash map. It does not change the underlying hash table capacity.
        """
        newBuckets = DynamicArray()
        for i in range(self.capacity):
            newBuckets.append(LinkedList())
        self.buckets = newBuckets
        # reset the size
        self.size = 0

    def get(self, key: str) -> object:
        """
        This method returns the value associated with the given key.
        If the key is not in the hash map, the method returns None.
        """
        index = (self.hash_function(key)) % self.capacity
        node = self.buckets[index].contains(key)
        value = None
        if node is not None:
            value = node.value
        return value

    def put(self, key: str, value: object) -> None:
        """
        This method updates the key / value pair in the hash map. If a given key already exists in the hash map, its
        associated value must be replaced with the new value.
        If a given key is not in the hash map, a key / value pair must be added.
        """
        # find the index of the key
        index = (self.hash_function(key)) % self.capacity
        # store the key in the linked list at the index
        # if the key is not in the linked list, insert a new node with the key and value
        if self.buckets[index].contains(key) is None:
            self.buckets[index].insert(key, value)
            self.size += 1
        # if the key is in the linked list, replace the associated value
        else:
            node = self.buckets[index].contains(key)
            node.value = value


    def remove(self, key: str) -> None:
        """
        This method removes the given key and its associated value from the hash map.
        If a given key is not in the hash map, the method does nothing (no exception is raised).
        """
        # find the index for the key
        index = (self.hash_function(key)) % self.capacity
        node = self.buckets[index].contains(key)
        if node is not None:
            self.buckets[index].remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        This method returns True if the given key is in the hash map. Otherwise returns False.
        An empty hash does not contain any keys.
        """
        # if the hash is empty
        if self.size == 0:
            return False

        # get the index for the key
        index = (self.hash_function(key)) % self.capacity
        node = self.buckets[index].contains(key)
        if node is not None:
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        This method returns the number of empty buckets in the hash table.
        """
        empty_buckets = 0
        for index in range(self.capacity):
            # if the length of the linked list is 0, then the bucket is empty
            if self.buckets[index].length() == 0:
                empty_buckets += 1
        return empty_buckets

    def table_load(self) -> float:
        """
        This method returns the current hash table load factor.
        Load factor = total number of elements stored in the hash table divided by the number of buckets.
        """
        load_factor = self.size / self.capacity
        return load_factor

    def resize_table(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the internal hash table.
        All existing key / value pairs must remain in the new hash map and all hash table links must be rehashed.
        If new_capacity is less than 1, the method should do nothing.
        """
        # if new capacity is less than 1
        if new_capacity < 1:
            return None

        new_buckets = DynamicArray()
        for index in range(new_capacity):
            new_buckets.append(LinkedList())

        # create a dynamic array of keys
        keys_DA = self.get_keys()
        # rehash all the keys to put into new linked lists
        while keys_DA.length() > 0:
            key = keys_DA.pop()
            value = self.get(key)
            index = (self.hash_function(key)) % new_capacity
            new_buckets[index].insert(key, value)

        self.buckets = new_buckets
        self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        """
        This method returns a DynamicArray object that contains all keys stored in the hash map.
        The order of the keys in the DynamicArray object does not matter.
        """
        keys_array = DynamicArray()
        # go through each index of the hash map
        for index in range(self.capacity):
            # check if the linked list is not empty
            if self.buckets[index].length() > 0:
                # step through each node of the linked list using the Linked List class's iterator
                for node in self.buckets[index]:
                    keys_array.append(node.key)

        return keys_array


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)
    #
    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)
        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
