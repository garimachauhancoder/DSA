n = int(input("Enter the no. of lines: "))
for i in range(n):
    if i%2==0:
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(i+1):
            print(j+1, end=" ")
    print()
             