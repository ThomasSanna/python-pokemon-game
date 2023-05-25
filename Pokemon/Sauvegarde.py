import pickle

#Sérialisation des données : Python objet -> fichier binaire (data.pickle)

#initialisation des quantités de pokeballs

po = 0
su = 0
hy = 0
ma = 0
objet = 0

try: # On essaie de lire le fichier
    
    # Ouverture du fichier en mode lecture binaire
    with open('data.pickle', 'rb') as file:
        # Chargement des variables depuis le fichier
        data = pickle.load(file)
except FileNotFoundError: # Si le fichier n'existe pas
    print("Le fichier 'data.pickle' est absent.") 
    data = {}  # On crée un dictionnaire vide

# Récupération des valeurs des variables
po = data.get('po', 0)
su = data.get('su', 0)
hy = data.get('hy', 0)
ma = data.get('ma', 0)
objet = data.get('objet', 0)
PokedexOB = data.get('PokedexOB', 0)
PokedexMQ = data.get('PokedexMQ', 0)