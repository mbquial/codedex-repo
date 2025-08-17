# Programa para saber si una palabra es palíndroma

def palindroma(p):
    """Función que verifica si una palabra es palíndroma usando ciclos
    (str) --> str"""
    inicio = 0
    fin = len(p) - 1 
    for _ in range(len(p)):
        if p[inicio] != p[fin]:
            return "NO ES PALÍNDROMA"
        else:
            inicio += 1
            fin -= 1
    return "ES PALÍNDROMA"

def palindroma2(p):
    """Función que verifica si una palabra es palíndroma usando [::-1]
    (str) --> str"""
    flip = p[::-1]
    if flip == p:
        return "ES PALÍNDROMA"
    else:
        return "NO ES PALÍNDROMA"
    
def main():
    palabra = [word.strip().lower() for word in "".join(input().split())]  # Solución al problema que me puse (Ponerle para que revise varias palabras al tiempo y frases completas, como "anita lava la tina")
    #print(palindroma(palabra))
    print(palindroma2(palabra))
main()