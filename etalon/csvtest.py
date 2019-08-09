import csv
from scipy import stats
#import matplotlib.pyplot as plt
from matplotlib import pyplot # voir comment faire un seul import
from matplotlib import plt
############################################### declaration

unit="Km/h"
path="C:/Users/User/Desktop/projet anemo/etalon/etalonnage.csv"
#################################################################### Lecture du csv
def importfile(path,col): #col 0 'vitesse(Km/h)'; col 1 'Freq[hz]\t' ##recupere les valeurs du fichier csv colonne par colonne et suprime l'en-tete
    # penser a verifier le format du csv npotament su header et extraire l'info noeud ou kmh qu'il contient
    data=[]
  
    x= open(path, newline='')
    reader = csv.reader(x)
    for row in reader:
        data.append(row[col])
        
    data=data[1:len(data)] # on retire la premiere ligne (l'en-tete)
    
    for i in range(0,len(data)):  #csv reader renvoie une liste de str on transforme en float
        data[i] = float(data[i])
    
    return data #renvoi une liste de float

speed = importfile(path,0)  # on recupere la liste des vitesse verifier l'ordre dans l'en-tete csv
freq = importfile(path,1)  # on recupere la liste des freq



print ("vitesse", speed) 
print ('')
print ("freq", freq)
######################################################################## regression

slope, intercept, r_value, p_value, std_err = stats.linregress(speed,freq) # calcul de la reg lineaire 

######################################################################## affichage du graph
def affichagegraph(slope, intercept, r_value, unit):

    print (slope , "x + " , intercept) # sortie console du R^2 et  Ax + B (optionel)
    print ("r-squared =", r_value**2)

    y=[] # on bricole en creant le y, il est utilisé pour tracer la fitted line
    for i in range(0,len(speed) ): 
        y.append( intercept + slope*speed[i])

    
    pyplot.title('y={0}X+{1}  R2={2}'.format(slope,intercept,r_value**2))
    pyplot.suptitle('Frequence en sortie du capteur en fonction de la Vitesse mesurée')
    axes = plt.axes()
    axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe
    axes.set_xlabel('vitesse({0})'.format(unit))
    axes.set_ylabel('Frequence(Hz)')
    plt.scatter(speed,freq) # speed et freq sont envoyer en param x et y
    plt.plot(speed, y, 'r', label='fitted line')
    plt.legend()
    plt.show()
    return


affichagegraph(slope, intercept, r_value, unit)



