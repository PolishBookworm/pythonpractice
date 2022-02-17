def modulo(a,b):
    iteracje = 0
    while b > 0:
        iteracje += 1
        c = b
        b = a % c
        a = c
    return [iteracje, a]

def subtract(a,b):
    iteracje = 0
  
    while a-b > 0:
        c = b
        b = a - c
        a = c
        print(a, b, c)
        iteracje += 1
    return [iteracje,b]
    
a = int(input("a = "))
b = int(input("b = "))

NWD = modulo(a,b)[1]
iteracje1 = modulo(a,b)[0]
iteracje2 = subtract(a,b)

print("NWD = ", NWD)
print("L_iteracji (I metoda) = ", iteracje1)
print("L_iteracji (II metoda) = ", iteracje2)
