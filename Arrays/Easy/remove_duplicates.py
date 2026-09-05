n = int(input("Enter no. of elements:"))
a = []
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)

unique=[]
for i in range(n):
    if a[i] not in unique:
        unique.append(a[i])

print("After removal from full array:", unique)