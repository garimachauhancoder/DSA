n = int(input("Enter no. of elements:"))
a = []
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)
i=1
while i<len(a):
    if a[i] == a[i-1]:
        a.pop(i)
    else:
        i +=1
    

print("After removal array is: ", a)