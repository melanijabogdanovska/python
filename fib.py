#fibonacci
n=int(input("Enter a num"))
f1=0
print("Fibonacci:", f1, end=" ")
for i in range(1,10):
    f3 = f1 + n
    f1 = n
    n = f3
    print(f3, end=" ")

