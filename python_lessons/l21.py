import urllib.request
import matplotlib.pyplot as plt

import pandas as pd

import datetime

'''
x = 1
y = 2
print(x)
print(y)
l = list(map(float,[x,y]))
print(l)
l2 = list(map(str,[x,y]))
print(l2)
l1 = list([x,y])
print(l1)
'''

# public data - covid
urldata = urllib.request.urlopen('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
data = urldata.read()

lines = data.splitlines()
lines.reverse()

totalC = int(0)
totalD = int(0)
totalC1 = int(0)
totalD1 = int(0)
t = []

C = []
D = []

C1 = []
D1 = []

d = 0
for line1 in lines:
    if 'Slovakia' in str(line1):
        items = str(line1).replace("b'", "").replace("'", "").split(",")
        totalC += int(items[4])
        totalD += int(items[5])
        d += 1
        t.append(d)
        C.append(totalC)
        D.append(totalD)

print(totalC)
print(totalD)


fig = plt.figure(figsize=plt.figaspect(2.))
fig.suptitle('COVID in Slovakia')

# First subplot
ax = fig.add_subplot(2, 1, 1)
ax.plot(t, C, 'b')
ax.grid(True)
ax.set_ylabel('Number of cases')
ax.set_xlabel('Day')
ax = fig.add_subplot(2, 1, 2)
ax.plot(t, D, 'g')

plt.show()

lines2 = str(lines).replace("b'", "").replace("'", "").split()

lines3 = list([i.split(',') for i in lines2])
lines4 = list(filter(lambda x : ("Czech") in x or ("Slovakia" ) in x,lines2))
lines5 = sorted(lines4)
#print(lines4[1:10000])

#print(lines[0])

dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')

covid_data= pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv', parse_dates=[0],date_parser=dateparse)

covid_data.columns =  ['Last Update', 'Day', 'Month', 'Year', 'NewCases','Deaths','Country','Region','Region2','ID']


r_data_CZ = covid_data[covid_data['Country']=='Czechia' ]
r_data_SK = covid_data[covid_data['Country']=='Slovakia' ]

#r_data = r_data.groupby(["Country"])["NewCases", "Deaths"].sum().reset_index()
r_data_CZ = r_data_CZ.sort_values(by='Last Update', ascending=True)
r_data_SK = r_data_SK.sort_values(by='Last Update', ascending=True)

#r_data = r_data[r_data['Deaths']>1]
plt.figure(figsize=(15, 5))
plt.plot(r_data_CZ['Last Update'], r_data_CZ['NewCases'],color='red')
plt.plot(r_data_CZ['Last Update'], r_data_CZ['Deaths'],color='green')

plt.plot(r_data_SK['Last Update'], r_data_SK['NewCases'],color='blue')
plt.plot(r_data_SK['Last Update'], r_data_SK['Deaths'],color='yellow')

 
plt.title('Load data with pandas')
plt.show()
#print(r_data_SK)