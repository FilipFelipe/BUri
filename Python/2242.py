frase = input()
op=[]
opp=[]
for x in frase:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        op.append(x)
        opp.append(x)

opp.reverse()
if op == opp:
    print("S")

else:
    print("N")
