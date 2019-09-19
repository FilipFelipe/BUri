# -*- coding: utf-8 -*-

dia = int(input())
respdia = 0
respdias = 0
if dia >= 365:
    respdia = dia/365
    dia = dia - (365 * int(respdia))
    print("%d ano(s)" % respdia)
    if dia >= 30:
        respdias = dia / 30
        dia = dia - (30 * int(respdias))
        print("%d mes(es)" % respdias)
        if dia < 30 and dia > 0:
            print("%d dia(s)" % dia)
            dia = dia - dia
    else:
        print("%d mes(es)" % respdias)
        print("%d dia(s)" % dia)
elif dia >=30 and dia < 365:
    respdias = dia / 30
    dia = dia - (30 * int(respdias))
    print("%d ano(s)" % respdia)
    print("%d mes(es)" % respdias)
    if dia < 30 and dia > 0:
        print("%d dia(s)" % dia)
        dia = dia - dia
    else:
        print("%d dia(s)" % dia)
elif dia < 30 and dia >= 0:
    print("%d ano(s)" % respdia)
    print("%d mes(es)" % respdias)
    print("%d dia(s)" % dia)
