
import serial#gestion des com sur port serie 
import time #pause d'x seconde


def serialconnect(mode,eq): # mode 42=etallonage fichier, 43=etallonage direct 44=retour de l'eq; eq y=ax+b de la regression lineaire
    count = 0
    donnéeSauvegardée  = {"speed":[],"freq":[]}

    ser = serial.Serial("COM3",timeout=1) #  //Le port utilisé est ici COM3
    print ('connexion serie établie')
    print(ser)
    print('')
    print('vous pouvez maintenant mettre votre arduino sous tension')
    print("pressez entrez immediatement apres avoir mis Arduino sous tension (10s maximum)")
    # a ce moment arduino demarre, le premier code qu'il execute lit le tampon serie si 42
    # si 42 est present il passe en mode etalonnage fichier
    #si 43 est present il demarre en mode etalonnage direct
    #si 44 on transmet le code pui l'eq

    
     
    
   
    if mode == 42 or mode == 43:#transmet le code correspondant aux différents mode
        
        wait=input("")
        code=str(mode)   
        ser.write(code.encode('utf-8'))

        print ('')
        
        
        
        while 1:
            donnee=str(ser.readline())
            print(donnee)
            time.sleep(1)# introduit une pause d'une seconde
            
        
    elif mode == 44:
        while 1:
            
            ser.write(43)
       
    return #rien pour l'instant mais un message d'etat serait pas mal


serialconnect(43,2)
