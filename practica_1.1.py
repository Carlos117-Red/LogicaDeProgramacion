edad = int(input("Ingrese su edad: "))

print(f"Es usted mayor de edad con {edad} años?\n{edad >= 18}")

if edad < 18:
    print("No puede pasar, porque es menor de edad ")
else:
    print("Usted es mayor de edad, puede pasar")
