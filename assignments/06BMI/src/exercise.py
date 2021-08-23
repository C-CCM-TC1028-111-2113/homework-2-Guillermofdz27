def main():
    #escribe tu código abajo de esta línea
peso= float(input("Introduce tu peso en kg: "))
altura= float(input("Introduce tu altura en m: "))
if altura <=0 or peso <= 0:
    print("Revisa tus datos, alguno de ellos es erroneo")
else:
    IBM= (peso)/(altura**2)
    if IBM < 20:
        print("PESO BAJO")
    elif IBM >= 20 and IBM < 25:
        print("NORMAL")
    elif IBM >= 25 and IBM < 30:
        print("SOBREPESO")
    elif IBM >= 30 and IBM < 40:
        print("OBESIDAD")
    else:
        print("OBESIDAD MORBIDA")
    pass
if __name__=='__main__':
    main()
