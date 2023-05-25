from StatsAllPokemons import AllPokemon, PokedexMQ, PokedexOB, NomPokemon
from StatsAllPokeBalls import AllBall, NomBall
import random
from random import randint
import time
from tkinter import *
from tkinter.ttk import *
import pygame
import tkinter as tk
import pickle
from Sauvegarde import po, su, hy, ma, objet, PokedexOB, PokedexMQ

#Si des erreurs surviennent après une capture, réinitialiser vos statistiques sur le menu principal > à propos du jeu.


def stopMusicGoCapture(): #Fonction pour arrêter la musique et lancer celle de la capture
    pygame.mixer.init() #Initialisation de pygame.mixer
    pygame.mixer.music.stop() #Arrêt de la musique
    pygame.mixer.music.load("Pokemon\Son\PokemonCapture.mp3") #Chargement de la musique
    pygame.mixer.music.play(-1) #Lancement de la musique
    pygame.mixer.music.set_volume(0.6) #Volume de la musique
    
def stopMusicGoMenu(): #Fonction pour arrêter la musique et lancer celle du menu
    pygame.mixer.init()
    pygame.mixer.music.stop() 
    pygame.mixer.music.load("Pokemon\Son\PokemonMenu.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)

def stopMusicGoFarm(): #Fonction pour arrêter la musique et lancer celle de la récolte
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Pokemon\Son\PokemonFarm.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)
    
def stopMusicGoSuccess():
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Pokemon\Son\PokeballSuccessSound.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)
    
def stopMusic(): #Fonction pour arrêter la musique
    pygame.mixer.music.stop()
 


pygame.init() #Initialisation de pygame

#Lancement du jeu
running=True 


# 0 signifie Pokeball, 1 Superball, 2 Hyperball, 3 Masterball, servira pour la récolte de pokeballs. 
aleatoirepoke=[0, 1, 2, 3]


click=0

#initialisation des reussites et echecs
YesorNo=["y", "n"]
YesorNoINT=[1, 0]




