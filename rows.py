n=eval(input("enter rows"))

# Outer loop controls the number of rows
for i in range(n):
    # Inner loop controls the number of stars/numbers printed in each row
    for j in range(i):
        print(i, end=" ")
    # Move to the next line after each row is complete
    print()