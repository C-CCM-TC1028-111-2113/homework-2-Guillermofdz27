def main():
    #escribe tu código abajo de esta línea
a= int(input("Ingresa el primer numero "))
b= int(input("Ingresa el segundo numero "))
c= int(input("ingresa el tercer numero "))
if a > (b and c):
    print(a)
elif b > (a and c):
    print(b)
elif c > ( a and b):
    print(c)
    pass


if __name__=='__main__':
    main()
