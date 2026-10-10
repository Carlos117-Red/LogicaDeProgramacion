print("P: para modalidad presencial => 60")
print("O: para modalidad online en vivo => 50")
print("G: para modalidad clases grabadas => 30")

modalidad = input("Escriba la modalidad que desea: ")

if modalidad.lower() == "p":
    precio = 60
elif modalidad.lower() == "o":
    precio = 50
elif modalidad.lower() == "g":
    precio = 30 
else:
    precio = -1

if precio != -1:
    edad = int(input("Ingrese su edad: "))
    if edad <= 13:
        desc = 50
        print("Le corresponde un descuento")
    else:
        desc = 0
        print("No le corresponde un descuento")
        
    monto_desc = precio * desc/100
    monto_pagar = precio - monto_desc
    print(f"el monto a pagar es {monto_pagar}$")
else:
    print("ERROR. Modalidad incorrecta")