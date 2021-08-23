def main():
    # Escribe el código adecuado para completar el programa
a= int(input("Ingresa el primer numero "))
b= int(input("Ingresa el segundo numero "))
c= int(input("ingresa el tercer numero "))
if a > b > c:
    print(str(c))
    print(str(b))
    print(str(a))
if a > c > b:
    print(str(b))
    print(str(c))
    print(str(a))
elif b > a > c:
    print(str(c))
    print(str(a))
    print(str(b))
elif b > c > a:
    print(str(a))
    print(str(c))
    print(str(b))
elif c > a > b:
    print(str(b))
    print(str(a))
    print(str(c))
elif c > b > a:
    print(str(a))
    print(str(b))
    print(str(c))
    pass


if __name__=='__main__':
    main()
