# Name: Frank Shang
# OSU Email: shangf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 11/16/2021
# Description: AVL Tree Implementation

import random

class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Helper function for the add method. If the tree is empty, will insert at the root.
        If not, will call the add_rec function.
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.add_rec(value, self.root)

    def add_rec(self, value, node):
        """
        Recursive function that inserts a node into the tree. Then rebalances it and corrects the height of affected nodes.
        """
        if value == node.value:
            return
        # insert to the left if the value is less than the current node
        if value < node.value and node.left is None:
            node.left = TreeNode(value)
            node.left.parent = node
            # check rebalance
            n = node.left
            p = n.parent
            while p is not None:
                self.rebalance(p)
                p = p.parent
            return
        # insert to the right if the value is less than the current node
        if value > node.value and node.right is None:
            node.right = TreeNode(value)
            node.right.parent = node
            # check rebalance
            n = node.right
            p = n.parent
            while p is not None:
                self.rebalance(p)
                p = p.parent
            return

        # move to the left of the tree if value is less than current node and there is a left node
        if value < node.value and node.left is not None:
            self.add_rec(value, node.left)
            return

        # move to the right of the tree if value is greater than current node and if there is a right node
        if value > node.value and node.right is not None:
            self.add_rec(value, node.right)
            return

    def updateHeight(self, node):
        """
        This method updates the node's height.
        """
        if node.left is None:
            heightLeft = -1
        if node.right is None:
            heightRight = -1
        if node.left is not None:
            heightLeft = node.left.height
        if node.right is not None:
            heightRight = node.right.height

        if heightRight > heightLeft:
            maxHeight = heightRight + 1
        elif heightLeft > heightRight:
            maxHeight = heightLeft + 1
        else:
            maxHeight = heightRight + 1

        node.height = maxHeight

    def rotateLeft(self, node):
        """
        This method performs left rotations around the node parameter.
        """
        c_node = node.right
        node.right = c_node.left
        if node.right is not None:
            node.right.parent = node
        c_node.left = node
        temp_parent = node.parent
        if temp_parent is None:
            self.root = c_node
        c_node.parent = temp_parent
        node.parent = c_node
        self.updateHeight(node)
        self.updateHeight(c_node)
        return c_node

    def rotateRight(self, node):
        """
        This method performs right rotations around the node parameter.
        """
        c_node = node.left
        node.left = c_node.right
        if node.left is not None:
            node.left.parent = node
        c_node.right = node
        temp_parent = node.parent
        if temp_parent is None:
            self.root = c_node
        c_node.parent = temp_parent
        node.parent = c_node
        self.updateHeight(node)
        self.updateHeight(c_node)
        return c_node

    def rebalance(self, node):
        """
        This method rebalances the altered node.
        """
        balancefactor = self.balanceFactor(node)

        if balancefactor < -1:
            if self.balanceFactor(node.left) > 0:
                node.left = self.rotateLeft(node.left)
                node.left.parent = node
            newSubtreeRoot = self.rotateRight(node)
            if newSubtreeRoot.parent is not None:
                if newSubtreeRoot.parent.left is node:
                    newSubtreeRoot.parent.left = newSubtreeRoot
                if newSubtreeRoot.parent.right is node:
                    newSubtreeRoot.parent.right = newSubtreeRoot
        elif balancefactor > 1:
            if self.balanceFactor(node.right) < 0:
                node.right = self.rotateRight(node.right)
                node.right.parent = node
            newSubtreeRoot = self.rotateLeft(node)
            if newSubtreeRoot.parent is not None:
                if newSubtreeRoot.parent.right is node:
                    newSubtreeRoot.parent.right = newSubtreeRoot
                if newSubtreeRoot.parent.left is node:
                    newSubtreeRoot.parent.left = newSubtreeRoot
        else:
            self.updateHeight(node)

    def balanceFactor(self, node):
        """
        This method determines the balance factor.
        """
        if node.right is None:
            height_right = -1
        if node.left is None:
            height_left = -1
        if node.right is not None:
            height_right = node.right.height
        if node.left is not None:
            height_left = node.left.height
        return height_right - height_left

    def remove(self, value: object) -> bool:
        """
        This method should remove the value from the AVL tree.
        The method must return True if the value is removed from the AVL Tree, otherwise return False.
        """
        removeNode = self.find(value)

        if removeNode is None:
            return False

        if self.is_empty():
            return False

        # finds the successor node
        successorNode = removeNode.right
        if successorNode is not None:
            while successorNode.left is not None:
                successorNode = successorNode.left

        #test whether node has none children / whether the node is a leaf node
        if removeNode.left is None and removeNode.right is None:
            p = removeNode.parent
            # if the leaf node is the root node
            if p is None:
                self.root = None
            # if the leaf node is not the root node
            else:
                if removeNode.parent.left is removeNode:
                    removeNode.parent.left = None
                elif removeNode.parent.right is removeNode:
                    removeNode.parent.right = None

            while p is not None:
                self.rebalance(p)
                p = p.parent
            return True

        # test whether the node to remove has a right subtree
        if removeNode.left is None and removeNode.right is not None:
            p = removeNode.parent
            removeNode.right.parent = removeNode.parent
            # if the removed node is the root
            if removeNode.parent is None:
                self.root = removeNode.right
            else:
                # sets the parent of the removed node to point to the remove node's child
                if removeNode.parent.right == removeNode:
                    removeNode.parent.right = removeNode.right
                elif removeNode.parent.left == removeNode:
                    removeNode.parent.left = removeNode.right
            while p is not None:
                self.rebalance(p)
                p = p.parent
            return True

        # test whether the node to remove has a left subtree
        if removeNode.left is not None and removeNode.right is None:
            p = removeNode.parent
            removeNode.left.parent = removeNode.parent
            # if the removed node is the root
            if removeNode.parent is None:
                self.root = removeNode.left
            else:
                # sets the parent of the removed node to point to the remove node's child
                if removeNode.parent.right == removeNode:
                    removeNode.parent.right = removeNode.left
                if removeNode.parent.left == removeNode:
                    removeNode.parent.left = removeNode.left
            while p is not None:
                self.rebalance(p)
                p = p.parent
            return True

        # test whether the node to remove have a left and a right subtree
        if removeNode.left is not None and removeNode.right is not None:
            # p represents lowest modified node
            p = successorNode.parent
            # pn is the parent of the removed node
            pn = removeNode.parent
            # ps is the parent of the successor
            ps = successorNode.parent

            # begin switching the pointers around
            successorNode.left = removeNode.left
            successorNode.left.parent = successorNode
            # if the successor node is not the same node as the removed node's right
            if successorNode is not removeNode.right:
                ps.left = successorNode.right
                successorNode.right = removeNode.right
                # successor now replaces removedNode, so must update the parent of the successor's right child to point to the successor
                if successorNode.right is not None:
                    successorNode.right.parent = successorNode

                # if ps.left contains successor's subtree
                if ps.left is not None:
                    # successor's subtree must point to the successor's parent
                    ps.left.parent = ps
                    # lowest modified node should change
                    p = ps.left

            # if the successor node is the same as the removed node's right
            else:
                # lowest modified node will be the successor node, since the parent of successor node is the removed node
                p = successorNode

            # if the root being removed is the root
            if pn is None:
                # change the root to point to the successor node
                self.root = successorNode
                # change parent of successor to None
                successorNode.parent = None

            # if the node being removed is not the root
            else:
                # sets the parent of the removed node to point to the inorder successor node
                if pn.right == removeNode:
                    pn.right = successorNode
                if pn.left == removeNode:
                    pn.left = successorNode
                # sets the parent of the successor node to point to the removed node's parent
                successorNode.parent = removeNode.parent

            while p is not None:
                self.rebalance(p)
                p = p.parent
            return True

    def find(self, value):
        """
        Helper function that sets up the find_rec method to find a node.
        """
        return self.find_rec(value, self.root)

    def find_rec(self, value, node):
        """
        Function that recursively goes down the tree, to determine whether a node is in the tree.
        """
        if value == node.value:
            return node
        if value < node.value and node.left is None:
            return None
        if value > node.value and node.right is None:
            return None
        if value < node.value:
            return self.find_rec(value, node.left)
        if value > node.value:
            return self.find_rec(value, node.right)

    def contains(self, value: object) -> bool:
        """
        This method returns True if the value parameter is in the tree or False if it is not.
        If the tree is empty, the method should return False.
        """
        if self.is_empty():
            return False

        newQueue = self.inorder_traversal()
        while not newQueue.is_empty():
            if value == newQueue.dequeue():
                return True
        return False

    def inorder_traversal(self) -> Queue:
        """
        This method will perform an inorder traversal of the tree.
        Returns a Queue object that contians the values of the visited nodes, in the order they were visited.
        If the tree is empty, the methods should return an Empty Queue
        """
        newQueue = Queue()
        if self.is_empty():
            return newQueue

        else:
            return self.inorder_traversal_rec(self.root, newQueue)

    def inorder_traversal_rec(self, node, queue):
        """
        The inorder traversal recursion method that performs an inorder traversal and returns a Queue object.
        """
        if node is not None:
            self.inorder_traversal_rec(node.left, queue)
            queue.enqueue(node.value)
            self.inorder_traversal_rec(node.right, queue)
        return queue

    def find_min(self) -> object:
        """
        This method returns the lowest value in the tree.
        If the tree is empty, the method should return None.
        """
        if self.is_empty():
            return None

        maxQueue = self.inorder_traversal()
        return maxQueue.dequeue()

    def find_max(self) -> object:
        """
        This method returns the highest value in the tree.
        If the tree is empty, the method should return None.
        """
        if self.is_empty():
            return None

        maxQueue = self.inorder_traversal()

        numMax = None
        while not maxQueue.is_empty():
            numMax = maxQueue.dequeue()

        return numMax

    def is_empty(self) -> bool:
        """
        This method return True if the tree is empty, otherwise the method should return False.
        """
        if self.root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        This method removes all the nodes from the tree.
        """
        self.root = None


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL()
        for value in case:
            avl.add(value)
        if not avl.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')
    # #

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)
    #
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl, avl.root.value)
        avl.remove(avl.root.value)
        print('RESULT :', avl)
    #
    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL(case)
        for value in case[::2]:
            avl.remove(value)
        if not avl.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))
    #
    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())
    #
    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
