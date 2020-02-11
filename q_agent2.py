import random as rd
import copy
anzahl_situationen = 0
anzahl_aktionen = 0

EPSILON = 0.5
ALPHA = 0.5
GAMMA = 0.9

    
def initialisiere_agent(anzahl_situationen_, anzahl_aktionen_):
    '''
    Initialisiert den Agenten.
    Dabei wird als erster Parameter die Anzahl der möglichen Situationen
    und als zweiter Parameter die Anzahl der insgesamt möglichen Aktionen angegeben.
    '''
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global j
    global train
    global actions_in_situation
    global bias


    bias = 1
    a = [[0,0,0],[0,0,0]]
    b = [[0,0,0],[0,0,0],[0,0,0]]
    c = [[0,0,0],[0,0,0],[0,0,0]]
    d = [[0,0,0]]
    e = [a,b,c,d]
    g = [[0,0,0],[0,0,0]]
    h = [[0,0,0],[0,0,0],[0,0,0]]
    i = [[0,0,0],[0,0,0],[0,0,0]]
    j = [[0,0,0]]
    f = [g,h,i,j]
    
    train = [1,2,5,2,5,0,7,6,6,0,0,0]
    actions_in_situation = [[0,1],\
                        [0,2,3,4],\
                        [0,3,4,5],\
                        [0,2,4],\
                        [0,4,5],\
                        [],\
                        [0,7],\
                        [0,6],\
                        [0,6],\
                        [],\
                        [],\
                        []]
    

    global anzahl_situationen
    global anzahl_aktionen
        
    anzahl_situationen=anzahl_situationen_
    anzahl_aktionen=anzahl_aktionen_
       
        
def nextStep():
    i = 0
    score1 = 0
    score2 = 0
    global e
    global f
    for aktion in train:
        if aktion != 0:
            if aktion != beste_aktion(i,get_possible_actions(i)):
                score1 -= abs(beste_aktion(i,get_possible_actions(i)) - aktion)
        i += 1
    netz = mutationsAlgorithmus(score1)
    i = 0
    for aktion in train:
        if aktion != 0:
            if aktion != beste_aktion(i,get_possible_actions(i)):
                score2 -= abs(beste_aktion(i,get_possible_actions(i)) - aktion)
        i += 1
    print('1:', score1, ' | 2:',  score2)
    if score1 > score2:
        a = g
        b = h
        c = i
        d = j
        print('\n \n VeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderungVeränderung \n \n')
        print(e)
        print(f)
    elif score1 == score2:
        f = e
        
    else:
        f = e

    

        
def get_possible_actions(s):
    return actions_in_situation[s]       
# ==============================================================        
        
def beste_aktion(sit, akt):
    [a1,a2,a3] = [sit*a[0][0]+ bias*a[1][0], sit*a[0][1]+ bias*a[1][1], sit*a[0][2]+ bias*a[1][2]]
    [b1,b2,b3] = [a1*b[0][0]+ a2*b[1][0]+ a3*b[2][0],a1*b[0][1]+ a2*b[1][1]+ a3*b[2][1],a1*b[0][2]+ a2*b[1][2]+ a3*b[2][2]]
    [c1,c2,c3] = [b1*c[0][0]+ b2*c[1][0]+ b3*c[2][0],b1*c[0][1]+ b2*c[1][1]+ b3*c[2][1],b1*c[0][2]+ b2*c[1][2]+ b3*c[2][2]]
    ergebnis = int(c1*d[0][0] +  c2*d[0][1] + c3*d[0][2])
    if ergebnis in akt:
        return ergebnis
    else:
        return 0
                      
# ==============================================================
def neugierige_aktion(situation, moegliche_aktionen):
    if rd.randint(0,100) > EPSILON*100:
        besteAktion = beste_aktion(situation, moegliche_aktion)
        return besteAktion
    else:
        return rd.choose(moegliche_aktionen)
    return 0


# ==============================================================

def mutationsAlgorithmus(score):
    altesNetz = f
    zufall1 = rd.randint(0,3)
    zufall2 = rd.randint(0,len(e[zufall1])-1)
    zufall3 = rd.randint(0,len(e[zufall1][zufall2])-1)
    if score != 0:
        e[zufall1][zufall2][zufall3] += (rd.random()-0.5)*abs(score)/20
    else:
        e[zufall1][zufall2][zufall3] += rd.random()-0.5
            
    neuesNetz = e
    if altesNetz == neuesNetz:
        print('wtf')
    return [altesNetz, neuesNetz]
    
    
def lerne_dazu(situation,aktion,belohnung,naechste_situation,naechste_moegliche_aktionen):
    '''
    Ein Lernschritt wird durchgeführt.
    Eingaben sind dabei:
    + die Situation, für die gelernt werden soll.
    + die Aktion, die neu bewertet werden soll.
    + die Belohnung, die beim Durchführen dieser Aktion erfolgt war.
    + die Situation, in der sich der Agent nach der Aktion befindet
    + eine Liste von Aktionen, die in der neuen Situation möglich sind.
    '''

    #q[situation][aktion] = (1 - ALPHA)*q[situation][aktion] +  ALPHA*(belohnung +  GAMMA*q[naechste_situation][beste_aktion(naechste_situation, naechste_moegliche_aktionen)])
    #print(q)
    
    
# ==============================================================


def dokumentiere_agent():
    '''
    Schreibt alle relevanten Parameter des "Gehirns" auf den Bildschirm.
    '''
    pass
