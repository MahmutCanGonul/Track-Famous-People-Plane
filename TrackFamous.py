# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:47:24 2022

@author: Mahmut Can Gonol
"""

import requests
import pandas as pd
from IPython.display import display
import webbrowser
import datetime


data = {'Elon Musk':'https://opensky-network.org/aircraft-profile?icao24=a835af','Bill Gates':'https://opensky-network.org/aircraft-profile?icao24=ac39d6',
        'Michael Jordan':'https://opensky-network.org/aircraft-profile?icao24=a21fe6','Taylor Swift':'https://opensky-network.org/aircraft-profile?icao24=ac64c6',
        'John Travolta':'https://opensky-network.org/aircraft-profile?icao24=a96f69','Jim Carry':'https://opensky-network.org/aircraft-profile?icao24=a0f9e7',
        'Donald Trump':'https://opensky-network.org/aircraft-profile?icao24=aa3410','Jeff Bezos':'https://opensky-network.org/aircraft-profile?icao24=a2aa92',
        'Alan Sugar':'https://opensky-network.org/aircraft-profile?icao24=acb4c7'}


register_code_data = {'Elon Musk':'N628TS','Bill Gates':'N887WM',
        'Michael Jordan':'N236MJ','Taylor Swift':'N898TS',
        'John Travolta':'N707JT','Jim Carry':'N162JC',
        'Donald Trump':'N757AF','Jeff Bezos':'N271DV',
        'Alan Sugar':'G-SUGA'}


 


def calling_flights(country):
    lon_min,lat_min=28.741951,41.261297
    lon_max,lat_max=28.741951,41.261297
    user_name='USERNAME'
    password='PASSWORD'
    url_data = 'https://'+user_name+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)
    response=requests.get(url_data).json()
    data=[]
    if response['states'] != None:
       for i in range(len(response['states'])):
           if str(response['states'][i][2]) != None:
               code = str(response['states'][i][2])
               result = code == str(country)
               if result:
                  data.append(response['states'][i])
    if len(data) > 0:
        print(len(data))
        for i in range(len(data)):
            print(data[i])
    else:
        print("I can not a find a flight!")
        


def datetime_flight_info(callSign,date):
    url = f"https://aerodatabox.p.rapidapi.com/flights/callsign/{callSign}/{date}"
    headers = {
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
    'x-rapidapi-key': "843406cdb2msh623e555d8416d8ep1d7e8ajsnb9afd7d794c4"
    }
    response = requests.request("GET", url, headers=headers)
    json_data = response.json()
    re = response.text.split(':')
    result = None
    if len(re) > 2:
        result = json_data
    return result

def show_plane(callSign):
    url = "https://aerodatabox.p.rapidapi.com/aircrafts/reg/N887WM/image/beta"

    headers = {
    'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
    'x-rapidapi-key': "843406cdb2msh623e555d8416d8ep1d7e8ajsnb9afd7d794c4"
    }

    response = requests.request("GET", url, headers=headers)
    result = None
    if response.text:
        if 'url' in response.text:
            result = response.json()['url']
    return result
            
            

print(f"We have {len(data)} Famous Plane!")


keys = data.keys()
  
while True:
     count=0
     counts = []
     flight_info = []
     great_circle_distance=[]
     isTrueChoice = False
     for key in keys:
          count+=1
          counts.append(str(count)+","+str(key))
          print(f"'{count}' ==> Check {key} Jet")
     count+=2
     print(f"'{count-1}' ==> Track Plane from Call Sign ID")
     print(f"'{count}' ==> exit")
     try:
         choice = int(input("Enter a choice: "))
         for i in range(len(counts)):
             split_data = counts[i].split(',')
             if choice == int(split_data[0]):
                 print(split_data[1]+" flight history is coming :)")
                 date = datetime.datetime.now()
                 for i in range(7):
                     history = str(date).split(' ') # index '0' is history
                     result = datetime_flight_info(register_code_data[split_data[1]],str(history[0]))
                     if result != None:
                         flight_info.append(result)
                         for j in range(len(result)):
                             re = result[j]
                             if 'greatCircleDistance' in re:
                                 great_circle_distance.append(re['greatCircleDistance'])
                     date = date - datetime.timedelta(1)
                 
                 if len(flight_info) > 0:
                     temp=0
                     for i in range(len(flight_info)):
                         print(f"{i+1} ==> {flight_info[i]}")
                         temp+=1
                         if temp == 2:
                             print()
                             temp=0
                     print("Great Circle Distances: ")
                     for i in range(len(great_circle_distance)):
                         print(f"{i+1} ==> {great_circle_distance[i]}")
                 else:
                     print("There is no flight data on last 7 days!")
                 webbrowser.open(data[split_data[1]])
                 url_data = show_plane(register_code_data[split_data[1]])
                 if url_data:
                     webbrowser.open(url_data)
                 isTrueChoice = True
                 break
         if isTrueChoice == False:
             if choice == count:
                 break
             elif choice == count-1:
                 callSign = input("Enter a Call Sign of Flight: ")
                 if callSign:
                     calling_flights(callSign)
             else:
                  print("I don't understand your choice!")
          
     except Exception as ex:
         print(ex)
        
      
         
 




