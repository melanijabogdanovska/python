#finding factorial of a num
num = int(input("Enter a num "))
f = 1
if num < 0:
   print("Nqma factorial")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       f = f*i
       print(num,"*",i,"=",f)
print(num,f)