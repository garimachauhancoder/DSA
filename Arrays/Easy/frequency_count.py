n = int(input("Enter total no. of elements: "))
a = []
for i in range(n):
    num = int(input(f"Element {i}:"))
    a.append(num)

for i in range(n):
    count = 0
    for j in range(n):
        if a[i]==a[j]:
            count +=1
    if count==1:
        print(f"No. appearing only once", a[i]);
