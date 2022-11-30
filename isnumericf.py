def input_nums(n):
    if not n.isnumeric():
        return list()

    n=int(n)
    nums_list=list()
    for i in range(n):
        a=input("Enter a list element: ")
        if a.isnumeric():
            nums_list.append(int(a))

    return nums_list
def sum_list(lst):
    sum=0
    

    for element in lst:
        if type(element)==int or type(element)==float or element.isnumeric():
            num=float(element)
            sum+=num
            

    return sum
def max_of_two(a, b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a if a >= b else b
        return a

    if type(b) == int or type(b) == float: return b

    return
n=input()
a=input_nums(n)
print(a)
m=int(input("How much "))
lst=[]
for i in range(m):
    lst.append(input("enter a value"))
b=sum_list(lst)
print(b)
c=int(input())
d=int(input())
g=max_of_two(c, d)
print(g)