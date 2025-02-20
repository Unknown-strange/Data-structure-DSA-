#7090921
#Amege Blessing Kwaku Obinna 

class stack_class:
    def _init_(self,expression):
        self.expression = expression
        
    def is_balanced(self):
        stack = []
        mapping = {')':'(',
                   '}':'{',
                   ']':'['}
        
        for char in self.expression:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
                
        return len(stack) == 0
    
    def postfix(self):
        stack = []
        
        for char in self.expression.split():
            if char.isdigit():
                stack.append(int(char))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression")
                
                a = stack.pop()
                b = stack.pop()
                
                if char == '+':
                    stack.append(a+b)
                elif char == '-':
                    stack.append(a-b)
                elif char == '/':
                    stack.append(a/b)
                elif char == '*':
                    stack.append(a*b)
        return stack.pop()
    
    

expre1 = stack_class("{[()]}")
print(expre1.is_balanced())

expre2 = stack_class("{[(]}")  
print(expre2.is_balanced())

expre3 = stack_class("3 4 + 5 * 6 / ")
print(expre3.postfix())

expre4 = stack_class("10 2 + 4 - ")  
print(expre4.postfix())