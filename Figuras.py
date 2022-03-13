def circulo():
    print("Ingrese las medidas")
    radio = float(input("Ingrese el radio: "))
    area = 3.1416 * (radio * radio)
    area = round(area, 2)
    print("El área es: ", area)
    menu()

def cuadrado():
    print("Ingrese las medidas")
    lado = float(input("Ingresa el lado: "))
    area = lado * lado
    area = round(area, 2)
    print("El area es: ", area)
    menu()

def rectangulo():
    print("Ingrese las medidas")
    lado1 = float(input("Ingresa lado a: "))
    lado2 = float(input("Ingresa lado b: "))
    area = lado1 * lado2
    area = round(area, 2)
    print("El area es: ", area)
    menu()

def triangulo():
    print("Ingrese las medidas")
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    area = (base * altura) / 2
    area = round(area, 2)
    print("El area es: ", area)
    menu()

def trapecio():
    print("Ingrese las medidas")
    lado1 = float(input("Ingresa el lado a: "))
    lado2 = float(input("Ingresa el lado b: "))
    altura = float(input("Ingresa la altura: "))
    area = ((lado1 + lado2) * altura) / 2
    area = round(area, 2)
    print("El area es: ", area)
    menu()

def salir():
    print("Programa terminado")
    exit()

def menu():
    while True:
        print("\nSeleccione la figura:\n"
              "1) Círculo\n"
              "2) Cuadrado\n"
              "3) Rectángulo\n"
              "4) Triángulo\n"
              "5) Trapecio\n"
              "6) Salir\n")
        op = input("Opción: ")
        if op == '1':
            circulo()
        elif op == '2':
            cuadrado()
        elif op == '3':
            rectangulo()
        elif op == '4':
            triangulo()
        elif op == '5':
            trapecio()
        elif op == '6':
            salir()
        else:
            print("Error, vuelva a intentarlo")

menu()
