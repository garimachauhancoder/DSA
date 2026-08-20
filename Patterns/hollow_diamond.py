n = int(input("Enter the no. of lines: "))
# Upper half
for i in range(n):
    # outer spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    if i == 0:
        print("*")
    else:
        # left star
        print("*", end=" ")
        # inner spaces
        for j in range(2 * i - 1):
            print(" ", end=" ")
        # right star
        print("*")

# Lower half
for i in range(n - 2, -1, -1):
    # outer spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    if i == 0:
        print("*")
    else:
        # left star
        print("*", end=" ")
        # inner spaces
        for j in range(2 * i - 1):
            print(" ", end=" ")
        # right star
        print("*")