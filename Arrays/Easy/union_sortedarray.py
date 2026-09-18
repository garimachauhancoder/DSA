n = int(input("Enter size of first array: "))
a = []

for i in range(n):
    a.append(int(input(f"a[{i}]: ")))

m = int(input("Enter size of second array: "))
b = []

for i in range(m):
    b.append(int(input(f"b[{i}]: ")))

i = 0
j = 0
union = []

while i < n and j < m:

    if a[i] < b[j]:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    elif b[j] < a[i]:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1

    else:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1
        j += 1

while i < n:
    if len(union) == 0 or union[-1] != a[i]:
        union.append(a[i])
    i += 1

while j < m:
    if len(union) == 0 or union[-1] != b[j]:
        union.append(b[j])
    j += 1

print("Union:", union)