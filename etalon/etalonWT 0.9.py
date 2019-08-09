import serial #com sur le port serie avec arduino
import csv #lecture des fichier CSV
from scipy import stats # fonction de regression lineaire
import matplotlib.pyplot as plt #affichage d'un graph
from matplotlib import pyplot # voir comment faire un seul import de matplotlib
import time #pause d'x seconde

######################################################################### com avec arduino et obtention des frequences
def serialconnect(mode,unit,vitesseEtalon=0,eq=0): # mode 42=etallonage fichier, 43=etallonage direct 44=retour de l'eq(optionnel); eq y=ax+b de la regression lineaire
    count = 0
    freqSum = 0.0
    freqMoy = []
    duréeEchantillonage = 5
    #freqBrut = []
    freqEtalon = []
    #donnéeSauvegardée  = {"speed":vitesseEtalon,"freq":[],"unité":unit} #on initialise un dict qui contiendra toule les valeurs
    

    ser = serial.Serial("COM3",timeout=1) #  //Le port utilisé est ici COM3
    print ('connexion serie établie')
    print(ser)
    print('')
    print('vous pouvez maintenant mettre votre arduino sous tension')
    print("pressez entrez immediatement apres avoir mis Arduino sous tension (5s maximum)")
    # a ce moment arduino demarre, le premier code qu'il execute lit le tampon serie si 42
    # si 42 est present il passe en mode etalonnage fichier
    #si 43 est present il demarre en mode etalonnage direct
    #si 44 on transmet le code puis l'eq

    
     
    
   
    if mode == 42 or mode == 43:#transmet le code correspondant aux différents mode
        
        wait=input("")#l'input semble necessaire au fonctionnement de ser.write ???
        code=str(mode) #on transforme le code en str (format necessaire a l'envoi via ser.write) l'envoi via  
        ser.write(code.encode('utf-8')) #envoi du code a l'arduino
        #while 1:
         #    print (ser.readline().decode('utf-8'))
        
        while str(ser.readline()) == "b''": #si quelque chose arrive sur le tampon on l'enregistre
            print ('Synchronisation en cours')
            time.sleep(1)# introduit une pause d'une seconde
        print     
        print ('synchronisation réussie')
       

        print ('L\'etalonnage va maintenant commencer.')
        print("")
        for vitesse in vitesseEtalon:
            count = 0
            freqSum=0
            freqEtalon = []
            print ('Vitesse a tester: {0}{1}'.format(vitesse,unit))
            print ('')
            wait = input('appuyer sur entrer quand la vitesse est stabilisée à {0}{1}, l\'echantillonage dure {2} secondes'.format(vitesse,unit,duréeEchantillonage))

            while count <= duréeEchantillonage: #regle le temps d'echantillonage a partir du moment ou les données arrivent
                donnee = float(ser.readline().decode('utf-8'))#on lit le tampon serie, on utilise .decode pour recuperer le nombre seul en string et float() pour en faire un nombre a virgule
                time.sleep(1)# introduit une pause d'une seconde
            
                if donnee != "b''": #si quelque chose arrive sur le tampon on l'enregistre
                    
                    freqEtalon.append(donnee) #list qui contient duréeEchantillonage valeurs
                    count+=1
                 
            for val in freqEtalon: # on fait la moyenne des frequences
                freqSum += float(val)
                #print(freqSum)
                
            freqMoy .append ( freqSum/len(freqEtalon) )

            
            print (freqEtalon)
            print (freqMoy,'Hz')
            print ('')
            
               
        
        
    elif mode == 44:
        while 1:
            
            ser.write(43)
       
    return freqMoy
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
def affichagegraph(slope, intercept, r_value, unit, freq=0, speed=0):
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


#########################################################################################################################
############################################################################################################################
###########################################################################################################################

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

    
    print ('Trois méthodes sont proposés:')
    print ('')
    print ('La méthode Fichier utilise un fichier CSV contenant une gamme de vitesse et les fréquences de rotation correspondantes.')
    print ('La méthode Direct recupere en temps réel la fréquence transmise par l\'arduino et vous permet d\'y associer la vitesse correspondante.')
    print ('La methode Equation transmet simplement l\'équation déja calculé par vos soins')
    print ('')
    print ('Choisissez votre méthode:')
    print ('0 Fichier')
    print ('1 Direct')
    print ('2 Equation')

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

        speedRange = []
        freq = []

        for i in range(mini, maxi, step): #on genere une liste de vitesse etalon
            speedRange.append(float(i))
            
        print ('Votre etalonnage sera réalisé pour les vitesse suivante:{0} {1}'.format(speedRange, unit))

        ####################################################################### Connexion a arduino pour recuperer la list
        freqDirect = serialconnect(43,unit,speedRange)
        ######################################################################## regression
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(freqDirect,speedRange) # calcul de la reg lineaire 
        
        ##################################################### on affiche
        affichagegraph(slope, intercept, r_value, unit, freqDirect, speedRange)
        ########################################################### fin de la methode direct
        
        
    elif methode == 2 :
        print("Méthode Equation")
        print ('')
        print ('L\'equation est de la forme y = ax + b')
        slope = input("Entré a :" )
        intercept = input("Entré b :")
        
           
    else :
        print ("Saisi incorect")
        
    print ('Voulez vous quitter le programme ? (Y/N)')
    continu = input()
    
        



