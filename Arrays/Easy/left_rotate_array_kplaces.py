n=int(input("Enter the no. of elements: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)

k = int(input("Enter the position with which rotate should start: "))
temp = [0]*k
# temp variable me value ka storage
for i in range(k):
    temp[i] = a[i]
# shifting of rest values of the array
for i in range(k, n):
    a[i-k] = a[i]
# placing of k array elements to original array at the back
j=0
for i in range(n-k, n):
    a[i] = temp[j]
    j+=1

print("Rotated Array: ", a)
