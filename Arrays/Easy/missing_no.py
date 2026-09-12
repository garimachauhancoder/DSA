n=int(input("Enter the no. of elements: "))
a=[]
for i in range(n):
    num = int(input(f"Element {i}: "))
    a.append(num)

expected_sum = n*(n+1) // 2
actual_sum=0
for i in range(n-1):
    actual_sum += a[i]

missing = expected_sum - actual_sum
print("Missing Number: ", missing)