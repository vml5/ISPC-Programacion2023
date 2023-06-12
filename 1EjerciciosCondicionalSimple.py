#1)Realice un programa que solicite dos letras ingresadas por el usuario y
#verifique si son iguales o no, mostrando un mensaje.

letra1 = (input("Ingrese una letra: "))
letra2 = (input("Ingrese una letra: "))

if letra1 == letra2:  
   print ("Ambos datos son iguales")
else:
    print ("Ambos datos son diferentes")




#2)Hacer un programa que permita decidir si dos palabras son iguales o
#diferentes. Mostrar mensaje por pantalla

palabra1=input("Ingrese una palabra: ")
palabra2=input("Ingrese una palabra: ")

if palabra1==palabra2:
    print("Ambas palabras son iguales")
else:
    print("Ambas palabras son diferentes")




#3)Realizar un programa que permita ingresar “f” o “m” y determinar si vota
#en mesa femenina o masculina.

f = "mesa femenina"
m = "mesa masculina"

print("Ingrese F si usted es mujer o M si usted es varón, para determinar en qué mesa votará:")
genero = input()

if genero == "f":
    print(f)
else:
    print(m)



#4)Realice un programa que lea dos números y diga cuál es el mayor.

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

if numero1 > numero2:
    print (numero1 ," es mayor que " ,numero2)
else:
    print (numero2, "es mayor que ", numero1)



#5)Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
#el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa.

dolarHoy=490

cambio=(input("Ingrese:\n 1 si quiere convertir pesos a dólares o \n 2 si quiere hacer la operación inversa: "))
if cambio == '1':
    
    cantidad= float(input("Ingrese cuántos pesos desea convertir: "))
    dólares=cantidad/dolarHoy
    print("Usted obtendrá", dólares, "dólares.")

elif cambio == '2':
    cantidad = float(input("Ingrese cuántos dólares desea convertir: "))
    pesos = cantidad * dolarHoy
    print("Usted obtendrá", pesos, "pesos.")
    
else:
    print("Opción inválida. Por favor, ingrese 1 o 2.")

       

#6)Realice un programa donde el usuario ingrese su edad. Si es mayor de
#16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad=int(input("Ingrese su edad: "))

if edad >= 16:
    print ("Puede votar")
else:
    print("No vota")







