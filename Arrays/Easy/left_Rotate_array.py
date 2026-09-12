n=int(input("Enter the no. of elements: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)

temp = a[0]
for i in range(1,n):
    a[i-1] = a[i]  
a[n-1] = temp
print("Array after shifting: ",a)