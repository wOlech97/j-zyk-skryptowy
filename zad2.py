import sys
import random
def deck():
    ranga=['2','3','4','5','6','7','8','9','10','J','D','K','A']
    kolor=['c','d','h','s']
    talia=[]
    for r in ranga:
        for k in kolor:
            talia.append((r,k))
    return talia
print(deck())
print("")
print("")
print("--------------")
print("")
def tasuj(talia):
    for x in range(0,100): #losowe karty zostaną zamienione miejscami 100 razy
        losowa_A = random.randint(0,52)- 1#losuje liczbę od 1 do 52, dlatego odejmuję 1 żeby losowało do 0 do 51
        while True: #wykonuje się do momentu aż losowa B będzie inna do losowej A  
            losowa_B=random.randint(0,52) -1
            if(losowa_B != losowa_A):
                break
        tmp = talia[losowa_A]
        talia[losowa_A]=talia[losowa_B]
        talia[losowa_B]= tmp #zamiana miejscami losowych kart
    return talia    
print(tasuj(deck()))
print("")
print("")
print("--------------")
print("")
def deal(deck,n):
    talie_graczy = [] #lista w której znajdzie się n list/talii 
    for x in range (0,n):  #dodaję n pustych list
        talie_graczy.append([])
    length = len(deck)
    for a in range(-1,n-1):#dwie pętle dla każdego gracza(a) losowanych jest 5 kart (b)
        for b in range(-1, n-1):
             losowa=random.randint(0,length) - 1 # losowanie pozydji karty nie może się powtarzać dlatego każda wylsoowana karta poniżej jest usuwana, więc zmniejsza się długośc listy 
             talie_graczy[a].append(deck[losowa])
             
             deck.pop(losowa)
             length-=1
    return talie_graczy
print(deal(tasuj(deck()),5))
                

        

    
   


