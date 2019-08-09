int codeDeDemarrage;

void setup() {
  pinMode(13,OUTPUT);
  codeDeDemarrage = 0;
  Serial.begin(9600);
/*  while(codeDeDemarrage < 21) //on verifie deux fois par seconde si des donnée arrive du port serie, si un entier arrive on le recupere comme code de demarrage ////si ca ne marche pas voir avec mili
  {
    //Serial.print("arduino en attente  ");
    //Serial.print(codeDeDemarrage);
    //Serial.println("/21");
    codeDeDemarrage+=1;
    if (Serial.available()) //s'il y a des données qui arrivent
    {
      codeDeDemarrage = Serial.parseInt();//Lecture d'un entier sur le tampon série
    
    }
    delay(500);  
  }
 */
 // if (codeDeDemarrage==43)
 // {
    // si code 43
   // Serial.println("MODE ETALONNAGE DIRECT");
    while (true)
    {
      Serial.print("bla");
      digitalWrite(13,HIGH);
      delay(100);
      digitalWrite(13,LOW);
      delay(100);
   }

  
}

void loop() {
  // put your main code here, to run repeatedly:

}
