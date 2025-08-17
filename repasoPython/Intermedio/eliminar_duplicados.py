# Programa que elimina los elementos duplicados de una lista

def delete_duplicate(lista):
    ans = []
    for i in lista:
        if i not in ans:
            ans.append(i)
    return ans

def main():
    lista = input("Escriba los elementos de la lista separados por comas ',': ").split(",")
    lista = [i.strip() for i in lista]
    print(delete_duplicate(lista))
main()