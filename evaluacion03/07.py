def conversion(centimetros):
    metros = centimetros/100
    milimetros = centimetros*10
    pulgadas = centimetros/2.54

    print("Usted ingreso:",centimetros," centimetros y su equivalente")
    print("en metros es: ",metros)
    print("en milimetros es: ", milimetros)
    print("y en pulgadas es: ", pulgadas)

conversion(50)
