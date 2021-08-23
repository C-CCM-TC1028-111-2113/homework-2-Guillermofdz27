
def main():
    #Escribe tu código debajo de esta línea
 edad= int(input("Ingresa tu edad "))   
if edad <18:
    print("No cumples con  los requisitos")
    w=0
elif edad >= 18:
    w= str(input("Tienes identificación oficial "))
    if w == ("s"):
        print("Tramite de licencia concedido")
    elif w == ("n"):
        print("No cumples con los requisitos")
    else:
        print("Respuesta incorrecta")
    pass


if __name__ == '__main__':
    main()
