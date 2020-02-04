# Spielumgebung Drachenburg

global current_situation

actions = ["Weglaufen", \
           "Burg betreten",\
           "Buch nehmen",\
           "Schwert nehmen", \
           "Drachen angreifen",\
           "Dem Drachen vorlesen",\
           "Safe öffnen und Geld holen",\
           "Mühsam mit dem Buch Kombination enträtseln"]

situations = ["Vor der Burg",\
              "Drache und kein Werkzeug",\
              "Drache (Held mit Buch)",\
              "Drache (Held mit Schwert)",\
              "Drache (Held mit Buch und Schwert)",\
              "Drache tot (Held ohne Buch)",\
              "Drache tot (Held mit Buch)",\
              "Drache verrät dankbar die Kombination",\
              "Kombination aus Buch enträtselt",\
              "Safe offen",\
              "Held hat versagt",\
              "Held wurde gefressen"]

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
init_situation = 0
score = 200

end_situations = [5,9,10,11]

next_situation = [[10, 1, 0, 0, 0, 0, 0, 0],\
                  [10, 0, 2, 3,11, 0, 0, 0],\
                  [10, 0, 0, 4,11, 7, 0, 0],\
                  [10, 0, 4, 0, 5, 0, 0, 0],\
                  [10, 0, 0, 0, 6, 7, 0, 0],\
                  [ 0, 0, 0, 0, 0, 0, 0, 0],\
                  [10, 0, 0, 0, 0, 0, 0, 8],\
                  [10, 0, 0, 0, 0, 0, 9, 0],\
                  [10, 0, 0, 0, 0, 0, 9, 0],\
                  [ 0, 0, 0, 0, 0, 0, 0, 0],\
                  [ 0, 0, 0, 0, 0, 0, 0, 0],\
                  [ 0, 0, 0, 0, 0, 0, 0, 0]]


reward =         [[ -40, 0,   0,   0,    0,    0,   0,    0],\
                  [ -40, 0, -90, -90,-1000,    0,   0,    0],\
                  [ -40, 0,   0, -90,-1000,    0,   0,    0],\
                  [ -40, 0, -90,   0, -100,    0,   0,    0],\
                  [ -40, 0,   0,   0,    0,    0,   0,    0],\
                  [   0, 0,   0,   0,    0,    0,   0,    0],\
                  [ -40, 0,   0,   0,    0,    0,   0, -200],\
                  [ -40, 0,   0,   0,    0,    0,1000,    0],\
                  [ -40, 0,   0,   0,    0,    0,1000,    0],\
                  [   0, 0,   0,   0,    0,    0,   0,    0],\
                  [   0, 0,   0,   0,    0,    0,   0,    0],\
                  [   0, 0,   0,   0,    0,    0,   0,    0]]



current_situation=init_situation



def set_init_situation(s):
    global current_situation
    current_situation=s
    
def get_current_situation():
    return current_situation
    
def get_possible_actions(s):
    return actions_in_situation[s]

def get_name_of_situation(s):
    return situations[s]

def get_name_of_action(a):
    return actions[a]

def get_situation_names():
    return siutations

def get_action_names():
    return actions

def get_end_situations():
    return end_situations

def perform_action(a):
    global current_situation
    rew = reward[current_situation][a]
    current_situation = next_situation[current_situation][a]
    return rew
    

    

if __name__ == '__main__' :
    while (not (get_current_situation() in get_end_situations())):
        print("Situation ",get_current_situation(),": ", get_name_of_situation(get_current_situation()), "    Score: ",score)
        list = get_possible_actions(get_current_situation())
        for a_nr in list:
            print("  ",a_nr,"  ",get_name_of_action(a_nr))
        act = eval(input("Wähle: "))
        rw = perform_action(act)
        print(rw," ",get_current_situation())
        score=score+rw
    print(get_name_of_situation(get_current_situation()))
    print("Die Episode ist zu Ende")
    print("Du hast ",score," Punkte erreicht.")




    
              