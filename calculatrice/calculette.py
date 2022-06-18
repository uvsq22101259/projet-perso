import tkinter as tk


def numero(chiffre:int):
    calcul.insert(tk.END,chiffre)

def operation(operation):
    calcul.insert(tk.END,operation)

def egal ():
    equation = eval(calcul.get())
    calcul.delete(0,tk.END)
    calcul.insert(0,equation)

racine = tk.Tk()
racine.title("calculatrice")
calcul = tk.Entry(racine, width = 30)
calcul.grid(column=0 , row=0, columnspan=3)

# chifffres #
zero = tk.Button(racine,text="0",command= lambda : numero(0) )
zero.grid(column=0 , row=4)
un = tk.Button(racine,text="1",command= lambda : numero(1) )
un.grid(column=0 , row=3)
deux = tk.Button(racine,text="2",command= lambda : numero(2) )
deux.grid(column=1 , row=3)
trois = tk.Button(racine,text="3",command= lambda : numero(3) )
trois.grid(column=2 , row=3)
quattre = tk.Button(racine,text="4",command= lambda : numero(4) )
quattre.grid(column=0 , row=2)
cinque = tk.Button(racine,text="5",command= lambda : numero(5) )
cinque.grid(column=1 , row=2)
six = tk.Button(racine,text="6",command= lambda : numero(6) )
six.grid(column=2 , row=2)
sept = tk.Button(racine,text="7",command= lambda : numero(7) )
sept.grid(column=0 , row=1)
huit = tk.Button(racine,text="8",command= lambda : numero(8) )
huit.grid(column=1 , row=1)
neuf = tk.Button(racine,text="9",command= lambda : numero(9) )
neuf.grid(column=2 , row=1)

# operateurs #
racine_carre = tk.Button(racine,text="√",command= lambda : operation("**0.5") )
racine_carre.grid(column=1 , row=4)
puissance = tk.Button(racine,text="^",command= lambda : operation("**") )
puissance.grid(column=2 , row=4)
plus = tk.Button(racine,text="+",command= lambda : operation("+") )
plus.grid(column=3 , row=1)
moins = tk.Button(racine,text="-",command= lambda : operation("-") )
moins.grid(column=3 , row=2)
div = tk.Button(racine,text="⁒",command= lambda : operation("/") )
div.grid(column=3 , row=3)
mult = tk.Button(racine,text="x",command= lambda : operation("*") )
mult.grid(column=3 , row=4)

resultat = tk.Button(racine,text="=",command= egal )
resultat.grid(column=3 , row=0)





racine.mainloop()