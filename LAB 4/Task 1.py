# Implement stack using Python

stack=[]

#Push
stack.append(5)
stack.append(45)
stack.append(89)
stack.append(14)

print("Stack: ", stack)

#Pop
print("Popped: ", stack.pop())

print("Stack after pop: ", stack)

#Top Element 
print("Top Element: ", stack[-1])

#check empty

if len(stack)==0:
    print("Stack is empty!")
else:
    print("stack is not empty!")   
stack.reverse()
print("Reversed:", stack) 


# Reverse 
stack=[]

string=input("Enter a string: ")

for ch in string:
    stack.append(ch)

    reverse = " "
while stack:
    reverse+=stack.pop()
print("Reversed String: ", reverse)