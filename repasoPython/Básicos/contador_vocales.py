# Programa para contar la cantidad de vocales en una palabra dada

# Solución al problema inicial
def vowels(word):
    """Función que cuenta la cantidad de vocales presentes en una palabra
    (str) --> int"""
    cont = 0
    for i in range(len(word)):
        letra = word[i]
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            cont += 1
    return cont

def main():
    words = input("Ingrese las palabras que desea revisar separadas por espacios: ").split()
    for word in words: # Solución al problema que me puse (Ponerle para que revise varias palabras al tiempo) 
        print(f"La palabra {word} tiene {vowels(word)} vocales")
main()
