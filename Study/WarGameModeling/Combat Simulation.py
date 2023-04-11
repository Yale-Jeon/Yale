import random as rd

global B_tank
global B_antitank
global R_tank
global R_antitank
global War

B_tank=[1,1,1,1,1]  # 1
B_antitank=[1,1,1] # 2
R_tank=[1,1,1,1,1,1] # 3
R_antitank=[1,1,1,1] # 4
War=[0,B_tank,B_antitank,R_tank,R_antitank]
Hit_table=[[0,0,0.4,0.5],[0,0,0.2,0],[0.3,0.3,0,0],[0.1,0,0,0]]
event=[]
# element of event : [time,[attack group, attack member], [targeted group, targeted member]]
def add(event,x):
    for i in range(len(event)):
        if x[0]<event[i][0]:
            event.insert(i,x)
            return event
    event.append(x)
    return event

def target(a):
    if a==1:
        A=sum(R_tank)
        B=sum(R_antitank)
        C=A+B
        rand=int(C*rd.random())
        if rand <= A-1:
            for i in range(len(R_tank)):
                if R_tank[i]==1:
                    if rand==0:
                        return [3, i]
                    else:
                        rand -= 1
        else:
            rand -= A
            for i in range(len(R_antitank)):
                if R_antitank[i]==1:
                    if rand==0:
                        return [4,i]
                    else:
                        rand -= 1
    elif a==2:
        A=sum(R_tank)
        rand = int(A * rd.random())
        for i in range(len(R_tank)):
            if R_tank[i] == 1:
                if rand == 0:
                    return [3, i]
                else:
                    rand -= 1
    elif a==3:
        A=sum(B_tank)
        B=sum(B_antitank)
        C=A+B
        rand=int(C*rd.random())
        if rand <= A-1:
            for i in range(len(B_tank)):
                if B_tank[i]==1:
                    if rand==0:
                        return [1, i]
                    else:
                        rand -= 1
        else:
            rand -= A
            for i in range(len(B_antitank)):
                if B_antitank[i]==1:
                    if rand==0:
                        return [2,i]
                    else:
                        rand -= 1
    elif a==4:
        A=sum(B_tank)
        rand = int(A * rd.random())
        for i in range(len(B_tank)):
            if B_tank[i] == 1:
                if rand == 0:
                    return [1, i]
                else:
                    rand -= 1
    return [0,0]

def targeting_time(a):
    rand=rd.random()
    if a==1:
        if rand<0.5:
            return 3+(2*rand)**(0.5)
        else:
            return 5-(2-2*rand)**(0.5)
    elif a==2:
        if rand<0.5:
            return 2+3*(2*rand)**(0.5)
        else:
            return 8-3*(2-2*rand)**(0.5)
    elif a==3:
        if rand<0.5:
            return 2+2*(2*rand)**(0.5)
        else:
            return 6-2*(2-2*rand)**(0.5)
    elif a==4:
        if rand<0.5:
            return 4+(2*rand)**(0.5)
        else:
            return 6-(2-2*rand)**(0.5)

def hitting_time(a):
    if a == 1:
        return 2*rd.random()+1
    elif a==3:
        return 2*rd.random()+2


# initial part
for i in range(len(B_tank)):
    event.append([0,[1,i],[0,0]])
for i in range(len(B_antitank)):
    event.append([0,[2,i],[0,0]])
for i in range(len(R_tank)):
    event.append([0,[3,i],[0,0]])
for i in range(len(R_antitank)):
    event.append([0,[4,i],[0,0]])


# simulation part
while True:
    if War[event[0][1][0]][event[0][1][1]] == 1:
        if event[0][2][0] == 0:
            event = add(event, [event[0][0] + targeting_time(event[0][1][0]), event[0][1], target(event[0][1][0])])
        else:
            prob = Hit_table[event[0][1][0]-1][event[0][2][0]-1]
            rand = rd.random()
            if War[event[0][2][0]][event[0][2][1]]==0:
                if event[0][1][0]==1 or event[0][1][0]==3:
                    event = add(event, [event[0][0] + hitting_time(event[0][1][0]), event[0][1], target(event[0][1][0])])
                else:
                    event = add(event, [event[0][0] + targeting_time(event[0][1][0]), event[0][1], target(event[0][1][0])])
            else:
                if rand < prob:
                    War[event[0][2][0]][event[0][2][1]] = 0
                    print(sum(B_tank),sum(B_antitank),sum(R_tank),sum(R_antitank))
                    if event[0][1][0]==1 or event[0][1][0]==3:
                        event = add(event, [event[0][0] + hitting_time(event[0][1][0]), event[0][1], target(event[0][1][0])])
                    else:
                        event = add(event, [event[0][0] + targeting_time(event[0][1][0]), event[0][1], target(event[0][1][0])])
                else:
                    if event[0][1][0]==1 or event[0][1][0]==3:
                        event = add(event, [event[0][0] + hitting_time(event[0][1][0]), event[0][1], event[0][2]])
                    else:
                        event = add(event, [event[0][0] + targeting_time(event[0][1][0]), event[0][1], event[0][2]])
    event.pop(0)

    if sum(B_tank)+sum(B_antitank)==0:
        print("Red is win")
        break
    elif sum(R_tank)+sum(R_antitank)==0:
        print("Blue is win")
        break

    if len(event)==0:
        break
