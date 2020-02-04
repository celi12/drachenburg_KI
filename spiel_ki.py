from tkinter import *
from umwelt import *
from q_agent import *
import time

the_reward = 0
halt = FALSE

DELAY_LERNEN = 50
DELAY_AUSFUEHREN = 50


def gui_perform(anr):
    # print("Führe Aktion ",anr,": ",get_name_of_action(anr)," aus und bestimme den Reward")
    the_reward=perform_action(anr)
    global score
    score=score+the_reward
    cs=get_current_situation()
    # print("Belohnung: ",the_reward," Neue Situation: ",cs)
    # verstecke_alle_buttons()
    zeige_neue_grafik(cs)
    # zeige_moegliche_buttons(cs)
    label_score.config(text="Score: "+str(score))
   

def erzeuge_buttons():
    global btn
    btn= []
    for i in range(len(an)):
        btn.append(Button(root, text=an[i], command=lambda c=i: gui_perform(c)))
    
def zeige_alle_buttons():
    for bt in btn:
        bt.pack()

def verstecke_alle_buttons():
    for bt in btn:
        bt.pack_forget()
    
        
def zeige_moegliche_buttons(s):
    list = get_possible_actions(s)
    for i in list:
        btn[i].pack()

def zeige_neue_grafik(s):
    global label_mit_bild
    label_mit_bild.config(image=bilder[s])
    

# =========================================================================


        

        
        
def nextOptStep():
    global score
    print("NextStep")
    cs=get_current_situation()
    zeige_neue_grafik(cs)
    if cs not in get_end_situations():
        

        print("beste_aktion(",cs,get_possible_actions(cs),')')
        act = beste_aktion(cs,get_possible_actions(cs))
        
                
        
        label_mit_com.config(text=get_name_of_action(act))
        rew=perform_action(act)
        score=score+rew
        csn = get_current_situation()
        zeige_neue_grafik(csn)
        print((cs,act,rew,csn,get_possible_actions(csn),0.5,0.9))
        cs=csn
        label_score.config(text=str(score))
        label_mit_com.after(DELAY_AUSFUEHREN,nextOptStep)
    else:
        set_init_situation(0)
        score=0
        print("NEUE RUNDE")
        
# =========================================================================
        
def start_Learning():
    global halt
    halt=False
    while halt == False:
        nextStep()
    
def start_Playing():
    nextOptStep()

def stopping():
    global halt
    halt=True   

# =========================================================================

root = Tk()
root.title("DIE DRACHENBURG")

bilder=[]

score=0
set_init_situation(0)

for i in range(12):
    # print("Lade Bild ",i)
    bilder.append(PhotoImage(file='Bild_'+str(i)+'.gif'))
 
  
label_score=Label(root,text="Score: "+str(score),font=("Helvetica", 16))
label_score.pack()
  
label_mit_bild = Label(root, image=bilder[0])
label_mit_bild.pack()

label_mit_com = Label(root, text="ACTION",font=("Helvetica", 16))
label_mit_com.pack()

bt_Lernen = Button(root, text="Lernen", command=lambda :start_Learning())
bt_Lernen.pack()

bt_Optimal = Button(root, text="Optimal Spielen", command=lambda :start_Playing())
bt_Optimal.pack()

bt_Stop = Button(root, text="Stop", command=lambda : stopping())
bt_Stop.pack()

# Aufruf
print('initialisiere_agent(12,8)')
initialisiere_agent(12,8)

cs = get_current_situation()
an=get_action_names()
# print(an)

root.mainloop()
