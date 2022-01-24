# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 10/25/2021
# Description: Linked List and ADT Implementation


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self._next = None
        self._value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        self._tail = SLNode(None)
        self._head._next = self._tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self._head._next != self._tail:
            cur = self._head._next._next
            out = out + str(self._head._next._value)
            while cur != self._tail:
                out = out + ' -> ' + str(cur._value)
                cur = cur._next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self._head
        while cur._next != self._tail:
            cur = cur._next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head._next == self._tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel).
        """
        # if linked list is empty
        if self.is_empty():
            self._head._next = SLNode(value)
            current = self._head._next
            current._next = self._tail
        # if linked list is not empty
        else:
            previous = self._head._next
            self._head._next = SLNode(value)
            current = self._head._next
            current._next = previous


    def add_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list (right before the back sentinal).
        """
        length = self.length()
        #if linked list is empty
        if self.is_empty():
            self._head._next = SLNode(value)
            current = self._head._next
            current._next = self._tail
        # if linked list is not empty
        # traverse the list to find last node
        else:
            current = self._head._next
            while current._next is not self._tail:
                current = current._next
            current._next = SLNode(value)
            current._next._next = self._tail

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specific index position in the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).

        If index is invalid, raises a SSLException
        N nodes exclude sentinel nodes. Valid Indices are [0, N], inclusive.
        """
        if index > self.length() or index < 0:
            raise SLLException

        # if linked list is empty
        if self.is_empty():
            self._head._next = SLNode(value)
            current = self._head._next
            current._next = self._tail
        # if linked list is not empty
        # traverse until the given index and insert a new node at the current index
        else:
            current = self._head._next
            previous = self._head
            for i in range(index):
                previous = current
                current = current._next
            # if the current node is the tail sentinel
            if current is self._tail:
                current = SLNode(value)
                current._next = self._tail
                previous._next = current
            # if current node is not the tail sentinel
            else:
                previous._next = SLNode(value)
                previous._next._next = current

    def remove_front(self) -> None:
        """
        This method removes the first node from the list.
        If the list is empty (not including the sentinels), the method raises a SLLException.
        """
        # if list is empty
        if self.is_empty():
            raise SLLException
        # get the first node's next value and set it the head's next value
        removed_node = self._head._next
        self._head._next = removed_node._next

    def remove_back(self) -> None:
        """
        This method removes the last node from the list.
        If the list is empty (not including the sentinels), the method raises SLLException.
        """
        if self.is_empty():
            raise SLLException

        current = self._head._next
        previous = self._head
        while current._next is not self._tail:
            previous = current
            current = current._next
        previous._next = self._tail

    def remove_at_index(self, index: int) -> None:
        """
        This method removes a node from the list given its index.
        Index 0 refers to the beginning of the list (right after the sentinel).
        If the index is invalid, raises SSLException.
        N elements do not include sentinel nodes.
        Valid indices are [0, N-1] inclusive.
        """
        if index < 0 or index >= self.length():
            raise SLLException

        current = self._head._next
        previous = self._head
        current_index = 0
        while current._next is not self._tail and current_index < index:
            previous = current
            current = current._next
            current_index += 1
        previous._next = current._next

    def get_front(self) -> object:
        """
        This method returns the value from the first node (after the front sentinel) in the list without removing it.
        If the list is empty, the method raises SLLException.
        """
        if self.is_empty():
            raise SLLException
        first_node = self._head._next
        return first_node._value

    def get_back(self) -> object:
        """
        This method returns the value from the last node in the list (before the back sentinel) without removing it.
        If the list is empty, the method raises SLLException.
        """
        if self.is_empty():
            raise SLLException
        current = self._head._next
        while current._next is not self._tail:
            current = current._next
        return current._value

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end and removes the first node in the list that
        matches the provided "value" object.
        Returns True if a node was removed.
        Returns False if a node was not removed.
        """
        current = self._head._next
        previous = self._head
        while current is not self._tail:
            if current._value == value:
                previous._next = current._next
                return True
            previous = current
            current = current._next
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided "value" object.
        """
        counter = 0
        current = self._head._next
        while current is not self._tail:
            if current._value == value:
                counter += 1
            current = current._next
        return counter

    def slice(self, start_index: int, size: int) -> object:
        """
        This method returns a new LinkedList object that contains the requested number of nodes from the original list,
        starting with the node located at the requested start index.
        N is the number of nodes in the linked list.
        Valid start_index is in the range of [0, N-1] inclusive.

        If start_index is invalid or if there are not enough nodes between the start_index and end index, the method
        raises a SLLException.
        """
        if start_index < 0 or start_index >= self.length() or size > (self.length() - start_index) or size < 0:
            raise SLLException

        newLinkedList = LinkedList()
        current = self._head._next
        # go to the node at the start_index
        for i in range(start_index):
            current = current._next

        index = 0
        while index < size:
            newLinkedList.insert_at_index(index, current._value)
            current = current._next
            index += 1

        return newLinkedList

if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F'), (4, 'X'), (2, 'T')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
    print(list)
    for i in range(12):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")
