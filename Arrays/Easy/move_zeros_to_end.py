n=int(input("Enter the no. of elements: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)
temp = []
for i in range(n):
    if a[i]!=0:
        temp.append(a[i])

# pick no. from temp and place in the front of a[]
for i in range(len(temp)):
    a[i] = temp[i]

# filling of zeros to end
for i in range(len(temp),n):
    a[i]=0

print("Array after shifting zeros to end using brute force approach: ",a)



### Optimal Approach
n=int(input("Enter the no. of elements: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)

j=0 #ye vo position hai jha pr non-zero elements ko place kra jayega
for i in range(n):
    if a[i]!=0:
        a[j], a[i] = a[i], a[j]
        j+=1

print("Array zeros movement at the back using optimal solution: ",a)