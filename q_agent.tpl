import random as rd
anzahl_situationen = 0
anzahl_aktionen = 0

EPSILON = 0.2
ALPHA = 0.5
GAMMA = 0.9

    
def initialisiere_agent(anzahl_situationen_, anzahl_aktionen_):
    '''
    Initialisiert den Agenten.
    Dabei wird als erster Parameter die Anzahl der möglichen Situationen
    und als zweiter Parameter die Anzahl der insgesamt möglichen Aktionen angegeben.
    '''
    global anzahl_situationen
    global anzahl_aktionen
        
    anzahl_situationen=anzahl_situationen_
    anzahl_aktionen=anzahl_aktionen_
       
        
 
        
# ==============================================================        
        
def beste_aktion(situation, moegliche_aktionen):
    '''
    Sucht zu einer bestimmten Situation die (nach seinem Wissen) beste Aktion aus.
    Der Parameter moegliche_aktionen ist dabei eine Liste von Aktions-Nummern, die in der Situation 
    überhaupt möglich sind.
    '''
    return 0
    
                      
# ==============================================================

def neugierige_aktion(situation, moegliche_aktionen):
    '''
    Sucht zu einer bestimmten Situation meistens die (nach seinem Wissen) beste Aktion aus.
    Der Parameter moegliche_aktionen ist dabei eine Liste von Aktions-Nummern, die in der Situation 
    überhaupt möglich sind.
    Mit einer gewissen Wahrscheinlich jedoch wählt die Funktion auch eine andere, zufällige Aktion aus,
    allerdings nur eine der möglichen Aktionen.
    '''
    return 0


# ==============================================================


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
    pass
    
    
# ==============================================================

def dokumentiere_agent():
    '''
    Schreibt alle relevanten Parameter des "Gehirns" auf den Bildschirm.
    '''
    pass