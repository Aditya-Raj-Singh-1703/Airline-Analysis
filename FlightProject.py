import pandas as pd

airports='airports_mod.dat'
finalairlines='Final_airlines'
route='routes.dat'

airports_names=['ID','Name','City','Country','IATA/FAA','IACO','Latitude','Longitude','Altitude','Timezone','DST','TZ']
finalairlines_names=['ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']
route_names=['Airline','ID','Source','SID','Destination','DID','Codeshare','Stops','Equipment']

airports_data=pd.read_csv(airports,sep=',',names=airports_names)
finalairlines_data=pd.read_csv(finalairlines,sep=',',names=finalairlines_names)
route_data=pd.read_csv(route,sep=',',names=route_names)

def A():
    a=[]
    b=airports_data.groupby(['Name','Country'])
    for i in b:
        if i[0][1]=='India':
            a.append(i[0][0])
    print("List of Airports operating in India are: \n",a)


def B():
     c=[]
     d=route_data.groupby(['Airline','Stops'])
     for i in d:
         if i[0][1]==0:
             c.append(i[0][0])
     print("Airlines having zero stops are:\n",c)

def C():
    e=[]
    f=route_data.groupby(['Airline','Codeshare'])
    for i in f:
        if i[0][1]=='Y':
            e.append(i[0][0])
    print("Airlines operating with codeshare are:",e)

def D():
    j = []
    k=airports_data['Altitude']
    for i in k:
        j.append(i)
    k=airports_data.groupby('Altitude')
    print('The country having highest Airport:\n',k.get_group(max(j))[['Country', 'Name', 'Altitude']])

def E():
    l=[]
    m=finalairlines_data.groupby(['Name','Country','Active'])
    for i in m:
        if i[0][2]=='Y' and i[0][1]=='United States':
            l.append(i[0][0])
    print("List of Active airports in United States:\n",l)


x='y'
while x is 'y':
    v=input("\nEnter A to view List of Airports operating in India\nEnter B to view Airlines having zero stops\nEnter C to view Airlines operating with codeshare\nEnter D to view The country having highest Airport\nEnter E to view List of Active airports in United States\nEnter Q to quit\n")
    if v is 'A':
        A()
    elif v is 'B':
        B()
    elif v is 'C':
        C()
    elif v is 'D':
        D()
    elif v is 'E':
        E()
    elif v is 'Q':
        break
    else:
        x=input("Wrong Input. Want to continue? y/n\n")
        if x is 'y':
            continue
        else:
            break