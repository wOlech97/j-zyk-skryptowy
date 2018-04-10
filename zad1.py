import sys 

def ile_razy(tekst):
    wynik={}
    uzyteLitery=[]
    licznik=0
    for x in tekst:
        if x in uzyteLitery or x == ' ':
            continue
        uzyteLitery.append(x)
        for a in tekst:
            if(x==a):
                licznik+=1
        wynik[x]=licznik
        licznik=0
    return wynik

tekst_input = input("Wprowadz tekst : ")
print(ile_razy(tekst_input))
    
