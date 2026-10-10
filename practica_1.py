import random
import calendar

año = random.randint(1900, 2026)
#Evaluar si un valor es par
if año % 2 == 0:
    print(f"El año {año} es par")
#Evual si un valor es bisiesto 
print(f"Es bisiesto el año {año}: {calendar.isleap(año)}")

