A = int(input())
B = int(input())
C = int(input())

if A == B or A == C or B == C or A == B+C or B == A+C or C == A+B:
    print("S")
else:
    print("N")

