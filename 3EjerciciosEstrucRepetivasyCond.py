#1. Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares.

numPares = 0
numImpares = 0
sumaPares = 0

for i in range(4):
    numero =int(input("Ingrese 4 números para evaluarlos: "))
    if numero % 2 == 0:
        numPares += 1
        sumaPares += numero
    else:
        numImpares += 1    

print("Cantidad de números pares: ", numPares)
print("Cantidad de números impares: ", numImpares)
print("Suma de los números pares: ", sumaPares)



#2. Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.

cantMayor100 = 0
cantMenor100 = 0
numMax = float('-inf')
numMin = float('inf')

for i in range(10):
    numero = float(input("Ingrese 10 números: "))
    
    if numero > 100:
        cantMayor100 += 1
    elif numero < 100:
        cantMenor100 += 1
    
    if numero > numMax:
        numMax = numero
    
    if numero < numMin:
        numMin = numero

print("Cantidad de números mayores a 100:", cantMayor100)
print("Cantidad de números menores a 100:", cantMenor100)
print("Número máximo:", numMax)
print("Número mínimo:", numMin)



#3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son
#mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad.

sexoFem = 0
sexoMasc = 0
mayor18 = 0
menor18 = 0

for i in range (15):
    sexo = input("Ingrese el sexo (F para femenino, M para masculino): ")
    edad = int(input("Ingrese la edad: "))

    if sexo == "F" or sexo == "f":
        sexoFem += 1
    elif sexo == "M" or sexo == "m":
        sexoMasc += 1

    if edad >= 18:
        mayor18 +=1
    else:
        menor18 +=1
     
print("Cantidad de mujeres:", sexoFem)
print("Cantidad de varones:", sexoMasc)
print("Cantidad de personas mayores de edad:", mayor18)
print("Cantidad de personas menores de edad:", menor18)



#4. Leer 10 números y mostrar solamente los números positivos, y su
#sumatoria.

sumaNum = 0

for i in range(10):
    numero = float(input("Ingrese 10 números positivos: "))
    if numero >= 0:
        sumaNum += numero
    else:
        print("Por favor ingrese un valor positivo")    
  
print("La suma de los números positivos ingresados es:", sumaNum)    



#5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
#números


