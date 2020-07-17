import sys

class Stack(object):
    
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(Stack):
    """
    Definition for class MaxStack that extends the class Stack
    
    To use:
    max_stack=MaxStack()
    print("Max stack", max_stack.items)
    """
    
    # https://leetcode.com/articles/max-stack/
    # Complexity Analysis:
    # Time Complexity: O(N) for the popMax operation, and O(1) for the other operations.
    # N is the number of operations performed.
    # Space Complexity: O(N), the maximum size of the stack.
    
    def __init__(self):
        """Initialize an empty stack"""
        #m is value of the largest element in the stack
        self.m = -sys.maxsize-1
        super().__init__()

    def push(self, x):
        """Push a new item onto the stack"""
        self.m=max(x,self.m)
        super().push(x)
        
    def get_max(self):
        """
        Return the last item without removing it
        
        To test this function,
        Example:
        #Stack([1,5,9,3])
        max_stack=MaxStack()
        max_stack.push(1)
        max_stack.push(5)
        max_stack.push(9)
        max_stack.push(3)
        print("Max value", max_stack.get_max())
        
        """
        # Time Complexity: O(1)
        return self.m
    
    def pop_max(self):
        """
        Retrieve the maximum element in the stack, and remove it.
        If you find more than one maximum elements, only remove the top-most one.
        
        To test this function,
        Example:
        #Stack([1,5,9,3])
        max_stack=MaxStack()
        max_stack.push(1)
        max_stack.push(5)
        max_stack.push(9)
        max_stack.push(3)
        max_stack.pop_max()
        print("Popped Max stack", max_stack.items)
        
        """
        # Time Complexity: O(n)
        # We can pop all items and push the popped elements that is not max back on the stack.
        
        t_stack=Stack()
        
        t_item=self.pop()
        
        # pop all items
        while (t_item):
            if (t_item != self.m):
                t_stack.push(t_item)
            t_item=self.pop()
        
        # reset new max value
        self.m = -sys.maxsize-1
        
        # push the popped elements back on the stack.
        t_item=t_stack.pop()
        while (t_item):
            self.push(t_item)
            t_item=t_stack.pop()

#Stack([-12, 1, 5, 3, -9, 9, -9])
max_stack=MaxStack()
max_stack.push(-12)
max_stack.push(1)
max_stack.push(5)
max_stack.push(3)
max_stack.push(3)
max_stack.push(-9)
max_stack.push(9)
max_stack.push(-9)
print("Max stack", max_stack.items)
print("Max value", max_stack.get_max())
max_stack.pop_max()
print("Popped Max stack", max_stack.items)
print("Max value", max_stack.get_max())


max_stack.pop_max()
print("Popped Max stack", max_stack.items)
print("Max value", max_stack.get_max())

max_stack.pop_max()
print("Popped Max stack", max_stack.items)
print("Max value", max_stack.get_max())

print(max_stack.pop())
print("Popped stack", max_stack.items)
print("Max value", max_stack.get_max())
