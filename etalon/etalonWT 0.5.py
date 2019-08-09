
import csv #lecture des fichier CSV
from scipy import stats # fonction de regression lineaire
import matplotlib.pyplot as plt #affichage d'un graph
from matplotlib import pyplot # voir comment faire un seul import de matplotlib

#################################################################### Lecture du csv
def importfile(path,col): #col 0 'vitesse(Km/h)'; col 1 'Freq[hz]\t' ##recupere les valeurs du fichier csv colonne par colonne et suprime l'en-tete
    # penser a verifier le format du csv notament su header et extraire l'info noeud ou kmh qu'il contient
    data=[]
  
    x= open(path, newline='')
    reader = csv.reader(x)
    for row in reader:
        data.append(row[col])
        
    data=data[1:len(data)] # on retire la premiere ligne (l'en-tete)
    
    for i in range(0,len(data)):  #csv reader renvoie une liste de str on transforme en float
        data[i] = float(data[i])
    
    return data #renvoi une liste de float

######################################################################## affichage du graph
def affichagegraph(slope, intercept, r_value, unit):
    print ('######################################################')
    print ('Equation de la droite de régression')
    print ("y={0}x + {1} ".format(slope, intercept)) # sortie console du R^2 et  Ax + B (optionel)
    print ('')
    print ("R-squared = {0}".format(r_value**2))
    print ('')
    print ('Le R-squared vous donne une idée de la qualité de la modélisation des données par la regression')
    print (' plus il est proche de 1.0 meilleur est l\'ajustement')
    print (' un R-squared trop faible peut etre du a un mauvais protocole d\'echantillonage ou a un capteur delivrant un signal NON linéaire')
    print ('######################################################')
    wait = input("Entrez pour continuer")

    y=[] # on bricole en creant le y, il est utilisé pour tracer la fitted line
    for i in range(0,len(freq) ): 
        y.append( intercept + slope*freq[i])

    
    pyplot.title('y={0}X+{1}  R2={2}'.format(slope,intercept,r_value**2))
    pyplot.suptitle('Frequence en sortie du capteur en fonction de la Vitesse mesurée')
    axes = plt.axes()
    axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
    axes.set_ylabel('vitesse({0})'.format(unit))
    axes.set_xlabel('Frequence(Hz)')
    plt.scatter(freq,speed) # speed et freq sont envoyer en param x et y
    plt.plot(freq, y, 'r', label='fitted line')
    plt.legend()
    plt.show()
    return





continu = "N"
while continu == "N":    #boucle principal du programme

    print ('-Bienvenus dans l\'utilitaire d\'étalonnage de WindTram-')
    print ('La procédure d\'étalonage vise a associer une vitesse de vent à chaque frequence de rotation de l\'anémometre.')
    print ('Le traitement de ces données via une regression lineaire permettra de determiner la vitesse réel du vent avec un minimum d\'erreur.')
    print ('')

    sorti = False
    while sorti == False:
        print ('Avant toute choses vous devez choisir l\'unitée de vitesse utilisé, il est entendu que la fréquence sera exprimé en Hz')
        print ('0 Km/h')
        print ('1 Noeud')
        print ('"Entrez le chiffre correspondant a votre choix"')
    
        unité = int(input())
        unit = ""
        
        if unité == 0:
            unit="Km/h"
            sorti = True
            break
            
        if unité == 1:
            unit = "Kt"
            sorti = True
            break
            
        else:
            print ('Saisi incorect')

    
    print ('Deux méthodes sont proposés:')
    print ('')
    print ('La méthode Fichier utilise un fichier CSV contenant une gamme de vitesse et les fréquences de rotation correspondantes.')
    print ('La méthode Direct recupere en temps réel la fréquence transmise par l\'arduino et vous permet d\'y associer la vitesse correspondante.')
    print ('')
    print ('Choisissez votre méthode:')
    print ('0 Fichier')
    print ('1 Direct')

    methode = int(input())
    
    
    if methode == 0 :
        print ('Méthode Fichier.')
        print ('Entrez le chemin d\'acces a votre fichier de données (.csv uniquement)')
        path = input()
        path="C:/Users/User/Desktop/projet anemo/etalon/etalonnage.csv" #pour les test

        
        speed = importfile(path,0) #recupere les vitesses sous forme de liste 
        freq = importfile(path,1)  #idem pour les freq
        print ('######################################################')
        print ('Votre fichier contient {0} point d\'etalonnage'.format(len(speed)))
        print ('')
        print ("vitesse{0}({1})".format(speed,unit)) #on les affiche pour verif
        print ('')
        print ("freq   {0}(Hz)".format(freq))
        print ('######################################################')
        wait = input("Entrez pour continuer")
        
        ######################################################################## regression

        slope, intercept, r_value, p_value, std_err = stats.linregress(freq,speed) # calcul de la reg lineaire 
        
        #####################################################
        
        affichagegraph(slope, intercept, r_value, unit) #on affiche le resultat
        

        
        
        



    
    elif methode == 1 :
        print ('Méthode Direct.')
        print ('')
        print ('Indiquez la vitesse mini la vitesse maxi (en {0}) et le pas de votre echantillonage de vitesse:'.format(unit))
        
        mini = int(input("Entrez la vitesse mini:"))
        maxi = int(input("Entrez la vitesse maxi:"))
        step = int(input("Entrez le pas:"))

        speed = []
        for i in range(mini, maxi, step): #on genere une liste de vitesse etalon
            speed.append(i)
            
        print ('Votre etalonnage sera réalisé pour les vitesse suivante:{0} {1}'.format(speed, unit))
        
    
    else :
        print ("Saisi incorect")
        
    print ('Voulez vous quitter le programme ? (Y/N)')
    continu = input()
    
        



