#1)Introducir los lados de un triángulo y visualizar por pantalla si dicho
#triángulo es equilátero, isósceles o escaleno.

lado1=float(input("Ingrese la medida de un lado del triángulo: "))
lado2=float(input("Ingrese la medida de otro lado del triángulo: "))
lado3=float(input("Ingrese la medida de otro lado del triángulo: "))
if lado1==lado2==lado3:
    print("Es un triángulo EQUILÁTERO")
elif lado1==lado2 or lado2==lado3 or lado3==lado1:
    print("Es un triángulo ISÓSCELES") 
else:
    print("Es un triángulo ESCALENO")
      


#2. Realice un programa que le permita al usuario simular el pago
#ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.

valorProducto = float(input("Ingrese el importe del producto: "))
opción=input("Ingrese la forma de pago deseada:\n 1 Contado -se aplicará un descuento del 10% -\n 2 Tarjeta -se aplicará un interés de 10% -\n 3 Débito -se aplicará un descuento del 5%")

if opción == '1':
    valorProducto = valorProducto-(valorProducto*0.1)
    print("El monto a abonar es:",valorProducto)
elif opción == '2':
    valorProducto = valorProducto * 0.1 + valorProducto
    print("El monto a abonar es:",valorProducto)
elif opción == '3':
    valorProducto = (valorProducto - valorProducto * 0.05)
    print("El monto a abonar es:",valorProducto)  
else:
    print("Ingrese una opción válida: 1, 2 o 3. Gracias!")    
    





#3. Realice un programa que lea tres números, muestre cuál es el mayor y
#determine si es par o impar.

num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))
num3=int(input("Ingrese otro número: "))

if num1>num2 and num1>num3:
    print(num1,"es el mayor")
    if num1 % 2 == 0:
        print(num1, "es par")
    else:
        print(num1, "es impar")
elif num2>num1 and num2>num3:
    print(num2,"es el mayor")
    if num2 % 2 == 0:
        print(num2, "es par")
    else:
        print(num2, "es impar")   
else:
    print(num3,"es el mayor")  
    if num3 % 2 == 0:
        print(num3, "es par")
    else:
        print(num3, "es impar")







#4. Confeccione un programa que pida un número del 1 al 7 y diga el día de
#la semana correspondiente.

lunes=1
martes=2
miércoles=3
jueves=4
viernes=5
sábado=6
domingo=7

dia=int(input("Ingrese un número del 1 al 7: "))
if dia==1:
    print("El día es lunes")
elif dia==2:
    print("El día es martes")
elif dia==3:
    print("El día es miércoles")
elif dia==4:
    print("El día es jueves")
elif dia==5:
    print("El día es viernes")
elif dia==6:
    print("El día es sábado")
elif dia==7:
    print("El día es domingo")
else:
    print("Ingrese un valor válido del 1 al 7") 





#5. Realice un programa que pida un número del 1 al 12 y diga el nombre
#del mes correspondiente

meses={1:"enero",
       2:"febrero",
       3:"marzo",
       4:"abril",
       5:"mayo",
       6:"junio",
       7:"julio",
       8:"agosto",
       9:"septiembre",
       10:"octubre",
       11:"noviembre",
       12:"diciembre"
       }

fecha=int(input("Ingrese un número del 1 al 12: "))
if fecha in meses:
    print("El mes es:",meses[fecha])
else:
    print ("Ingrese una opción válida del 1 al 12, por favor.")    
    


