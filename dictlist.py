n=int(input("Enter a num: "))
dicti={}
for i in range(n):
    key=input()
    value=input()
    dicti[key]=value
m=int(input("Enter a num: "))
lista=[]
for i in range(m):
    lista.append(input("Enter a value for list"))
print(dicti, lista)
for i in range(len(lista)):
    if lista[i]  in dicti.keys():
        a=lista[i]
        lista[i]=dicti[lista[i]]
        dicti.pop(a)
        print(dicti, lista)
