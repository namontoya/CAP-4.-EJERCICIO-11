#Capitulo 4. Ejercicio resuelto 11

N1 = int(input("Ingrese el primer número entero: "))
N2 = int(input("Ingrese el segundo número entero: "))
N3 = int(input("Ingrese el tercer número entero: "))

if (N1 > N2) and (N1 > N3):
    print(f"EL VALOR MAYOR ENTRE: {N1}, {N2} Y {N3} es: {N1}")

elif (N2 > N1) and (N2 > N3):
    print(f"EL VALOR MAYOR ENTRE: {N1}, {N2} Y {N3} es: {N2}")
    
else:
    print(f"EL VALOR MAYOR ENTRE: {N1}, {N2} Y {N3} es: {N3}")
  
