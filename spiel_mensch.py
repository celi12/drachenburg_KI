from tkinter import *
from umwelt import *

the_reward = 0

def gui_perform(anr):
    print("Führe Aktion ",anr,": ",get_name_of_action(anr)," aus und bestimme den Reward")
    the_reward=perform_action(anr)
    global score
    score=score+the_reward
    cs=get_current_situation()
    print("Belohnung: ",the_reward," Neue Situation: ",cs)
    verstecke_alle_buttons()
    zeige_neue_grafik(cs)
    zeige_moegliche_buttons(cs)
    label_score.config(text="Situation Nr. "+str(cs)+ "   Score: "+str(score)+" (Letzte Belohnung: "+str(the_reward)+")")
   

def erzeuge_buttons():
    global btn
    btn= []
    for i in range(len(an)):
        btn.append(Button(root, text=str(i)+"  "+an[i], command=lambda c=i: gui_perform(c)))
    
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


root = Tk()
root.title("DIE DRACHENBURG")

bilder=[]

score=0


for i in range(12):
    print("Lade Bild ",i)
    bilder.append(PhotoImage(file='Bild_'+str(i)+'.gif'))
    
bilder.append(PhotoImage(file='Bild_0.gif'))
  
  
label_score=Label(root,text="Situation Nr. 0   "+  "Score: "+str(score))
label_score.pack()
  
label_mit_bild = Label(root, image=bilder[0])
label_mit_bild.pack()


cs = get_current_situation()
an=get_action_names()
print(an)

erzeuge_buttons()
zeige_moegliche_buttons(0)


root.mainloop()