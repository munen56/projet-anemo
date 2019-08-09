
## import pandas as pd #lecture des fichier CSV, panda genere des dataframe:"two-dimensional labeled data structures with columns of potentially different types" voir https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
import csv

continu = "N"
while continu == "N":    #boucle principal du programme

    print ('-Bienvenus dans l\'utilitaire d\'étalonnage de WindTram-')
    print ('La procédure d\'étalonage vise a associer une vitesse de vent à chaque frequence de rotation de l\anémometre.')
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
            
        if unit == 1:
            unit = "Kt"
            sorti = True
            
        else:
            print ('Saisi incorect')

    
    print ('Deux méthodes sont proposés:')
    print ('')
    print ('La méthode Fichier utilise un fichier CSV contenant une gamme de vitesse et leur fréquences de rotation.')
    print ('La méthode Direct recupere en temps réel la fréquence transmise par l\'arduino et vous permet d\'y associer la vitesse correspondante.')
    print ('')
    print ('Choisissez votre méthode:')
    print ('0 Fichier')
    print ('1 Direct')

    methode = int(input())
    print (methode)
    
    if methode == 0 :
        print ('Méthode Fichier.')
        print ('Entrez le chemin d\'acces a votre fichier de données (.csv uniquement)')
        path = input()
        print (path)
##        data = pd.read_csv(path) 
        



    
    elif methode == 1 :
        print ('Méthode Direct.')
        print ('')
        print ('Indiquez la vitesse mini la vitesse maxi (en {0}) et le pas de votre echantillonage de vitesse:'.format(unit))
        
        mini = int(input("Entrez la vitesse mini:"))
        maxi = int(input("Entrez la vitesse maxi:"))
        step = int(input("Entrez le pas:"))

        speed = []
        for i in range(mini, maxi, step):
            speed.append(i)
            
        print ('Votre echantillonage sera réalisé pour les vitesse suivante:{0} {1}'.format(speed, unit))
        
##        on utilise ce code pour recuperer la freq en temps reel code pompé la http://www.isn.cligniez.fr/ressources/arduino-python.pdf
##        il manque le code qui permet de demander a l'arduino de transmettre des valeurs de freq brut, genre on met une var sur true dans le code arduino (au demarrage de la carte par exemple) qui permet l'execution du code qui transmet la frequence brut. 
##        import serial oooo a declarer en debut de code oooooo
##        ser = serial.Serial("COM4",timeout=1)
##        print (ser)
##        while 1:
##        frequence=str(ser.readline())
##        print(frequence)
##        la valeur de frequence retenu devra etre une moyenne sur x seconde
    
        
    
    else :
        print ("Saisi incorect")
        
    print ('Voulez vous quitter le programme ? (Y/N)')
    continu = input()
    
        



