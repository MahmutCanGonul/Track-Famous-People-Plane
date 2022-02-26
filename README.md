# Track-Famous-People-Plane
Track Famous People Plane With Python


In this code you can check that famous people going to which place with plane. If the flight has live data, you can instantly observe the departure of the aircraft.

Which celebrities can you follow?:

Bill Gates:

![image](https://user-images.githubusercontent.com/75094927/155206796-16975053-420e-4f16-9be6-bc5b3f371960.png)


Donald Trump:

![image](https://user-images.githubusercontent.com/75094927/155206566-38234eb1-1199-40fd-8a6f-536ca15702af.png)


Elon Musk:

![image](https://user-images.githubusercontent.com/75094927/155206622-b6b24a11-a821-4868-96bc-32549d179c64.png)



Taylor Swift:

![image](https://user-images.githubusercontent.com/75094927/155206665-15ab1f6a-579a-490e-b3b4-0155e26147bc.png)


Michael Jordan:

![image](https://user-images.githubusercontent.com/75094927/155206739-c5bd7bfa-efcb-4573-85d5-9abe7cd10bae.png)


Jim Carry:

![image](https://user-images.githubusercontent.com/75094927/155206905-049c42f6-d4d3-46dd-9762-79143a992fe7.png)


John Travolta:

![image](https://user-images.githubusercontent.com/75094927/155206938-d2a7276e-998c-422b-a4ec-31a842041c36.png)

Jeff Bezos:

![image](https://user-images.githubusercontent.com/75094927/155568307-38ea1673-444a-47d7-82d2-9f31f8d3c2df.png)


 



💣Code:



     import webbrowser





    data = {'Elon Musk':'https://opensky-network.org/aircraft-profile?icao24=a835af','Bill Gates':'https://opensky-network.org/aircraft-profile?icao24=ac39d6',
        'Michael Jordan':'https://opensky-network.org/aircraft-profile?icao24=a21fe6','Taylor Swift':'https://opensky-network.org/aircraft-profile?icao24=ac64c6',
        'John Travolta':'https://opensky-network.org/aircraft-profile?icao24=a96f69','Jim Carry':'https://opensky-network.org/aircraft-profile?icao24=a0f9e7',
        'Donald Trump':'https://opensky-network.org/aircraft-profile?icao24=aa3410'}



     keys = data.keys()
 
 
     while True:
           count=0
           counts = []
           isTrueChoice = False
           for key in keys:
                 count+=1
                 counts.append(str(count)+","+str(key))
                 print(f"'{count}' ==> Check {key} Jet")
      count+=1
      print(f"'{count}' ==> exit")
      try:
          choice = int(input("Enter a choice: "))
           for i in range(len(counts)):
               split_data = counts[i].split(',')
               if choice == int(split_data[0]):
                  print(split_data[1]+" flight history is coming :)")
                  webbrowser.open(data[split_data[1]])
                   isTrueChoice = True
                   break
           if isTrueChoice == False:
               if choice == count:
                   break
                else:
                    print("I don't understand your choice!")
          
      except Exception as ex:
          print(ex)
        
    
    
OUTPUT:

💣Output is given json data about famous people flights

![FlightHistory](https://user-images.githubusercontent.com/75094927/155841779-50b043dd-0e1d-4df1-a215-a2cf85e7f7a1.png)

    
    
    
    
    
References:
 
 https://opensky-network.org/

https://rapidapi.com/aedbx-aedbx/api/aerodatabox/





