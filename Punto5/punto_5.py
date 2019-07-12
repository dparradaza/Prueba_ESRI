# Funcion que muestra los numeros pares
def pares(n):
    print ("Pimeros ",n," números pares:")
    for i in range(0,(n*2),2):
        print (i)
#Funcion que muestra los numeros impares
def impares(n):
    print ("Primeros ",n,"números impares:")
    for i in range(1,(n*2),2):
        print (i)
#Funcion que muestra los numeros primos
def primos(n):
    print ("Primeros ",n,"números primos:")
    contador=0
    primos=0
    while (primos < n):
        if (es_primo(contador)):
            print(contador)
            primos=primos+1
        contador=contador+1
#Funcions que valida si un numero es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    n = int(input("Ingrese un numero n: "))
    if (n > 0):
        pares(n)
        impares(n)
        primos(n)



if __name__ == "__main__":
    main()
