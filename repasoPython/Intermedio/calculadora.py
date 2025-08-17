# Calculadora 1.1 (solo funciona con una operación)

def separar_nums(lista):
    operaciones = ["+", "-", "/", "*", "x"]    # Por si acaso pongo la "x"
    op = ""
    pos = 0
    for i in lista:
        if i in operaciones:
            pos += lista.index(i)
            op += i
    num1 = lista[:pos]
    num2 = lista[pos+1:]
    return [num1, op, num2]

def conv_lista(op):
    lista = []
    for i in op:
        lista.append(i)
    return lista

def calculadora(lista):
    numerito1 = "".join(lista[0])
    numerito2 = "".join(lista[2])

    if lista[1] == "+":
        return int(numerito1) + int(numerito2)
    elif lista[1] == "-":
        return int(numerito1) - int(numerito2)
    elif lista[1] == "*":
        return int(numerito1) * int(numerito2)
    elif lista[1] == "x":
        return int(numerito1) * int(numerito2)
    elif lista[1] == "/":
        return int(numerito1) / int(numerito2)

def main():
    op = input().strip()
    print(calculadora(separar_nums(conv_lista(op))))
main()

# Ponerle qué pasaría si tuviera más de un signo de operación y pues claro, más números