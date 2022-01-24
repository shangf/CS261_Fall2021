# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 11/23/2021
# Description: MinHeap Implementation

# Import DynamicArray from Assignment 2
from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self.heap[i] for i in range(self.heap.length())]
        return 'HEAP ' + str(heap_data)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def getLeftChildIndex(self, parentIndex):
        """
        Helper function that returns the index of the node's left child.
        """
        return parentIndex * 2 + 1

    def getRightChildIndex(self, parentIndex):
        """
        Helper function that returns the index of the node's right child.
        """
        return parentIndex * 2 + 2

    def getParentIndex(self, childIndex):
        """
        Helper function that returns the index of the node's parent.
        """
        return (childIndex - 1) // 2

    def findSmallestChild(self, leftChildIndex, rightChildIndex):
        """
        Helper function that returns the smallest child index.
        If the values are the same, then returns the index of the left child.
        """
        if rightChildIndex > self.heap.length() - 1:
            return leftChildIndex

        if self.heap[leftChildIndex] < self.heap[rightChildIndex]:
            return leftChildIndex

        if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
            return rightChildIndex

        if self.heap[leftChildIndex] == self.heap[rightChildIndex]:
            return leftChildIndex

    def swap(self, indexOne, indexTwo):
        """
        Helper function that swaps two elements in the Dynamic Array.
        """
        temp = self.heap[indexOne]
        self.heap[indexOne] = self.heap[indexTwo]
        self.heap[indexTwo] = temp

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap maintaining heap property.
        Runtime complexity of this implementation must be O(log N).
        """
        self.heap.append(node)
        currentIndex = self.heap.length() - 1
        parentIndex = self.getParentIndex(currentIndex)

        # begin percolating up
        while parentIndex >= 0 and self.heap[currentIndex] < self.heap[parentIndex]:
            self.swap(currentIndex, parentIndex)
            currentIndex = self.getParentIndex(currentIndex)
            parentIndex = self.getParentIndex(currentIndex)

    def get_min(self) -> object:
        """
        This method returns an object with a minimum key without removing it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        Runetime complexity must be O(1).
        """
        if self.heap.is_empty():
            raise MinHeapException

        return self.heap[0]

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        """
        if self.heap.is_empty():
            raise MinHeapException

        minValue = self.heap[0]
        lastIndex = self.heap.length() - 1
        self.swap(0, lastIndex)
        self.heap.remove_at_index(lastIndex)

        currentIndex = 0
        leftChildIndex = self.getLeftChildIndex(currentIndex)
        rightChildIndex = self.getRightChildIndex(currentIndex)
        # find the index of smallest child
        smallestIndex = self.findSmallestChild(leftChildIndex, rightChildIndex)
        # begin perculating down
        while smallestIndex < self.heap.length() and self.heap[currentIndex] > self.heap[smallestIndex]:
            self.swap(currentIndex, smallestIndex)
            currentIndex = smallestIndex
            leftChildIndex = self.getLeftChildIndex(currentIndex)
            rightChildIndex = self.getRightChildIndex(currentIndex)
            smallestIndex = self.findSmallestChild(leftChildIndex, rightChildIndex)

        return minValue

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a dynamic array with objects in any order and builds a proper MinHeap from them.
        """
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(da[i])
        # find the first non-leaf subtree
        nonLeafIndex = (self.heap.length() // 2) - 1

        for index in range(nonLeafIndex, -1, -1):
            leftChildIndex = self.getLeftChildIndex(index)
            rightChildIndex = self.getRightChildIndex(index)
            smallestIndex = self.findSmallestChild(leftChildIndex, rightChildIndex)
            currentIndex = index
            # percolate down
            while smallestIndex < self.heap.length() and self.heap[currentIndex] > self.heap[smallestIndex]:
                self.swap(currentIndex, smallestIndex)
                currentIndex = smallestIndex
                leftChildIndex = self.getLeftChildIndex(currentIndex)
                rightChildIndex = self.getRightChildIndex(currentIndex)
                smallestIndex = self.findSmallestChild(leftChildIndex, rightChildIndex)

    @staticmethod
    def heapsort(da: DynamicArray) -> None:
        """
        Function that receives a DynamicArray object and sorts its content in non-ascending order.
        Sorts the array in place without creating a new array.
        Does not return anything.
        """
        # build the heap out of the array
        nonLeafIndex = (da.length() // 2) - 1

        for index in range(nonLeafIndex, -1, -1):
            currentIndex = index
            leftChildIndex = index * 2 + 1
            rightChildIndex = index * 2 + 2
            smallestIndex = leftChildIndex
            if rightChildIndex < da.length() and da[rightChildIndex] < da[leftChildIndex]:
                smallestIndex = rightChildIndex
            # percolate down
            while smallestIndex < da.length() and da[currentIndex] > da[smallestIndex]:
                # swap the values
                temp = da[currentIndex]
                da[currentIndex] = da[smallestIndex]
                da[smallestIndex] = temp
                # update the currentIndex to the child index
                currentIndex = smallestIndex
                # find the next left and right child
                leftChildIndex = smallestIndex * 2 + 1
                rightChildIndex = smallestIndex * 2 + 2
                # find the next smallest child
                smallestIndex = leftChildIndex
                if rightChildIndex < da.length() and da[rightChildIndex] < da[leftChildIndex]:
                    smallestIndex = rightChildIndex

        # complete the sort
        # keep a running total called lastIndex - initialized to one less than the size of the array
        lastIndex = da.length() - 1

        while lastIndex > 0:
            # swap the element at the beginning of the array with the element at the last index
            temp = da[0]
            da[0] = da[lastIndex]
            da[lastIndex] = temp
            # decrement lastIndex
            lastIndex -= 1
            # setting up the first downward percolation
            currentIndex = 0
            leftChildIndex = currentIndex * 2 + 1
            rightChildIndex = currentIndex * 2 + 2
            # find the initial smallest child
            smallestIndex = leftChildIndex
            if rightChildIndex <= lastIndex and da[rightChildIndex] < da[leftChildIndex]:
                smallestIndex = rightChildIndex
            # being percolating down, stopping at the the lastIndex
            while smallestIndex <= lastIndex and da[currentIndex] > da[smallestIndex]:
                # swap the values
                temp = da[currentIndex]
                da[currentIndex] = da[smallestIndex]
                da[smallestIndex] = temp
                # move to the child index
                currentIndex = smallestIndex
                # find the next child indexes
                leftChildIndex = currentIndex * 2 + 1
                rightChildIndex = currentIndex * 2 + 2
                # find the next smallest child
                smallestIndex = leftChildIndex
                if rightChildIndex <= lastIndex and da[rightChildIndex] < da[leftChildIndex]:
                    smallestIndex = rightChildIndex

    def size(self) -> int:
        """
        This method returns the number of items currently stored in the heap.
        Runtime complexity of this implementation is O(1).
        """
        return self.heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap.
        Runtime complexity of this implementation is O(1).
        """
        self.heap = DynamicArray()


# BASIC TESTING
if __name__ == '__main__':
    print("zebra" > "bear")

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da[0] = 500
    print(da)
    print(h)
    #
    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    MinHeap.heapsort(da)
    print(f"After:  {da}")
    #
    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    MinHeap.heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