while running==True:
    
    stopMusicGoMenu() #Lancement de la musique du menu

    print("Bonjour ! Que voulez-vous faire ?")
    #Ouverture Première fenêtre
    PremiereAct=Tk()
    
    #Choix 1 : Capturer des Pokemons
    def Capturer(): 
        PremiereAct.destroy()  #Quitte la fenêtre
        global ChoixActionUne
        ChoixActionUne='capture'
        return ChoixActionUne
    
    #Choix 2 : Récolter des PokeBalls
    def Farmm():
        PremiereAct.destroy()
        global ChoixActionUne
        ChoixActionUne='farm'
        return ChoixActionUne
    
    #Choix 3 : Voir son Pokedex
    def VoirPDex():
        PremiereAct.destroy()
        global ChoixActionUne
        ChoixActionUne='pokedex'
        return ChoixActionUne
    
    #Choix 4 : Voir ses PokeBalls
    def VoirPB():
        PremiereAct.destroy()
        global ChoixActionUne
        ChoixActionUne='ball'
        return ChoixActionUne
    
    #Choix 5 : A propos du jeu
    def APropos():
        PremiereAct.destroy()
        global ChoixActionUne
        ChoixActionUne='apropos'
        return ChoixActionUne
    
    #Choix 6 : Quitter le jeu
    def Quit():
        PremiereAct.destroy()
        global ChoixActionUne
        ChoixActionUne='stop'
        return ChoixActionUne

    label=tk.Label(PremiereAct, text="Bonjour ! Que voulez-vous faire ?", font=("Arial", 18), bg="#191722", fg="white")
    label.pack(pady=10)
    #Initialisation des boutons  ("command=Fonction" permet de lancer la fonction quand on clique sur le bouton)
    CaptureClick=tk.Button(PremiereAct, text=('Capturer des Pokemons !'), compound=TOP, command=Capturer, font=("Arial", 15), bg="#3E1530", fg="white")
    CaptureClick.pack(pady=1)  #Pour afficher le bouton
    FarmClick=tk.Button(PremiereAct, text=('Récuperer des PokeBalls !'), compound=TOP, command=Farmm, font=("Arial", 15), bg="#3E1530", fg="white")
    FarmClick.pack(pady=1)
    VoirPDClickex=tk.Button(PremiereAct, text=('Voir mon Pokedex !'), compound=TOP, command=VoirPDex, font=("Arial", 15), bg="#3E1530", fg="white")
    VoirPDClickex.pack(pady=1)
    VoirPBClick=tk.Button(PremiereAct, text=('Voir mes PokeBalls !'), compound=TOP, command=VoirPB, font=("Arial", 15), bg="#3E1530", fg="white")
    VoirPBClick.pack(pady=1)
    AProposClick=tk.Button(PremiereAct, text=('À propos du jeu'), compound=TOP, command=APropos, font=("Arial", 15), bg="#3E1530", fg="white")
    AProposClick.pack(pady=1)
    QuitClick=tk.Button(PremiereAct, text=('Quitter le jeu'), command=Quit, font=("Arial", 15), bg="#3E1530", fg="white")
    QuitClick.pack()
    
    PremiereAct.wm_attributes("-topmost", True) #Pour que la fenetre soit toujours au dessus des autres
    PremiereAct.title("Que Voulez-vous faire ?") #titre de la fenetre
    PremiereAct.resizable(True, True) #pour que la fenêtre soit redimensionnable
    PremiereAct.geometry('500x320') #taille de la fenêtre
    PremiereAct.config(bg="#1E1722") #couleur de fond de la fenêtre
    mainloop() #pour que la fenetre reste ouverte
    
    if ChoixActionUne=="stop": 
        stopMusic()
        for i in range(1, 4): #"animation" dans le terminal
            print("Fermeture du jeu" + "." * i, end="\r")
            time.sleep(1)
        running=FALSE
        
        
    elif ChoixActionUne=="ball":
        print("Vous avez", po, "PokeBalls,", su, "SuperBalls,", hy, "HyperBalls,", ma, "MasterBalls et", objet, "Oeufs chances !")
        time.sleep(1)
        
        
    elif ChoixActionUne=="apropos":
        master=Tk()
    
        def ResetStat():
            master.destroy()
            global po, su, hy, ma, PokedexOB, PokedexMQ, objet
            print("Vos statistiques ont été réinitialisées !")
            time.sleep(1)
            po, su, hy, ma, objet=0, 0, 0, 0, 0
            PokedexMQ=[0, "Bulbizarre", "Herbizarre", "Florizarre", "Salamèche", "Reptincel", "Dracaufeu", "Carapuce", "Carabaffe", "Tortank", "Chenipan", "Chrysacier", "Papilusion", "Aspicot", "Coconfort", "Dardargnan", "Roucool", "Roucoups", "Roucarnage", "Rattata", "Rattatac", "Piafabec", "Rapasdepic", "Abo", "Arbok", "Pikachu", "Raichu", "Sabelette", "Sablaireau", "NidoranF", "Nidorina", "Nidoqueen", "NidoranM", "Nidorino", "Nidoking", "Mélofée", "Mélodelfe", "Goupix", "Feunard", "Rondoudou", "Grodoudou", "Nosferapti", "Nosferalto", "Mystherbe", "Ortide", "Rafflésia", "Paras", "Parasect", "Mimitoss", "Aéromite", "Taupiqueur", "Triopikeur", "Miaouss", "Persian", "Psykokwak", "Akwakwak", "Férosinge", "Colossinge", "Caninos", "Arcanin", "Ptitard", "Têtarte", "Tartard", "Abra", "Kadabra", "Alakazam", "Machoc", "Machopeur", "Mackogneur", "Chétiflor", "Boustiflor", "Empiflor", "Tentacool", "Tentacruel", "Racaillou", "Gravalanch", "Grolem", "Ponyta", "Galopa", "Ramoloss", "Flagadoss", "Magnéti", "Magnéton", "Canarticho", "Doduo", "Dodrio", "Otaria", "Lamantine", "Tadmorv", "Grotadmorv", "Kokiyas", "Crustabri", "Fantominus", "Spectrum", "Ectoplasma", "Onix", "Soporifik", "Hypnomade", "Krabby", "Krabboss", "Voltorbe", "Électrode", "Noeunoeuf", "Noadkoko", "Osselait", "Ossatueur", "Kicklee", "Tygnon", "Excelangue", "Smogo", "Smogogo", "Rhinocorne", "Rhinoféros", "Leveinard", "Saquedeneu", "Kangourex", "Hypotrempe", "Hypocéan", "Poissirène", "Poissoroy", "Stari", "Staross", "MrMime", "Insécateur", "Lippoutou", "Élektek", "Magmar", "Scarabrute", "Tauros", "Magicarpe", "Léviator", "Lokhlass", "Métamorph", "Évoli", "Aquali", "Voltali", "Pyroli", "Porygon", "Amonita", "Amonistar", "Kabuto", "Kabutops", "Ptéra", "Ronflex", "Artikodin", "Électhor", "Sulfura", "Minidraco", "Draco", "Dracolosse", "Mewtwo", "Mew"]
            PokedexOB=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151]

        def RetourMenu():
           master.destroy() 
        
        def Quit2():
            master.destroy()
            global running
            stopMusic()
            for i in range(1, 4): 
                print("Fermeture du jeu" + "." * i, end="\r")
                time.sleep(1)
            running=False
            return running
        
        master.config(bg="#1E1722")
        master.title("A propos du jeu !")
        master.geometry('400x250')
        master.resizable(True, True)
        master.wm_attributes("-topmost", True)
        
        label=tk.Label(master, text="Projet pensé et créé par \n SANNA Thomas et ADANI François.", font=("Arial", 15), bg="#191722", fg="white")
        label.pack(pady=15)
        reset=tk.Button(master,  text=('Reinitialiser les stastistiques'), compound=TOP, command=ResetStat, font=("Arial", 15), bg="#3E1530", fg="white")
        reset.pack(pady=2)
        MenuBouton=tk.Button(master, text=('Retourner au menu'), command=RetourMenu, font=("Arial", 15), bg="#3E1530", fg="white")
        MenuBouton.pack(pady=2)
        Quit2Click=tk.Button(master, text=('Quitter le jeu'), command=Quit2, font=("Arial", 15), bg="#3E1530", fg="white")
        Quit2Click.pack()
        mainloop()
        
        
        
    elif ChoixActionUne=="farm":
        
        stopMusicGoFarm() 
        
        master=Tk()

        
        def buttonCommand():
            global po, su, hy, ma, click, label, objet
            click += 1
            modu = click % 5
            if modu == 0:
                boll = random.choices(aleatoirepoke, weights=(0.70, 0.25, 0.045, 0.005)) #choix aléatoire de la pokeball
                obj =random.choices(YesorNoINT, weights=(0.20 , 0.80))
                objint= int(obj[0])
                bollint = int(boll[0])
                print('Bravo ! Vous avez gagné', AllBall[bollint][1])
                if bollint == 0:
                    po += 1
                elif bollint == 1:
                    su += 1
                elif bollint == 2:
                    hy += 1
                elif bollint == 3:
                    ma += 1
                if objint == 1:
                    objet +=1
                    print('Bravo ! Vous avez gagné un Oeuf Chance !')
            if click==5:
                VisuClic.config(text=str(5))
            else:
                VisuClic.config(text=str((-1) * (click-5)))
            if modu == 0:
                click = 0
        
        photo = PhotoImage(file=r"pokeballFARM.png")
        mainClickButton = tk.Button(master, text="Obtiens une Ball tous les 5 Clicks !", image=photo, compound=TOP, command=buttonCommand, bg="white", fg="#3E1530")
        mainClickButton.pack()
        
        VisuClic = tk.Label(master, text="", font=("Arial", 35), bg="white", fg="#3E1530")
        VisuClic.pack(pady=10)
        VisuClic.place(x=15, y=10) # placer le label en haut à gauche
        
        master.config(bg="#1E1722")
        master.wm_attributes("-topmost", True)
        master.title("PokeBall Farm !")
        master.resizable(True, True)
        master.geometry('300x280')
        
        mainloop()
        
        print('Vous avez désormais', po, 'PokeBall,', su, 'SuperBall,', hy, 'HyperBall et', ma, 'MasterBall', objet, "Oeufs chances")
        time.sleep(1)

        
    elif ChoixActionUne=="pokedex":
        PokelistO=[]
        PokelistM=[]
        for elementO in PokedexOB:
            if (type(elementO)==str):
                PokelistO.append(elementO)
        print("Vous avez attrapé : ", len(PokelistO), "Pokemons")
        time.sleep(1)
        print(", ".join(PokelistO))
        time.sleep(1)

        for elementM in PokedexMQ:
            if (type(elementM)==str):
                PokelistM.append(elementM)
        print("Il vous manque : ", len(PokelistM), "Pokemons")
        time.sleep(1)
        print(", ".join(PokelistM))
        time.sleep(1)
        
        
        
    elif ChoixActionUne=="capture":
        
        capture=True
        
        while capture==True:
            
            stopMusicGoCapture()
            
            n=random.randint(1, 151) #nombre aléatoire entre 1 et 151
            rencontre=NomPokemon[n] #nom du Pokemon rencontré
            Sprite=AllPokemon[n][2] #sprite (l'image du pokemon pour pygame) du Pokemon rencontré

            pygame.display.set_caption("Pokemon") #titre de la fenêtre pygame
            screen=pygame.display.set_mode((300, 300)) #taille de la fenêtre pygame


            ApparitionPokemon=pygame.image.load(AllPokemon[n][2]) #chargement de l'image
            ApparitionPokemon=pygame.transform.scale (ApparitionPokemon, (300, 300)) #redimensionnement de l'image

            runningim=True #lancement de la boucle pygame

            screen.blit(ApparitionPokemon, (0, 0)) #affichage de l'image
            pygame.display.flip() #rafraichissement de l'image
            
            
            print("Un",rencontre,"sauvage apparaît")
            print("Voulez-vous capturer le pokemon ?")
            
            ChoixCap=Tk()
            
            def repcap(): #Choix 1 : Capturer le Pokemon
                ChoixCap.destroy()
                global choixcapture
                choixcapture='y'
                return choixcapture
            def repfui(): #Choix 2 : Prendre la fuite
                ChoixCap.destroy()
                global choixcapture
                choixcapture='n'
                return choixcapture
            
            repcapclick=tk.Button(ChoixCap, text=('Capturer le Pokemon !'), command=repcap, font=("Arial", 15), bg="#3E1530", fg="white") #Initialisation des boutons
            repcapclick.pack(pady=2)
            repfuiclick=tk.Button(ChoixCap, text=('Prendre la Fuite !'), command=repfui, font=("Arial", 15), bg="#3E1530", fg="white")
            repfuiclick.pack()
            
            ChoixCap.config(bg="#1E1722")
            ChoixCap.wm_attributes("-topmost", True)
            ChoixCap.title("Que Voulez-vous faire ?")
            ChoixCap.resizable(True, True)
            ChoixCap.geometry('300x100')
            mainloop()
            
            
            if choixcapture=="n":
                pygame.quit() #la fenetre pygame se ferme
                print("Vous prenez la fuite ")
                time.sleep(1)
                capture=False
                
            elif choixcapture=="y":
                captureYes=True
                chance = False
                
                while captureYes==True:
                    if (po <=0 and su <=0 and hy <=0 and ma <=0):
                        print("Vous n'avez pas assez de Pokeballs, essayez d'en obtenir pour capturer un pokemon.")
                        time.sleep(1)
                        captureYes=False
                        capture=False
                        pygame.quit() #la fenetre pygame se ferme
                        
                    else:
                        print("Quelle Pokeball voulez-vous utiliser ?")
                        
                        ChoixBall=Tk()
                        def PokeChoix():
                            ChoixBall.destroy()
                            global choixballs
                            choixballs=0
                            return choixballs
                        def SuperChoix():
                            ChoixBall.destroy()
                            global choixballs
                            choixballs=1
                            return choixballs
                        def HyperChoix():
                            ChoixBall.destroy()
                            global choixballs
                            choixballs=2
                            return choixballs
                        def MasterChoix():
                            ChoixBall.destroy()
                            global choixballs
                            choixballs=3
                            return choixballs
                        def ObjetChoix():
                            ChoixBall.destroy()
                            global choixballs
                            choixballs=4
                            return choixballs
                        def Fuite():
                            ChoixBall.destroy()
                            global choixballs
                            choixballs=5
                            return choixballs

                        pokephoto=PhotoImage(file=r"pokeball.png") #Chemin des images
                        superphoto=PhotoImage(file=r"superball.png")
                        hyperphoto=PhotoImage(file=r"hyperball.png")
                        masterphoto=PhotoImage(file=r"masterball.png")
                        objetphoto = PhotoImage(file=r"Oeuf_Chance.png")

                        PokeClick=tk.Button(ChoixBall, image=pokephoto, text=('PokeBall'), compound=TOP, command=PokeChoix, font=("Arial", 15), bg="#3E1530", fg="white")
                        PokeClick.pack(pady=2)
                        SuperClick=tk.Button(ChoixBall, image=superphoto, text=('SuperBall'), compound=TOP, command=SuperChoix, font=("Arial", 15), bg="#3E1530", fg="white")
                        SuperClick.pack(pady=2)
                        HyperClick=tk.Button(ChoixBall, image=hyperphoto, text=('HyperBall'), compound=TOP, command=HyperChoix, font=("Arial", 15), bg="#3E1530", fg="white")
                        HyperClick.pack(pady=2)
                        MasterClick=tk.Button(ChoixBall, image=masterphoto, text=('MasterBall'), compound=TOP, command=MasterChoix, font=("Arial", 15), bg="#3E1530", fg="white")
                        MasterClick.pack(pady=2)
                        ObjetClick=tk.Button(ChoixBall, image=objetphoto, text=('Oeuf Chance'), compound=TOP, command=ObjetChoix, font=("Arial", 15), bg="#3E1530", fg="white")
                        ObjetClick.pack(pady=2)
                        FuiteClick=tk.Button(ChoixBall, text=('Prendre la fuite !'), command=Fuite, font=("Arial", 15), bg="#3E1530", fg="white")
                        FuiteClick.pack()
                        
                        ChoixBall.config(bg="#1E1722")
                        ChoixBall.wm_attributes("-topmost", True)
                        ChoixBall.title("Quelle Ball ?")
                        ChoixBall.resizable(True, True)
                        ChoixBall.geometry('200x400')
                        mainloop()
                        if ((choixballs==0 and po<=0)or (choixballs==1 and su<=0)or(choixballs==2 and hy<=0)or(choixballs==3 and ma<=0)):
                            print("Vous n'avez pas assez de",NomBall[choixballs])
                            time.sleep(1)
                            
                        elif choixballs==5:
                            print("Vous prenez la fuite")
                            time.sleep(1)
                            captureYes=False
                            capture=False
                            pygame.quit() #la fenetre pygame se ferme

                        elif (objet == 0) and (choixballs == 4):
                            print("Vous n'avez pas assez d'Oeufs Chances")
                            time.sleep(1)

                        elif choixballs==4:
                            if chance == False:
                                print("Vous utilisez un Oeuf Chance !")
                                time.sleep(1)
                                chance = True
                                objet -= 1
                            else:
                                print("Vous avez déjà utilisé un Oeuf Chance !")
                                time.sleep(1)
                            
                        else:
                            print("Vous avez lancé votre", NomBall[choixballs])
                            time.sleep(1)
                            
                            if choixballs==0:
                                po-=1
                            if choixballs==1:
                                su-=1
                            if choixballs==2:
                                hy-=1
                            if choixballs==3:
                                ma-=1
                                
                                
                       
                            probball=float(AllBall[choixballs][0][0])
                            probpoke=float(AllPokemon[n][1])
                            if chance == False:
                                probALLlist=random.choices(YesorNo, weights=(probball * probpoke * 1.4 , 1.0))
                            else:
                                probALLlist=random.choices(YesorNo, weights=(probball * probpoke * 1.4 * 1.2 , 1.0))
                            probALL=str(probALLlist[0])
                            
                            if probALL=="n":
                                but=randint(2, 3)
                                for i in range (but):
                                    print ('Bup' + '.' * i, end="\r")
                                    time.sleep(1)
                                print ('Cling !')
                                time.sleep(1)
                                print ("Oh non !,", rencontre, "est sorti de sa Pokeball !")
                                time.sleep(1)
                                print('Voulez vous essayer de le capturer à nouveau ?')
                                
                                yon2=Tk()
                                def repy2():
                                    yon2.destroy()
                                    global retr2
                                    retr2='y'
                                    return retr2
                                def repn2():
                                    yon2.destroy()
                                    global retr2
                                    retr2='n'
                                    return retr2
                                repy2click=tk.Button(yon2, text=('Lancer une autre Ball !'), command=repy2, font=("Arial", 15), bg="#3E1530", fg="white")
                                repy2click.pack(pady=2)
                                repn2click=tk.Button(yon2, text=('Prendre la fuite !'), command=repn2, font=("Arial", 15), bg="#3E1530", fg="white")
                                repn2click.pack()
                                
                                yon2.config(bg="#1E1722")
                                yon2.wm_attributes("-topmost", True)
                                yon2.title("Chasser de nouveau ?")
                                yon2.resizable(True, True)
                                yon2.geometry('300x100')
                                mainloop()
                                
                                if retr2=='n':
                                    print("Vous prenez la fuite !")
                                    time.sleep(1)
                                    captureYes=False
                                    capture=False
                                    pygame.quit() #la fenetre pygame se ferme
                                
                            else :
                                for bup in range (4) :
                                    print ('Bup' + '.' * bup, end="\r")
                                    time.sleep (1)
                                print ('Tching !!')
                                stopMusicGoSuccess()
                                time.sleep (1)
                                print('Félicitation !, Vous avez capturé un', rencontre, '!')
                                time.sleep(1)
                                
                                if rencontre not in PokedexOB:
                                    print("Bravo !", rencontre, "a été ajouté à votre Pokédex !")
                                    time.sleep(1)
                                    PokedexOB[n], PokedexMQ[n]=PokedexMQ[n], PokedexOB[n]
                                    
                                else:
                                    print(rencontre, "est déjà dans le pokedex !")
                                    time.sleep(1)
                                    
                                captureYes=False
                                pygame.quit() #la fenetre pygame se ferme
                                print("Voulez-vous lancer une nouvelle capture ?")
                                yon1=Tk()
                                def repy1():
                                    yon1.destroy()
                                    global retry
                                    retry='y'
                                    return retry
                                def repn1():
                                    yon1.destroy()
                                    global retry
                                    retry='n'
                                    return retry
                                repy1click=tk.Button(yon1, text=('Chasser de nouveaux Pokemons !'), command=repy1, font=("Arial", 15), bg="#3E1530", fg="white")
                                repy1click.pack(pady=2)
                                repn1click=tk.Button(yon1, text=('Arrêter la chasse !'), command=repn1, font=("Arial", 15), bg="#3E1530", fg="white")
                                repn1click.pack()
                                
                                yon1.config(bg="#1E1722")
                                yon1.wm_attributes("-topmost", True)
                                yon1.title("Chasser de nouveau ?")
                                yon1.resizable(True, True)
                                yon1.geometry('400x100')
                                mainloop()
                                
                                if retry=="n":
                                    capture=False
                                    pygame.quit() #la fenetre pygame se ferme
                                    

# Variables à sauvegarder
data={'po': po,
      'su' : su,
      'hy' : hy,
      'ma' : ma,
      'objet' : objet,
      'PokedexOB' : PokedexOB,
      'PokedexMQ' : PokedexMQ}

# Ouverture du fichier en mode écriture binaire
with open('data.pickle', 'wb') as file:
    # Écriture des variables dans le fichier
    pickle.dump(data, file)