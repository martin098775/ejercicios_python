# ejecicio 
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
def suma(num1, num2):
    return num1 + num2

resultado = suma(num1, num2)
print(resultado)

# ejecicio 2

nombre = input("Ingresa tu nombre: ")
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar(nombre)

# ejecicio 3

num3 = int(input("Ingresa un numero: "))
def ver(num3):
    if num3 % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

ver(num3)