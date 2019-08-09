Ce module de WindTram permet d'etalonner un capteur de vitesse, initialement anemo mais fonctionne pour les loch ou tout autre capteur qui renvoi un signal LINEAIRE
et codé en FREQUENCE.

Une fois les données acquise elles sont traité par regression lineaire, l'equation resultante est televersé dans l'arduino permettant a ce dernier de realiser
la conversion frequence vitese necessaire pour generer les trames NMEA.

La librairie Panda permet la lecture des CSV et peut etre trouvée a cette adresse https://pypi.python.org/pypi/pandas#downloads ou installer via la distribution anaconda