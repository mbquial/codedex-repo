# Programa que comprueba si un número es par o impar

# Solución al problema inicial
def par_impar(num):
    """Función que retorna si un número es PAR o IMPAR según corresponda
    (int) --> str"""
    if num % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"
    
def main():
    numeritos = list(map(int, input("Ingrese el o los números que desea verificar separados por espacios: ").split()))
    for i in numeritos: # Solución al problema que me puse (Ponerle para que sean varios números los que se revisen al tiempo)
        print(f"El número {i} es {par_impar(i)}")
    # print(par_impar(num)) *** Solución al problema inicial
main()
