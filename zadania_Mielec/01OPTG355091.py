lancuch = input()

if len(lancuch) != 15 and len(lancuch) != 16:
    print("Niepoprawna długość łańcucha")
else:
    znaki = lancuch[0]
    for n in range(2,len(lancuch)+1,2):
        znaki += lancuch[n]
    haslo = znaki[0:3]
    haslo += znaki[4]
    haslo += znaki[3]
    haslo += znaki [5:]
    haslo = haslo[::-1]
    print(haslo)

