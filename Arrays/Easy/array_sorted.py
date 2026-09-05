n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    num = int(input(f"Element {i}:"))
    a.append(num)

for i in range(1,n):
    if a[i]>=a[i-1]:
        pass
    else:
        print("False")
        break
else:
    print("True")