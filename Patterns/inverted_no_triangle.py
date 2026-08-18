n = int(input("Enter no. of lines: "))
for i in range(n+1):
    for j in range(1,n-i):
        print(j, end=" ")
    print()