class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
            
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def peekvalue(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]
        
    def size(self):
        if self.isEmpty():
            return "Stack is empty"
        return len((self.stack))
    
    
myStack = Stack()


myStack.push("Prince")
myStack.push("Edwin")
myStack.push("Kekeli")
print("My Stack: ", myStack.stack)

myStack.pop()

print("Peek value is: ", myStack.peekvalue())

print("Size of stack: ",myStack.size())


print("The Stack is empty: ", myStack.isEmpty())
print("My Stack: ", myStack.stack)    