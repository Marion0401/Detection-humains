from tkinter import *
from PIL import Image, ImageTk
import  tkinter as Tk 
import tkinter.ttk as ttk
import socket

#connexion  à la rasberry 1
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind(('', 15555))
socket1.listen(5)
client1, address1 = socket1.accept()
print ("{} connected 1")

#connexion  à la rasberry 2
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.bind(('', 15556))
socket2.listen(5)
client2, address2 = socket2.accept()
print ("{} connected 2")

#reception d'une valeur pour initialiser
listerasb1=[]
while len(listerasb1)<1:
    dispoA411 = int(client1.recv(255).decode())
    listerasb1.append(dispoA411)
    print('dispo A411', dispoA411)

listerasb2=[]
while len(listerasb2)<1:
    dispoA412 = int(client2.recv(255).decode())
    listerasb2.append(dispoA412)
    print('dispo A412',dispoA412)

def clicksalledetp(event=None):          #def la fenêtre qui s'ouvre après avoir cliqué sur une salle de tp = toujours indisponible
    global fenexiste, fen                   #fen désigne la fenêtre donnant les information de la salle désignée
    if fenexiste==1:                        #si on a déjà cliqué sur un bouton on supprime la fenêtre qui était affichée
        fen.destroy()
    fen = Tk.Tk()                           #et on en crée la nouvelle
    affiche = Tk.Label(fen, width=120, text="Salle de TP / Statut = Indisponible", fg="black")
    affiche.pack(side=Tk.LEFT)              #avec un message sur le statut de la salle
    fenexiste=1                             #une fenêtre est donc créée
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)         #si on appuie sur la croix rouge de la petite fenêtre d'information cela renvoie vers la fonction croixrougefen
    fen.mainloop()
