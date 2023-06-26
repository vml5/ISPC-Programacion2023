

#5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
#números


numeros = []

for i in range(15):
    numero = int(input("Ingrese un número negativo: "))
    while numero >= 0:
        numero = int(input("El número ingresado no es negativo. Por favor, ingrese un número negativo: "))
    
    numero = abs(numero)  # Convierte el número negativo a positivo
    numeros.append(numero)

print("Números positivos convertidos:")
for numero in numeros:
    print(numero)
