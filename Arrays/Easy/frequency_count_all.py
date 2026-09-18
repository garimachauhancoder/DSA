n = int(input("Enter total no. of elements: "))
a = []
for i in range(n):
    num = int(input(f"Element {i}:"))
    a.append(num)

visited = []
for i in range(n):
    if a[i] in visited:
        continue
    count = 0
    for j in range(n):
        if a[i]==a[j]:
            count +=1
    print(f"Count of {a[i]} element is: {count}")
    visited.append(a[i])