


def colors():
    couleurs = ["blue", "green", "black", "yellow", "magenta","red"]
    a = rd.choice(couleurs)
    return a

def deplacement(event):

    couleurs = colors()
    pas = 10
    global x,y,fautes
    if event.char == "d":
        circuit.move(player,pas,0)
        x += pas
    elif event.char == "q":
        circuit.move(player,-pas,0)
        x -= pas
    elif event.char == "s":
        circuit.move(player,0,pas)
        y += pas
    elif event.char == "z":
        circuit.move(player,0,-pas)
        y -= pas


    if fautes == 3:
        circuit.create_rectangle((0,0),(500,500),fill= "white", outline= "white")
        circuit.create_text( 250 , 250 , text = "game\nover " , fill= "red", font= "40")
        circuit.quit()
        
    if (0-14) <= x <= (420+14) and (50-14) <= y <= (57+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (150-14) <= x <= (500+14) and (100-14) <= y <= (107+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (75-14) <= x <= (82+14) and (100-14) <= y <= (200+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (75-14) <= x <= (275+14) and (150-14) <= y <= (157+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (200-14) <= x <= (207+14) and (107-14) <= y <= (150+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (0-14) <= x <= (200+14) and (250-14) <= y <= (257+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (275-14) <= x <= (500+14) and (200-14) <= y <= (207+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (200-14) <= x <= (207+14) and (200-14) <= y <= (250+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (350-14) <= x <= (357+14) and (207-14) <= y <= (307+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (75-14) <= x <= (350+14) and (300-14) <= y <= (307+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (75-14) <= x <= (82+14) and (300-14) <= y <= (375+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (125-14) <= x <= (175+14) and (375-14) <= y <= (382+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (175-14) <= x <= (182+14) and (350-14) <= y <= (500+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (175-14) <= x <= (225+14) and (350-14) <= y <= (357+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (225-14) <= x <= (232+14) and (350-14) <= y <= (400+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (275-14) <= x <= (282+14) and (300-14) <= y <= (350+14):
        circuit.config(bg=couleurs)  
        fautes += 1
    if (275-14) <= x <= (350+14) and (350-14) <= y <= (357+14):
        circuit.config(bg=couleurs) 
        fautes += 1
    if (225-14) <= x <= (300+14) and (400-14) <= y <= (407+14):
        circuit.config(bg=couleurs)   
        fautes += 1
    if (300-14) <= x <= (307+14) and (400-14) <= y <= (450+14):
        circuit.config(bg=couleurs)   
        fautes += 1
    if (300-14) <= x <= (350+14) and (450-14) <= y <= (457+14):
        circuit.config(bg=couleurs)   
        fautes += 1
    if (350-14) <= x <= (357+14) and (450-14) <= y <= (500+14):
        circuit.config(bg=couleurs)  
        fautes += 1
    if (350-14) <= x <= (357+14) and (350-14) <= y <= (400+14):
        circuit.config(bg=couleurs)   
        fautes += 1
    if (350-14) <= x <= (400+14) and (400-14) <= y <= (407+14):
        circuit.config(bg=couleurs)   
        fautes += 1
    if (400-14) <= x <= (407+14) and (400-14) <= y <= (450+14):
        circuit.config(bg=couleurs)
        fautes += 1
    if (400-14) <= x <= (500+14) and (450-14) <= y <= (457+14):
        circuit.config(bg=couleurs)   
        fautes += 1

    

fautes = 0  
w= 500
h= 500
x = 15
y =15

import random as rd
import tkinter as tk
racine = tk.Tk()
racine.title("pacman")
circuit = tk.Canvas(racine,width= w,height=h,bg= "yellow")
circuit.grid(column=0,row=0)
circuit.create_rectangle((-1,50),(420,57),fill= "white", outline= "white")
circuit.create_rectangle((501,100),(150,107),fill= "white", outline= "white") 
circuit.create_rectangle((75,100),(82,200),fill= "white", outline= "white") 
circuit.create_rectangle((75,150),(275,157),fill= "white", outline= "white") 
circuit.create_rectangle((200,150),(207,107),fill= "white", outline= "white")# a faire apparaitre en discontinue
circuit.create_rectangle((0,250),(200,257),fill= "white", outline= "white")  
circuit.create_rectangle((275,200),(500,207),fill= "white", outline= "white")  
circuit.create_rectangle((200,257),(207,200),fill= "white", outline= "white")
circuit.create_rectangle((350,207),(357,307),fill= "white", outline= "white")  
circuit.create_rectangle((75,300),(350,307),fill= "white", outline= "white")
circuit.create_rectangle((75,300),(82,375),fill= "white", outline= "white")
circuit.create_rectangle((125,375),(175,382),fill= "white", outline= "white")
circuit.create_rectangle((175,350),(182,500),fill= "white", outline= "white")
circuit.create_rectangle((175,350),(225,357),fill= "white", outline= "white")
circuit.create_rectangle((225,350),(232,400),fill= "white", outline= "white")
circuit.create_rectangle((275,300),(282,350),fill= "white", outline= "white")
circuit.create_rectangle((275,350),(350,357),fill= "white", outline= "white")
circuit.create_rectangle((225,400),(300,407),fill= "white", outline= "white")
circuit.create_rectangle((300,400),(307,450),fill= "white", outline= "white")
circuit.create_rectangle((300,450),(350,457),fill= "white", outline= "white")
circuit.create_rectangle((350,450),(357,500),fill= "white", outline= "white")
circuit.create_rectangle((350,350),(357,400),fill= "white", outline= "white")
circuit.create_rectangle((350,400),(400,407),fill= "white", outline= "white")
circuit.create_rectangle((400,400),(407,450),fill= "white", outline= "white")
circuit.create_rectangle((400,450),(500,457),fill= "white", outline= "white")

player =circuit.create_oval((0,0),(30,30),fill= "green",outline="white")
racine.bind("<KeyPress>",deplacement)
racine.mainloop()