año = int(input("Introduzca el año de nacimiento: "))

if año > 1900:
    if año % 4 == 0:
        print(f"El año {año} es bisiesto")
        n_dias = 366
    else:
        print(f"El año {año} NO es bisiesto")
        n_dias = 365 

    print(f"el año {año} tiene {n_dias} dias")
else:
    print("El año es invalido")
