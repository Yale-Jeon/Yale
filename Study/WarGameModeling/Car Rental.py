import math
import random as rd

def interarrival(i):
    lamb=[0,14/3600,10/3600,24/3600]
    x=math.log(1-rd.random())
    x=(-1)*x/lamb[i]
    return int(x)

def unloadtime():
    return int(8*rd.random()+16.5)

def loadtime():
    return int(10*rd.random()+15.5)

def destination(i):
    if i == 3:
        if rd.random() < 0.583:
            return 1
        else:
            return 2
    else:
        return 3

Time=540
Bus=[]
Bus_location=1
Busloc=[0,2,3,1]
transit_time=[0,120,540,540]
loc_1=[]
loc_2=[]
loc_3=[]
loc_1_time=0
loc_2_time=0
loc_3_time=0
location=[0,loc_1,loc_2,loc_3]
location_time=[0,loc_1_time,loc_2_time,loc_3_time]
avg1=[0,0,0]
max1=[0,0,0]
avg2=[0,0,0]
max2=[0,0,0]
avg3=0
max3=0
avg4=[0,0,0]
max4=[0,0,0]
min4=[9999,9999,9999]
avg5=[0,0,0]
max5=[0,0,0]
min5=[9999,9999,9999]
avg6=0
max6=0
min6=9999
loop=[-1,-1,-1,0]
num2=[0,0,0]
num3=0
num4=[0,0,0]
num5=[0,0,0]
num6=0
simulation_time = 288000

while Time < simulation_time:
    departure_time=Time+300
    if len(Bus) != 0:
        remove_list=[]
        for people in Bus:
            if people[1] == Bus_location:
                remove_list.append(people)
                Time += unloadtime()
                avg6 += Time - people[0]
                num6 += 1
                if max6 < Time - people[0]:
                    max6 = Time - people[0]
                if min6 > Time - people[0]:
                    min6 = Time - people[0]
        for remove in remove_list:
            Bus.remove(remove)

    ans1 = 0
    while True:
        if len(location[Bus_location]) == 0:
            location_time[Bus_location] += interarrival(Bus_location)
            location[Bus_location].append([location_time[Bus_location], destination(Bus_location), 0])
            ans1 += 1
        if len(Bus) >= 20:
            break
        if location[Bus_location][0][0] > Time:
            if location[Bus_location][0][0] <= departure_time:
                delay = Time - location[Bus_location][0][0]
                avg2[Bus_location-1] += delay
                num2[Bus_location-1]+=1
                if delay > max2[Bus_location-1]:
                    max2[Bus_location-1] = delay
                Time += loadtime()
                location[Bus_location][0][2] = Time
                Bus.append(location[Bus_location][0])
                location[Bus_location].remove(location[Bus_location][0])
            else:
                if Time < departure_time:
                    Time = departure_time
                break
        else:
            delay = Time - location[Bus_location][0][0]
            avg2[Bus_location-1] += delay
            num2[Bus_location-1] += 1
            if delay > max2[Bus_location - 1]:
                max2[Bus_location - 1] = delay
            Time += loadtime()
            location[Bus_location][0][2] = Time
            Bus.append(location[Bus_location][0])
            location[Bus_location].remove(location[Bus_location][0])

    if max1[Bus_location-1] < ans1:
        max1[Bus_location-1] = ans1

    avg3 += len(Bus)
    num3 += 1
    if len(Bus)>max3:
        max3 = len(Bus)

    avg4[Bus_location-1] += Time-departure_time+300
    num4[Bus_location-1] += 1
    if min4[Bus_location-1] > Time-departure_time+300:
        min4[Bus_location-1] = Time - departure_time + 300
    if Time-departure_time > max4[Bus_location-1]:
        max4[Bus_location-1] = Time-departure_time

    if loop[Bus_location] != -1:
        avg5[Bus_location-1] += Time - loop[Bus_location]
        num5[Bus_location-1] += 1
        if max5[Bus_location-1] < Time - loop[Bus_location]:
            max5[Bus_location - 1] = Time - loop[Bus_location]
        if min5[Bus_location-1] > Time - loop[Bus_location]:
            min5[Bus_location - 1] = Time - loop[Bus_location]
    loop[Bus_location] = Time

    Time += transit_time[Bus_location]
    Bus_location = Busloc[Bus_location]



avg1[0] = avg2[0]/simulation_time
avg1[1] = avg2[1]/simulation_time
avg1[2] = avg2[2]/simulation_time

avg2[0] = avg2[0]/num2[0]
avg2[1] = avg2[1]/num2[1]
avg2[2] = avg2[2]/num2[2]

avg3 = avg3 / num3

avg4[0] = avg4[0]/num4[0]
avg4[1] = avg4[1]/num4[1]
avg4[2] = avg4[2]/num4[2]

avg5[0] = avg5[0]/num5[0]
avg5[1] = avg5[1]/num5[1]
avg5[2] = avg5[2]/num5[2]

avg6 = avg6 / num6

print(avg1)
print(max1)
print(avg2)
print(max2)
print(avg3)
print(max3)
print(avg4)
print(max4)
print(min4)
print(avg5)
print(max5)
print(min5)
print(avg6)
print(max6)
print(min6)