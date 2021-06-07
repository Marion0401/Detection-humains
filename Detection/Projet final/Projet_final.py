from tkinter import *
from PIL import Image, ImageTk
import  tkinter as Tk 
import tkinter.ttk as ttk
import socket


#connexion  à la rasberry 1
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

socket.listen(5)
client, address = socket.accept()
print ("{} connected")

liste=[]
while len(liste)<3:
    dispoA411 = int(client.recv(255).decode())
    liste.append(dispoA411)
    print(dispoA411)


  

def clicksalledetp(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="Salle de TP / Statut = Indisponible", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickA410(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="Local A410 / Statut = Indisponible", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickA411(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="A411 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 4 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickA412(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="A412 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 2 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickC401(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C401 / Cours programmé / Nombre de personnes présentes dans la salle = 22 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickC402(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C402 / Cours programmé / Nombre de personnes présentes dans la salle = 25 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickC403(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C403 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 31 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickC404(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C404 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 26 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickC405(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C405 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 18 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickC406(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C406 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickB505(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="B505 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickB506(event=None):
    global click
    global fen
    if click==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="C406 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 3 / statut = Occupée", fg="black")
    affiche.pack(side=Tk.LEFT) 
    click=1
    fen.mainloop()
def clickretour(event=None):
    global click
    root.destroy()
    if click==1:
        fen.destroy()
        click=0
    return
def clickquitter(event=None):
    global w
    w=0
    root.destroy()
    if click==1:
        fen.destroy()
    return
def clickactualiser(event=None):
    global z, click, dispoA411
    root.destroy()

    dispoA411 = int(client.recv(255).decode())
    print(dispoA411)

    if dispoA411 != "":
        print (dispoA411)

    if click==1:
        fen.destroy()
        click=0
    if z == 0:
        etage400choisi()
    elif z == 1:
        etage600choisi()
    return
def boutonsenhautagauche():
    retour = Image.open("retour.jpg")
    photoretour = ImageTk.PhotoImage(retour)
    bretour = Tk.Button(root, image=photoretour, command=clickretour)
    bretour.pack()
    bretour.place(x=0, y=50)

    quitter = Image.open("quitter.jpg")
    photoquitter = ImageTk.PhotoImage(quitter)
    bquitter = Tk.Button(root, image=photoquitter, command=clickquitter)
    bquitter.pack()
    bquitter.place(x=0, y=0)

    actualiser = Image.open("actualiser.jpg")
    photoactualiser = ImageTk.PhotoImage(actualiser)
    bactualiser = Tk.Button(root, image=photoactualiser, command=clickactualiser)
    bactualiser.pack()
    bactualiser.place(x=0 , y=25)
    root.mainloop()
def etage400choisi():
    global click, root, dispoA411
    root = Tk.Tk() 
    root.title("Etage 400-500")
    root.geometry("900x1000")
    image = Image.open("imageetage2.jpg")
    photo = ImageTk.PhotoImage(image)

    label_img = Label(root, image = photo)
    label_img.place(x=0 , y=0)

    salletp1 = Image.open("images indispo/salletp1.jpg")
    photosalletp1 = ImageTk.PhotoImage(salletp1)
    bsalletp1 = Tk.Button(root, image=photosalletp1, command=clicksalledetp)
    bsalletp1.pack()
    bsalletp1.place(x=95, y=58)

    salletp2 = Image.open("images indispo/salletp2.jpg")
    photosalletp2 = ImageTk.PhotoImage(salletp2)
    bsalletp2 = Tk.Button(root, image=photosalletp2, command=clicksalledetp)
    bsalletp2.pack()
    bsalletp2.place(x=95, y=145)

    A410 = Image.open("images indispo/A410.jpg")
    photoA410 = ImageTk.PhotoImage(A410)
    bA410 = Tk.Button(root, image=photoA410, command=clickA410)
    bA410.pack()
    bA410.place(x=93, y=318)

    B501 = Image.open("images indispo/B501.jpg")
    photoB501 = ImageTk.PhotoImage(B501)
    bB501 = Tk.Button(root, image=photoB501, command=clicksalledetp)
    bB501.pack()
    bB501.place(x=234, y=530)

    B502 = Image.open("images indispo/B502.jpg")
    photoB502 = ImageTk.PhotoImage(B502)
    bB502 = Tk.Button(root, image=photoB502, command=clicksalledetp)
    bB502.pack()
    bB502.place(x=319, y=530)

    B503 = Image.open("images indispo/B503.jpg")
    photoB503 = ImageTk.PhotoImage(B503)
    bB503 = Tk.Button(root, image=photoB503, command=clicksalledetp)
    bB503.pack()
    bB503.place(x=403, y=530)    

  
    if dispoA411 > 0:
        A411 = Image.open("images vertes/A411.jpg")
    else :
        A411 = Image.open("images rouges/A411.jpg")
    photoA411 = ImageTk.PhotoImage(A411)
    bA411 = Tk.Button(root, image=photoA411, command=clickA411)
    bA411.pack()
    bA411.place(x=93, y=393)

    dispoA412 = 0
    if dispoA412 == 1:
        A412 = Image.open("images vertes/A412.jpg")
    else :
        A412 = Image.open("images rouges/A412.jpg")
    photoA412 = ImageTk.PhotoImage(A412)
    bA412 = Tk.Button(root, image=photoA412, command=clickA412)
    bA412.pack()
    bA412.place(x=93, y=550)

    dispoC401 = 0
    if dispoC401 == 1:
        C401 = Image.open("images vertes/C401.jpg")
    else :
        C401 = Image.open("images rouges/C401.jpg")
    photoC401 = ImageTk.PhotoImage(C401)
    bC401 = Tk.Button(root, image=photoC401, command=clickC401)
    bC401.pack()
    bC401.place(x=199, y=60)

    dispoC402 = 0
    if dispoC402 == 1:
        C402 = Image.open("images vertes/C402.jpg")
    else :
        C402 = Image.open("images rouges/C402.jpg")
    photoC402 = ImageTk.PhotoImage(C402)
    bC402 = Tk.Button(root, image=photoC402, command=clickC402)
    bC402.pack()
    bC402.place(x=327, y=60)

    dispoC403 = 0
    if dispoC403 == 1:
        C403 = Image.open("images vertes/C403.jpg")
    else :
        C403 = Image.open("images rouges/C403.jpg")
    photoC403 = ImageTk.PhotoImage(C403)
    bC403 = Tk.Button(root, image=photoC403, command=clickC403)
    bC403.pack()
    bC403.place(x=442, y=60)

    dispoC404 = 0
    if dispoC404 == 1:
        C404 = Image.open("images vertes/C404.jpg")
    else :
        C404 = Image.open("images rouges/C404.jpg")
    photoC404 = ImageTk.PhotoImage(C404)
    bC404 = Tk.Button(root, image=photoC404, command=clickC404)
    bC404.pack()
    bC404.place(x=512, y=60)

    dispoC405 = 0
    if dispoC405 == 1:
        C405 = Image.open("images vertes/C405.jpg")
    else :
        C405 = Image.open("images rouges/C405.jpg")
    photoC405 = ImageTk.PhotoImage(C405)
    bC405 = Tk.Button(root, image=photoC405, command=clickC405)
    bC405.pack()
    bC405.place(x=582, y=60)

    dispoC406 = 1
    if dispoC406 == 1:
        C406 = Image.open("images vertes/C406.jpg")
    else :
        C406 = Image.open("images rouges/C406.jpg")
    photoC406 = ImageTk.PhotoImage(C406)
    bC406 = Tk.Button(root, image=photoC406, command=clickC406)
    bC406.pack()
    bC406.place(x=712, y=60)

    dispoB505 = 1
    if dispoB505 == 1:
        B505 = Image.open("images vertes/B505.jpg")
    else :
        B505 = Image.open("images rouges/B505.jpg")
    photoB505 = ImageTk.PhotoImage(B505)
    bB505 = Tk.Button(root, image=photoB505, command=clickB505)
    bB505.pack()
    bB505.place(x=483, y=530)

    dispoB506 = 0
    if dispoB506 == 1:
        B506 = Image.open("images vertes/B506.jpg")
    else :
        B506 = Image.open("images rouges/B506.jpg")
    photoB506 = ImageTk.PhotoImage(B506)
    bB506 = Tk.Button(root, image=photoB506, command=clickB506)
    bB506.pack()
    bB506.place(x=553, y=530)

    boutonsenhautagauche()

    root.mainloop()
def etage600choisi():
    global click, root
    click=0
    root = Tk.Tk() 
    root.title("Etage 600-700")
    root.geometry("900x1000")
    image = Image.open("papillon.jpg")
    photo = ImageTk.PhotoImage(image)
    label_img = Label(root, image = photo)
    label_img.place(x=0, y=0)
    boutonsenhautagauche()
    root.mainloop()
def choixdesetages():
    global root1, click, root,z
    if o.current() == 0 :
        z=0
        root1.destroy()
        click = 0        
        etage400choisi()
        root.mainloop()
    elif o.current() == 1 :
        z=1
        root1.destroy()
        click = 0
        etage600choisi()
        root.mainloop()


w = 1
while w == 1 : 

    root1 = Tk.Tk()
    root1.geometry("500x200")
    root1.title("Choisissez l'étage : ")
    o = ttk.Combobox(root1, values=["étages 400-500", "étages 600-700"])
    o.pack ()
    b = Tk.Button (root1, text="OK")
    b.config (command = choixdesetages)
    b.pack ()
    root1.mainloop()
