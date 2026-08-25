n = int(input("Enter the no. of lines: "))
a=[]
for i in range(n):
    num = int(input("Enter element: "))
    a.append(num)

largest = a[0]
for i in range(1,n):
    if a[i]>largest:
        largest = a[i]

print("Largest element:", largest)