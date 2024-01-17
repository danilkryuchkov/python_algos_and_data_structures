#stack is just a list in python. gotta use specific methods on it
#push = append() 
#pop = pop
#peek = [-1]

#exsamples
if __name__ == "__main__":
    #create a stack
    stack = []
    #push to stack
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    

    #print the stack
    print("Stack:")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    #[1,2,3,4,5] but sice it is a stack (LIFO),
    # we think of it as ->[5,4,3,2,1]
        
    #pop from stack
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    #print the stack
    print("Stack:")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])

    #peek at stack
    print("Peeked:", stack[-1])

    #print the stack
    print("Stack:")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])

    #push to stack
    stack.append(6)
    stack.append(7)

    #print the stack
    print("Stack:")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])

    #peek at stack
    print("Peeked:", stack[-1])

    #print the stack
    print("Stack:")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])

    #pop from stack
    