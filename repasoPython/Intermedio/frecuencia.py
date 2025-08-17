# Programa para calcular la frecuencia de los caracteres en una cadena

def hz(cadena):
    frecuencias = []
    for i in cadena:
        cont = 0
        for j in cadena:
            if i == j:
                cont += 1
        tupla = (i,cont)
        frecuencias.append(tupla)

    return list(set(frecuencias))  # Esto es para eliminar las repeticiones

def imprimir_lindo(lista):
    for i in lista:
        letra = i[0]
        repe = i[1]
        print(f"La letra {letra} está un total de {repe} veces/vez en la cadena ingresada")

def main():
    cadena = input().strip()
    imprimir_lindo(hz(cadena))
main()