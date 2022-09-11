import math

a=float(input("Digite um valor para a: "))
b=float(input("Digite um valor para b: "))
c=float(input("Digite um valor para c: "))

delta=b**2-4*a*c

if delta==0:
    raiz01=(-b+ math.sqrt(delta))/(2*a)
    print("A única raiz é: ",raiz01)
else:
    if delta<0:
        print("Esta equação não possiu raízes reais")
    else:
        raiz01=(-b+ math.sqrt(delta))/(2*a)
        raiz02=(-b- math.sqrt(delta))/(2*a)
        print("A primeira raiz é :",raiz01)
        print("A Segunda raiz é :",raiz02)
