n = int(input("Enter the no. of lines: "))
for i in range(n):
    # spaces
    for j in range(n-i-1):
        print(" ", end = " ")
    
    # numbers
    for j in range((2*i)+1):
        print(i+1, end =" ")
    
    # spaces
    for j in range(n-i-1):
        print(" ", end=" ")
    print()