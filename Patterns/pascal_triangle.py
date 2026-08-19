n = int(input("Enter the no. of lines: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end= " ")
    
    num=1
    for j in range(i+1):
        print(num, end=" ")
        num = num*(i-j)//(j+1)
    print()