def clickA410(event=None):               #idem pour la salle A410
    global fenexiste, fen
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    affiche = Tk.Label(fen, width=120, text="Local A410 / Statut = Indisponible", fg="black")
    affiche.pack(side=Tk.LEFT)
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickA411(event=None):               #def la fenetre qui s'ouvre après avoir cliqué sur la salle A411 : 
    global fenexiste, fen, dispoA411
    if fenexiste==1:                        #si on a déjà cliqué sur un bouton on supprime la fenêtre qui était affichée
        fen.destroy()
    fen = Tk.Tk()                           #et on en crée la nouvelle
    if dispoA411 == 0:                      #si 0 personne détectée -> salle dispo
         affiche = Tk.Label(fen, width=120, text="A411 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:                                   #si 1 ou + de personnes détectées -> salle indispo
        affiche = Tk.Label(fen, width=120, text="A411 / Aucun cours programmé  / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoA411, fg="black")
    affiche.pack(side=Tk.LEFT)              #on intègre le message sur le statut de la salle
    fenexiste=1                             #une fenêtre est donc créée
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)    #si on appuie sur la croix rouge de la petite fenêtre d'information cela renvoie vers la fonction croixrougefen
    fen.mainloop()
def clickA412(event=None):              #idem pour A412
    global fenexiste, fen, dispoA412
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoA412 == 0:
         affiche = Tk.Label(fen, width=120, text="A412 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="A412 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoA412, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickC401(event=None):              #idem pour C401
    global fenexiste, fen, dispoC401
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoC401 == 0:
         affiche = Tk.Label(fen, width=120, text="C401 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="C401 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoC401, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickC402(event=None):              #idem pour C402
    global fenexiste, fen, dispoC402
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoC402 == 0:
         affiche = Tk.Label(fen, width=120, text="C402 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="C402 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoC402, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickC403(event=None):              #idem pour C403
    global fenexiste, fen, dispoC403
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoC403 == 0:
         affiche = Tk.Label(fen, width=120, text="C403 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="C403 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoC403, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickC404(event=None):              #idem pour C404
    global fenexiste, fen, dispoC404
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoC404 == 0:
         affiche = Tk.Label(fen, width=120, text="C404 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="C404 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoC404, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickC405(event=None):              #idem pour C405
    global fenexiste, fen, dispoC405
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoC405 == 0:
         affiche = Tk.Label(fen, width=120, text="C405 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="C405 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoC405, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickC406(event=None):              #idem pour C406
    global fenexiste, fen, dispoC406
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoC406 == 0:
         affiche = Tk.Label(fen, width=120, text="C406 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="C406 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoC406, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickB505(event=None):              #idem pour B505
    global fenexiste, fen, dispoB505
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoB505 == 0:
         affiche = Tk.Label(fen, width=120, text="B505 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="B505 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoB505, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickB506(event=None):             #idem pour B506
    global fenexiste, fen, dispoB506
    if fenexiste==1:
        fen.destroy()
    fen = Tk.Tk()
    if dispoB506 == 0:
         affiche = Tk.Label(fen, width=120, text="B506 / Aucun cours programmé / Nombre de personnes présentes dans la salle = 0 / statut = Disponible", fg="black")
    else:
        affiche = Tk.Label(fen, width=120, text="B506 / Aucun cours programmé / statut = Occupée \nNombre de personnes présentes dans la salle = %d " %dispoB506, fg="black")
    affiche.pack(side=Tk.LEFT) 
    fenexiste=1
    fen.protocol("WM_DELETE_WINDOW", croixrougefen)
    fen.mainloop()
def clickretour(event=None):            #après avoir cliqué sur le bouton retour, il renvoit à la fenêtre d'accueil
    global fenexiste
    deuxiemefenetre.destroy()                  #en supprimant la carte
    if fenexiste==1:                #et les fenêtres sur le statut de des salles
        fen.destroy()
        fenexiste=0
    return
def clickquitter(event=None):           #après avoir cliqué sur le bouton quitter ou sur la corix rouge de la fenêtre 
    global boucleOK, premierefenetreexiste, deuxiemefenetreexiste, fenexiste        #on ne veut plus continuer la boucle principal -> le programme s'arrête
    boucleOK = 0                                    #changement de la variable qui va arrêter le programme
    if premierefenetreexiste == 1:                  #si on appuie sur la croix de la première fenêtre
        premierefenetre.destroy()                   #on la supprime
    if deuxiemefenetreexiste == 1:                  #si on appuie sur la croix de la deuxième fenêtre
        deuxiemefenetre.destroy()                   #on la supprime
    if fenexiste==1:                                #si on appuie sur la croix de la fenêtre d'informations des salles
        fen.destroy()                               #on la supprime
    return
def clickactualiser(event=None):        #après avoir cliqué sur le bouton actualiser, on renlance la fonction de l'étage choisit au préalable
    global etagechoisi, fenexiste, dispoA411, dispoA412
    deuxiemefenetre.destroy()                  #en supprimant la carte d'une part

    dispoA411 = int(client1.recv(255).decode())
    print ('actualisation A411',dispoA411)

    dispoA412 = int(client2.recv(255).decode())
    print ('actualisation A412',dispoA412)

    if fenexiste==1:
        fen.destroy()                          #et les fenêtres d'informations des salles
        fenexiste=0
    if etagechoisi == 0:
        etage400choisi()
    elif etagechoisi == 1:
        etage600choisi()
    return
def boutonsenhautagauche():             #affiche la trois boutons quitter, actualiser et retour
    retour = Image.open("retour.jpg")
    photoretour = ImageTk.PhotoImage(retour)
    bretour = Tk.Button(deuxiemefenetre, image=photoretour, command=clickretour)       #bretour = boutonretour idem pour les autres mots précédés d'un b
    bretour.pack()
    bretour.place(x=0, y=50)

    quitter = Image.open("quitter.jpg")
    photoquitter = ImageTk.PhotoImage(quitter)
    bquitter = Tk.Button(deuxiemefenetre, image=photoquitter, command=clickquitter)
    bquitter.pack()
    bquitter.place(x=0, y=0)

    actualiser = Image.open("actualiser.jpg")
    photoactualiser = ImageTk.PhotoImage(actualiser)
    bactualiser = Tk.Button(deuxiemefenetre, image=photoactualiser, command=clickactualiser)
    bactualiser.pack()
    bactualiser.place(x=0 , y=25)

    deuxiemefenetre.after(15000, clickactualiser)                                      #intègre une fonction qui revoit à la fonction actualiser au bout d'une minute
    deuxiemefenetre.mainloop()
def croixrougefen():                   #cette fonction devait être rajoutée pour dire que la fenêtre n'existe plus si on appuie sur la croix rouge en haut à droite
    global fenexiste, fen
    if fenexiste == 1:        
        fen.destroy()
        fenexiste = 0
def etage400choisi():               #si l'utilisateur a choisi l'étage 400-500 on affiche le logo avec tous les boutons placés
    global premierefenetreexiste, deuxiemefenetreexiste, fenexiste, fen, deuxiemefenetre, dispoA411, dispoA412, dispoB505, dispoB506, dispoC401, dispoC402, dispoC403, dispoC404, dispoC405, dispoC406
    deuxiemefenetre = Tk.Tk() 
    deuxiemefenetre.title("Etage 400-500")
    deuxiemefenetre.geometry("900x575+175+50")            # on dimentionne et place la deuxième fenêtre sur l'écran

    fenexiste = 0
    premierefenetreexiste = 0
    deuxiemefenetreexiste = 1

    imagelogoisen = Image.open("logo isen.jpg")
    photologoisen = ImageTk.PhotoImage(imagelogoisen)
    logoisen = Label(deuxiemefenetre, image = photologoisen)
    logoisen.place(x=0 , y=0)    

    salletp1 = Image.open("images indispo/salletp1.jpg")
    photosalletp1 = ImageTk.PhotoImage(salletp1)
    bsalletp1 = Tk.Button(deuxiemefenetre, image=photosalletp1, command=clicksalledetp)
    bsalletp1.pack()
    bsalletp1.place(x=95, y=20)

    salletp2 = Image.open("images indispo/salletp2.jpg")
    photosalletp2 = ImageTk.PhotoImage(salletp2)
    bsalletp2 = Tk.Button(deuxiemefenetre, image=photosalletp2, command=clicksalledetp)
    bsalletp2.pack()
    bsalletp2.place(x=95, y=107)

    A410 = Image.open("images indispo/A410.jpg")
    photoA410 = ImageTk.PhotoImage(A410)
    bA410 = Tk.Button(deuxiemefenetre, image=photoA410, command=clickA410)
    bA410.pack()
    bA410.place(x=93, y=250)

    B501 = Image.open("images indispo/B501.jpg")
    photoB501 = ImageTk.PhotoImage(B501)
    bB501 = Tk.Button(deuxiemefenetre, image=photoB501, command=clicksalledetp)
    bB501.pack()
    bB501.place(x=234, y=402)

    B502 = Image.open("images indispo/B502.jpg")
    photoB502 = ImageTk.PhotoImage(B502)
    bB502 = Tk.Button(deuxiemefenetre, image=photoB502, command=clicksalledetp)
    bB502.pack()
    bB502.place(x=319, y=402)

    B503 = Image.open("images indispo/B503.jpg")
    photoB503 = ImageTk.PhotoImage(B503)
    bB503 = Tk.Button(deuxiemefenetre, image=photoB503, command=clicksalledetp)
    bB503.pack()
    bB503.place(x=403, y=402)    

    if dispoA411 == 0:
        A411 = Image.open("images vertes/A411.jpg")
    else :
        A411 = Image.open("images rouges/A411.jpg")
    photoA411 = ImageTk.PhotoImage(A411)
    bA411 = Tk.Button(deuxiemefenetre, image=photoA411, command=clickA411)
    bA411.pack()
    bA411.place(x=93, y=320)

    if dispoA412 == 0:
        A412 = Image.open("images vertes/A412.jpg")
    else :
        A412 = Image.open("images rouges/A412.jpg")
    photoA412 = ImageTk.PhotoImage(A412)
    bA412 = Tk.Button(deuxiemefenetre, image=photoA412, command=clickA412)
    bA412.pack()
    bA412.place(x=93, y=440)

    dispoC401 = 0
    if dispoC401 == 0:
        C401 = Image.open("images vertes/C401.jpg")
    else :
        C401 = Image.open("images rouges/C401.jpg")
    photoC401 = ImageTk.PhotoImage(C401)
    bC401 = Tk.Button(deuxiemefenetre, image=photoC401, command=clickC401)
    bC401.pack()
    bC401.place(x=199, y=20)

    dispoC402 = 0
    if dispoC402 == 0:
        C402 = Image.open("images vertes/C402.jpg")
    else :
        C402 = Image.open("images rouges/C402.jpg")
    photoC402 = ImageTk.PhotoImage(C402)
    bC402 = Tk.Button(deuxiemefenetre, image=photoC402, command=clickC402)
    bC402.pack()
    bC402.place(x=327, y=20)

    dispoC403 = 0
    if dispoC403 == 0:
        C403 = Image.open("images vertes/C403.jpg")
    else :
        C403 = Image.open("images rouges/C403.jpg")
    photoC403 = ImageTk.PhotoImage(C403)
    bC403 = Tk.Button(deuxiemefenetre, image=photoC403, command=clickC403)
    bC403.pack()
    bC403.place(x=442, y=20)

    dispoC404 = 0
    if dispoC404 == 0:
        C404 = Image.open("images vertes/C404.jpg")
    else :
        C404 = Image.open("images rouges/C404.jpg")
    photoC404 = ImageTk.PhotoImage(C404)
    bC404 = Tk.Button(deuxiemefenetre, image=photoC404, command=clickC404)
    bC404.pack()
    bC404.place(x=512, y=20)

    dispoC405 = 0
    if dispoC405 == 0:
        C405 = Image.open("images vertes/C405.jpg")
    else :
        C405 = Image.open("images rouges/C405.jpg")
    photoC405 = ImageTk.PhotoImage(C405)
    bC405 = Tk.Button(deuxiemefenetre, image=photoC405, command=clickC405)
    bC405.pack()
    bC405.place(x=582, y=20)

    dispoC406 = 0
    if dispoC406 == 0:
        C406 = Image.open("images vertes/C406.jpg")
    else :
        C406 = Image.open("images rouges/C406.jpg")
    photoC406 = ImageTk.PhotoImage(C406)
    bC406 = Tk.Button(deuxiemefenetre, image=photoC406, command=clickC406)
    bC406.pack()
    bC406.place(x=712, y=20)

    dispoB505 = 0
    if dispoB505 == 0:
        B505 = Image.open("images vertes/B505.jpg")
    else :
        B505 = Image.open("images rouges/B505.jpg")
    photoB505 = ImageTk.PhotoImage(B505)
    bB505 = Tk.Button(deuxiemefenetre, image=photoB505, command=clickB505)
    bB505.pack()
    bB505.place(x=483, y=402)

    dispoB506 = 0
    if dispoB506 == 0:
        B506 = Image.open("images vertes/B506.jpg")
    else :
        B506 = Image.open("images rouges/B506.jpg")
    photoB506 = ImageTk.PhotoImage(B506)
    bB506 = Tk.Button(deuxiemefenetre, image=photoB506, command=clickB506)
    bB506.pack()
    bB506.place(x=553, y=402)

    deuxiemefenetre.protocol("WM_DELETE_WINDOW", clickquitter)
    boutonsenhautagauche()

    deuxiemefenetre.mainloop()
def etage600choisi():       #si l'utilisateur a choisi l'étage 600-700 on affiche les 3 boutons et une image de papillon pour l'exemple
    global fenexiste, deuxiemefenetre, premierefenetreexiste, deuxiemefenetreexiste
    fenexiste=0
    premierefenetreexiste = 0
    deuxiemefenetreexiste = 1
    deuxiemefenetre = Tk.Tk() 
    deuxiemefenetre.title("Etage 600-700")
    deuxiemefenetre.geometry("900x575+175+50")
    imageetage600 = Image.open("papillon.jpg")
    photoetage600 = ImageTk.PhotoImage(imageetage600)
    carteetage600 = Label(deuxiemefenetre, image = photoetage600)
    carteetage600.place(x=0, y=0)

    deuxiemefenetre.protocol("WM_DELETE_WINDOW", clickquitter)
    boutonsenhautagauche()

    deuxiemefenetre.mainloop()
def choixdesetages():
    global premierefenetre, fenexiste, deuxiemefenetre,etagechoisi
    if choix.current() == 0 :       #si l'utilisateur a choisi l'étage 400-500 son ferme la fenêtre principale et on renvoit à la fonction etage400choisi
        etagechoisi=0
        premierefenetre.destroy()
        fenexiste = 0        
        etage400choisi()
        deuxiemefenetre.mainloop()
    elif choix.current() == 1 :     #si l'utilisateur a choisi l'étage 600-700 son ferme la fenêtre principale et on renvoit à la fonction etage600choisi
        etagechoisi=1
        premierefenetre.destroy()
        fenexiste = 0
        etage600choisi()
        deuxiemefenetre.mainloop()
boucleOK = 1
while boucleOK == 1 :           #affichage de la fenêtre d'accueil avec la liste des choix des étages
    premierefenetre = Tk.Tk()
    fenexiste = 0
    premierefenetreexiste = 1
    deuxiemefenetreexiste = 0
    premierefenetre.geometry("500x200+375+200")         # on dimentionne et place la première fenêtre sur l'écran
    premierefenetre.title("Choisissez l'étage : ")    
    premierefenetre.config(bg='burlywood1')
    choix = ttk.Combobox(premierefenetre, values=["étages 400-500", "étages 600-700"])
    choix.pack ()
    boutonOK = Tk.Button (premierefenetre, text="OK")
    boutonOK.config (command = choixdesetages)
    boutonOK.pack ()
    premierefenetre.protocol("WM_DELETE_WINDOW", clickquitter)
    premierefenetre.mainloop()