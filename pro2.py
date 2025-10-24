from pickle import INT


print("*** Arvude mäng ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta täisarv => "))))
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrame, mitu paaris- ja mitu paaritut numbrit arvus on.")
    print()
    # Count even and odd digits
    temp = a
    paaris = 0
    paaritu = 0
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        temp //= 10

    print("Paaris:", paaris)
    print("Paaritu:", paaritu)
    print()

    # Reverse the number
    print("*Pöörame* sisestatud arvu ümber")
    print()
    temp = a
    b = 0
    while temp > 0:
        number = temp % 10
        temp //= 10
        b = b * 10 + number
    print("*Pööratud* arv", b)
    print()

    # Syracuse (Collatz) sequence
    print("Kontrollime Syracuse’i hüpoteesi")
    print()
    c = a
    if c % 2 == 0:
        print("c - Paaris arv. Jagame 2-ga.")
    else:
        print("c - Paaritu arv. Korrutame 3-ga ja liidame 1.")
    # Print the sequence (include starting value)
    seq = [c]
    while c != 1:
        if c % 2 == 0:
            c = c // 2
        else:
            c = 3 * c + 1
        seq.append(c)
    # Print sequence on one line
    print(" -> ".join(str(x) for x in seq))
    print()
    print("Teoreem tõestatud")