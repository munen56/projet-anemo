

##$--MWV,x.x,a,x.x,a*hh<CR><LF>
##$--MWV,1,2,3,4*hh<CR><LF>
##1=Wind Angle, 0 to 360 degrees 	2=Reference, R = Relative, T = True 	3=Wind Speed 	4=Wind Speed Units, K/M/N 
##5=Status, A = Data Valid 	6=Checksum 		
##tram entre $ et * puis checksum
##en C une lib le fait: libnmea a voir pour arduino

#$--MWV,290.0,R,30.0,K*hh<CR><LF>
unit = "K"
windspeed = 30.0
angle = 180.0
checksum = "hh"
nmeawithout=""

count = 0
while count<10:

    for i in range(5):
        angle +=i
        windspeed -=i
        
    
    for i in range(5):
        angle -=i
        windspeed +=i
        nmeawithout ="--MWV,"+'angle'+",R,"+windspeed+","+'unit'
        
        nmeacheck = print ("${}*{}".format(nmeawithout,checksum))
        
    
    count=count+1
    
    


