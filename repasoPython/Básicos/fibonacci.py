# Programa para imprimir una cantidad deseada de los números de fibonacci (versión con ciclo)

def fibonacci(n):
    ans = [0,1]
    if n == 0:
        return ans[0:1]
    elif n == 1:
        return ans
    else:
        for _ in range(n-1):
            suma = ans[-1] + ans[-2]
            ans.append(suma)
        return ans
        
def print_secuencia(lista):
    sec = ""
    for i in range(len(lista)):
        if i == 0:
            sec += str(lista[i])
        else:
            sec += (", " + str(lista[i]))
    return sec 

def main():
    n = int(input())
    print(print_secuencia(fibonacci(n)))
main()

# Hacerlo usando recursividad (no tengo ni idea)