# If same nuumber are not present into the array then this app. would be successful.
n = int(input("Enter the no. of lines: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i+1}: "))
    a.append(num)

largest = a[n-1]
second_largest = a[n-2]
for i in range(n-2,0):
    if a[i]!=largest:
        second_largest=a[i]
        break
print("Second largest element: ", second_largest)