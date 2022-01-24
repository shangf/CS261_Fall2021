
# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 10/18/2021
# Description: Bag ADT Implementation with Dynamic Array

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag.
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method removes any one element from the bag that matches the value object.
        Returns True if an object was removed.
        Returns False if no object was removed.
        """
        for i in range(self.da.length()):
            if self.da[i] == value:
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the bag that match the provided value object.
        """
        count = 0
        for i in range(self.da.length()):
            if self.da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        This method clears the contents of the bag.
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        This method compares the contents of a bag with the contents of a second bag.
        Returns True if bags are equal.
        Returns False if bags are not equal.
        """

        if self.da.length() == 0 and second_bag.da.length() == 0:
            return True

        # test if bags have same number of elements
        if self.da.length() != second_bag.da.length():
            return False

        elementNotFound = False

        # check the number of times each element shows up in each bag
        for i in range(self.da.length()):
            first_count = self.count(self.da[i])
            for index in range(second_bag.da.length()):
                if self.da[i] == second_bag.da[index]:
                    elementNotFound = False
                    second_count = second_bag.count(second_bag.da[index])
                    if first_count != second_count:
                        return False
                    break
                else:
                    elementNotFound = True
            if elementNotFound:
                return False
        return True

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    bag3 = Bag([1, 1, 2])
    bag4 = Bag([2, 1, 1])
    print(bag1, bag2, bag3, bag4, sep="\n")
    print(bag1.equal(bag2))
    print(bag3.equal(bag4))
    print(bag1, bag2, bag3, bag4, sep = "\n")
