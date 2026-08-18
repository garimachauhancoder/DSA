n = int(input("Enter no. of the lines: "))
num=1
for i in range(n):
    for j in range(i+1):
        print(num, end= " ")
        num = num+1
    print()