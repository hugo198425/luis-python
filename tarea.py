def evaluar_numero(numero):
    if numero == 10:
        print("El numero ingresado es 10")
    elif numero == 7:
        print("Se ha ingresado un comodin")
    elif numero % 2 == 0:
        print("El numero ingresado es par") 
    else:
        print("El numero ingresado es impar")

def main():
    entrada = int(input("Ingrese el numero a evaluar: "))
    evaluar_numero(entrada)

# Llamada a la función principal
main()