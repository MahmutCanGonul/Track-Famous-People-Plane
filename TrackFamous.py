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
        
      
