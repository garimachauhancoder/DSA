n=int(input("Enter the no. of elements: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)

c = int(input("Element needs to search:"))

for i in range(n):
    if a[i] == c:
        print(f"Element {c} found at index no.: ",i)