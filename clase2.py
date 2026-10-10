import random

edad = random.(-50, 50)

if edad < 0:
    print(f"el numero es: {edad}")
    print("el numero es negativo")
else:
    print(f"La edad es: {edad}")
    print("el numero es positivo")
    
    if edad >= 18:
        print("es mayor de edad")                    
    else:
        print("es menor de edad")

if edad % 2 == 0:
    print("es un numero par")
else:
    print("es un numero impar")



print("fin")
