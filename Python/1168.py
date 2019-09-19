op = int(input())
numero = []
for i in range(op):
    numero.append(input())
for nu in range(op):
    led = 0
    numero1 = numero[nu]
    for ut in range(len(numero[nu])):
        if numero1[ut] == "0":
            led += 6
        if numero1[ut] == "1":
            led += 2
        if numero1[ut] == "2":
            led += 5
        if numero1[ut] == "3":
            led += 5
        if numero1[ut] == "4":
            led += 4
        if numero1[ut] == "5":
            led += 5
        if numero1[ut] == "6":
            led += 6
        if numero1[ut] == "7":
            led += 3
        if numero1[ut] == "8":
            led += 7
        if numero1[ut] == "9":
            led += 6
    print("%d leds" % led)
