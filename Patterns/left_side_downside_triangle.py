n = int(input("Enter the number of lines: "))
i=0
j=0
for i in range(n):
    for j in range(n-i):
        print("* ", end=" ")
    print()
