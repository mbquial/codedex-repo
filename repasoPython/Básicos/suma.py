# Programa para sumar dos números dados

# Solución al problema inicial
def suma(nums):
    """Función que suma dos números dados
    (list) --> int"""
    return nums[0] + nums[1]

# Solución al problema que me puse (sumar más de dos números)
def suma_final(nums):
    """Función que suma varios números dados
    (list) --> int"""
    ans = 0
    for i in nums:
        ans += i
    return ans

def main():
    nums = input("Ingrese los números que quiera sumar: ").split()
    int_nums = list(map(int, nums))
    # print(suma(int_nums)) ***Solución al problema inicial
    print(suma_final(int_nums))
main()
