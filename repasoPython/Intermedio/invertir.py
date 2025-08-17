# Programa que invierte una cadena sin usar [::-1]

def flip(cadena):
    flipped = ""
    cont = -1
    for _ in cadena:
        ult = cadena[cont]
        flipped += ult
        cont -= 1
    return flipped

# Esta solución la dio chat gpt después de que le pedí que revisara el ejercicio.
# me pareció interesante el uso del range()
def flip2(cadena):
    flipped = ""
    for i in range(len(cadena) - 1, -1, -1):
        flipped += cadena[i]
    return flipped


def main():
    cadena = input().strip()
    print(flip(cadena))
main()
