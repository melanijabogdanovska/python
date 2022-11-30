#finding average of list
def avg (lst, mnozitel='1'):

    if not mnozitel.isnumeric():
        print('Mnozitel must be a number')
        return

    mnozitel = int(mnozitel)
    counter = 0
    sum = 0

    for element in lst:
        if type(element)==int or type(element)==float or element.isnumeric():
            element = int(element)
            sum += element * mnozitel
            counter += 1
    if counter == 0:
        print('Error')
        return

    return sum / counter
m=int(input("How much  "))
lst=[]
for i in range(m):
    lst.append(input("Enter: "))
print(lst)
b=avg(lst)
print(b)


    
