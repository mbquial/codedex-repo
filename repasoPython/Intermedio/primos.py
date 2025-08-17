# Programa que determina si un número es primo

def primo(num):
    num = int(num)
    if num == 2:
        return "Primo"
    elif num % 2 == 0 or num == 1:
        return "No es primo"
    elif num <= 0:
        return "Número ingresado no válido"
    else:
        contador = 3
        while contador ** 2 <= num:
            if num % contador == 0:
                return "No es primo"
            contador = contador + 2
        else:
            return "Primo"  
        
def main():
    num = int(input().strip())
    print(primo(num))
main()