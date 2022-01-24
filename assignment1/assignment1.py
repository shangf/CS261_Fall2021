# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 10/11/2021
# Description: Assignment 1 - Python Fundamentals Review

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    Function that receives a one dimensional array of integers and returns a Python tuple of two values:
    returns (minimum, maximum)
    """
    # finding highest (maximum)
    highest = arr[0]
    for index in range(1, arr.length()):
        if highest < arr[index]:
            highest = arr[index]

    # finding lowest (minimum)
    lowest = arr[0]
    for index in range(1, arr.length()):
        if lowest > arr[index]:
            lowest = arr[index]

    return (lowest, highest)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Function that receives a StaticArray of integers and returns a new StaticArray object.
    The returned StaticArray object contains integers, "fizz", "buzz", or "fizzbuzz" depending on the integer's multiples.
    """
    # creating a new StaticArray object
    newArray = StaticArray(arr.length())

    # stepping through the given StaticArray to add values to the new StaticArray
    for index in range(arr.length()):
        if ((arr[index] % 3 == 0) and (arr[index] % 5 != 0)):
            newArray[index] = 'fizz'
        elif ((arr[index] % 5 == 0) and (arr[index] % 3 != 0)):
            newArray[index] = 'buzz'
        elif ((arr[index] % 3 == 0) and (arr[index] % 5 == 0)):
            newArray[index] = 'fizzbuzz'
        else:
            newArray[index] = arr[index]
    return newArray


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Function that receives a StaticArray and reverses the order of the elements in the array.
    The reversal is done in place, meaning the original input array will be modified.
    """
    # end_index = the last index of the StaticArray
    end_index = arr.length() - 1
    # swapping the beginning and end indexes of the StaticArray until the middle index
    for index in range(arr.length() // 2):
        temp = arr[end_index - index]
        arr[end_index - index] = arr[index]
        arr[index] = temp

# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Function that receives two parameters: a StaticArray and an integer value (called steps).
    The function will create and return a newStaticArray, where all of the elements are from the original array,
    but their positions will be shifted right or left, depending on the number of steps.
    """
    # creating a new StaticArray named newArray
    newArray = StaticArray(arr.length())

    # copying the values from the input StaticArray into newArray
    for i in range(arr.length()):
        newArray[i] = arr[i]

    # using the remainder to determine the number of rotations
    numRotations = steps % arr.length()

    if numRotations == 0:
        return newArray
    else:
        # creating a StaticArray named savedArray to save the ending portion of the original StaticArray
        # savedArray will represent the beginning portion of newArray
        savedArray = StaticArray(numRotations)
        savedIndex = arr.length() - numRotations
        # fill in the savedArray, which will get pasted into the beginning of newArray
        for i in range(savedArray.length()):
            savedArray[i] = arr[savedIndex]
            savedIndex += 1
        #filling in newArray, starting from the last index of savedArray
        startIndex = 0
        for index in range(savedArray.length(), newArray.length()):
            newArray[index] = arr[startIndex]
            startIndex += 1
        #filling in the beginning of newArray with savedArray's values
        for index in range(savedArray.length()):
            newArray[index] = savedArray[index]
    return newArray

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Function that receives two integers start and end and returns a StaticArray that contains all the consecutive
    integers between start and end.
    """
    # counter used to keep track of array size
    counter = 0
    startingValue = start

    # determining the size of the array by incrementing counter for each value in between start and end
    if start <= end:
        while (startingValue <= end):
            counter += 1
            startingValue += 1
    else:
        while (end <= startingValue):
            counter += 1
            startingValue -= 1

    # creating a StaticArray named newArray
    newArray = StaticArray(counter)

    # if starting value is less than or equal to ending value, the array will be ascending
    if (start <= end):
        for index in range(newArray.length()):
            newArray[index] = start
            start += 1
    # if starting value is greater than the ending value, the array will be descending
    else:
        for index in range(newArray.length()):
            newArray[index] = start
            start -= 1

    return newArray

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Function that receives a StaticArray and returns an integer that describes whether the array is sorted.
    1 if the array is sorted in strictly ascending order.
    -1 if the list is sorted in strictly descending order.
    0 otherwise.
    """

    if arr.length() == 1:
        return 1
    else:
    # test whether array is sorted in strictly ascending order
        ascending = True
        descending = False
        for index in range(arr.length() - 1):
            if arr[index] >= arr[index + 1]:
                ascending = False
                descending = True

    # test whether array is sorted in strictly descending order
        for index in range(arr.length() - 1):
            if arr[index] <= arr[index + 1]:
                descending = False

    # finished testing ascending and descending. returns corresponding value
        if ascending is True:
            return 1
        if descending is True:
            return -1
        if ascending is False and descending is False:
            return 0

# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    Function that receives a StaticArray and sorts its content in non-descending order.
    The original array is sorted and the function does not return anything.
    """
    # using selection sort
    # traverse through all arrays
    for index in range(arr.length()):
        min_index = index
        # find the minimum element in the remaining unsorted array
        for next_index in range(index + 1, arr.length()):
            if arr[min_index] > arr[next_index]:
                min_index = next_index
        # swapping minimum element found at min_index with the element at index
        temp = arr[index]
        arr[index] = arr[min_index]
        arr[min_index] = temp

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Function that receives a StaticArray where the elements are already in sorted order.
    Returns a new StaticArray with all of the duplicated values removed.
    Original array is not modified.
    """
    if arr.length() == 1:
        newArray = StaticArray(arr.length())
        newArray[0] = arr[0]
        return newArray
    else:
        copiedArray = StaticArray(arr.length())
        # inputting the first value of the original array into the copy array
        copiedArray[0] = arr[0]
        arrSize = 1
        # traverse through the array to determine any duplicates
        for index in range(arr.length() - 1):
            if arr[index] != arr[index + 1]:
                arrSize += 1
                copiedArray[index + 1] = arr[index + 1]

        newArray = StaticArray(arrSize)

        # copying the first value of the original array into the first value of newArray
        newArray[0] = arr[0]
        # because 0th index is filled, the current index that needs to be filled is now 1
        arrIndex = 1
        counter = 0
        while (arrIndex != arrSize):
            tempIndex = arrIndex + counter
            # if the next value in copiedArray is None or if the preceding element in newArray is equal to the current
            # value of the copiedArray (means that they are duplicates), increment to next available index
            while (copiedArray[tempIndex]) is None or newArray[arrIndex-1] == copiedArray[tempIndex]:
                tempIndex += 1
                counter += 1
            newArray[arrIndex] = copiedArray[tempIndex]
            arrIndex += 1
        return newArray


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    Function that receives a StaticArray and returns a new StaticArray with the same content.
    Sorted in non-ascending order.
    Original array is not modified
    """
    # finding the maximum value in the given array
    max = arr[0]
    for i in range(1, arr.length()):
        if max < arr[i]:
            max = arr[i]

    # finding the minimum value in the given array
    min = arr[0]
    for i in range(1, arr.length()):
        if min > arr[i]:
            min = arr[i]

    # create new array to count the number of distinct elements
    distinctArray = StaticArray(max - min + 1)
    for i in range(distinctArray.length()):
        distinctArray[i] = 0

    # counting the totals of each distinct element
    for i in range(arr.length()):
        if arr[i] == max:
            distinctArray[0] += 1
        elif arr[i] == min:
            distinctArray[distinctArray.length() - 1] += 1
        else:
            distinctArray[max - arr[i]] += 1

    # adding from left to right, starting at the first index
    for i in range(1, distinctArray.length()):
        distinctArray[i] += distinctArray[i - 1]

    # creating a new array to transfer values from distinctArray
    transferArray = StaticArray(distinctArray.length())
    for i in range(transferArray.length()):
        transferArray[i] = 0

    # moving the values of distinctArray, one index over to the right, into transferArray
    for i in range(1, transferArray.length()):
        transferArray[i] = distinctArray[i-1]

    # creating the sorted array
    sortedArray = StaticArray(arr.length())

    # placing the values in their correct positions and increasing the corresponding index position by 1
    for i in range(arr.length()):
        if arr[i] == min:
            savedIndex = transferArray[transferArray.length() - 1]
            transferArray[transferArray.length() - 1] += 1
        elif arr[i] == max:
            savedIndex = transferArray[0]
            transferArray[0] += 1
        else:
            savedIndex = transferArray[max - arr[i]]
            transferArray[max - arr[i]] += 1
        sortedArray[savedIndex] = arr[i]
    return sortedArray


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3**14)
    rotate(arr, -3**15)
    print(f'Finished rotating large array of {array_size} elements')


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')


    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')
