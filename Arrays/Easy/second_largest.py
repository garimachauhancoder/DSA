# If same nuumber are not present into the array then this approach 1 would be successful.
# Approach 1:
# n = int(input("Enter the no. of lines: "))
# a=[]
# for i in range(n):
#     num = int(input(f"Element {i+1}: "))
#     a.append(num)

# largest = a[n-1]
# second_largest = a[n-2]
# for i in range(n-2,0):
#     if a[i]!=largest:
#         second_largest=a[i]
#         break
# print("Second largest element: ", second_largest)

# Approach 2:
n = int(input("Enter the no. of lines: "))
a=[]
for i in range(n):
    num=int(input(f"Element {i+1}: "))
    a.append(num)

largest = a[0]
for i in range(n):
    if a[i]>largest:
        largest=a[i]

second_largest = -1
for i in range(n):
    if a[i]>second_largest and a[i]!=largest:
        second_largest = a[i]
        break
print("Second largest element is: ", second_largest)
