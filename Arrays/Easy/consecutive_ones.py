n = int(input("Enter total no. of elements: "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i}]: ")))

count=0
maximum =0 
for i in range(n):
    if a[i]==1:
        count += 1
        if count > maximum:
            maximum = count
    
    else:
        count = 0

print("Maximum consecutive 1s:", maximum)