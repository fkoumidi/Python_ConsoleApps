import random as rn
import os


#main programm


with open ('cl.txt','r') as cl:
    clteams=cl.readlines()
dclteams={}
for i in range(len(clteams)):
    y=clteams[i]
    y=y[:-2]
    clteams[i]=y
    a,b,c=y.split(',')
    dclteams[int(a[0:2])]=[a[4:len(a)-1],b[1:4],c[1:]]
##print(dclteams[2][0])   
##print(dclteams)
print('Teams for the UEFA Champions League\n')
drawteams={}
for i in range(1,9):
    drawteams[i]=dclteams.get(i)
    print(drawteams[i])
while (len(drawteams)<17):
    x=rn.randint(9,22)
    drawteams[x]=dclteams.get(x)
    print(drawteams[x])
while(len(drawteams)<28):
    x=rn.randint(23,60)
    drawteams[x]=dclteams.get(x)
    print(drawteams[x])
while(len(drawteams)<32):
    x=rn.randint(61,74)
    drawteams[x]=dclteams.get(x)
    print(drawteams[x])


t=sorted(drawteams.keys())
#print(t)
##print(drawteams[t[0]])

pot=[[0 for i in range(8)] for k in range(4)]
k=0
for i in range(4):
    for j in range(8):
        pot[i][j]=drawteams[t[k]]
        k+=1
print('\n\n\t\t\t\tWelcome to the Champions League Group Stage Draw\n\n')
print('Pot 1\t\t\t\tPot 2\t\t\t\tPot 3\t\t\t\tPot 4')
for j in range(8):
    print('\n')
    for i in range(4):
        print('{0:20s}'.format(pot[i][j][0]),'\t\t',end='')
print('\n\n\n')

for i in range(8):
    y='Group '+str(i+1)
    print('{0:20s}'.format(y),end='')
print('\n')
k=0
groups=[[0 for i in range(4)] for k in range(8)]
for i in range(4):
    balls=[i for i in range(8)]
    for j in range(8):
        k=rn.choice(balls)
        balls.remove(k)
        groups[j][i]=pot[i][k]
        print('{0:20s}'.format(groups[j][i][0]),end='')
        
        #os.system('pause')
    print(' ')  


















