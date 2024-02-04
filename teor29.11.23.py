#stack

# stack = []
# stack.append("a")
# stack.append("b")
# stack.append("c")
# stack.append("d")
# stack.append("e")
#
# print(stack)
# stack.pop()
# print(stack)

# from collections import deque
# stack = deque()
# stack.append("a")
# stack.append("b")
# stack.append("c")
# print(stack)
# stack.pop()
# print(stack)


# from queue import LifoQueue
# stack = LifoQueue(maxsize=3)
#
# stack.put("a")
# stack.put("b")
# stack.put("c")
# print(stack.full())
# print(stack.qsize())
# print(stack.get())


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = Node("head")
#         self.size = 0
#     def __str__(self):
#         cur = self.head.next
#         out = ""
#         while cur:
#             out += str(cur.value) + " -> "
#             cur = cur.next
#         return out[:-4]
#     def getSize(self):
#         return self.size
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def peek(self):
#         if self.isEmpty():
#             raise Exception("stack is empty")
#         return self.head.next.value
#
#     def push(self, value):
#         node = Node(value)
#         node.next = self.head.next
#         self.head.next = node
#         self.size += 1
#
#     def pop(self):
#         if self.isEmpty():
#             raise Exception("stack is empty - 2")
#         remove = self.head.next
#         self.head.next = self.head.next.next
#         self.size -= 1
#         return remove.value
#
# stack = Stack()
# for i in range(1, 11):
#     stack.push(i)
# print(stack)


#ПРАКТИКА

def check_brackets(text):
    stack = []
    for char in text:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack or not is_matching(stack.pop(), char):
                return False
    return len(stack) == 0

def is_matching(opening, closing):
    return opening == '(' and closing == ')' or \
           opening == '{' and closing == '}' or \
           opening == '[' and closing == ']'



test = ["()", "[[{}]]", "{[}]", "((())"]
for t in test:
    result = check_brackets(t)
    print(result)
