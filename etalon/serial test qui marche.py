
import serial#gestion des com sur port serie 
import time #pause d'x seconde


def serialconnect(mode,vitesseEtalon,unit,eq=0): # mode 42=etallonage fichier, 43=etallonage direct 44=retour de l'eq(optionnel); eq y=ax+b de la regression lineaire
    count = 0
    freqSum = 0.0
    freqMoy = []
    duréeEchantillonage = 5
    #freqBrut = []
    freqEtalon = []
    donnéeSauvegardée  = {"speed":vitesseEtalon,"freq":[],"unité":unit} #on initialise un dict qui contiendra toule les valeurs
    

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
            freqSum=0  
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
       
    return freqMoyenne


serialconnect(43,[10,20,30],"Km/h")
