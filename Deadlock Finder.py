'''
p = [[1,2],[3,2],[0,6],[5,3],[0,4],[0,5,3]]
r = [[1],[1],[2],[0],[3],[5],[5],[6]]

p[0] ==> r[2] ==> p[1] ==> r[6] ==> p[2]#==>r[0]==>p[0](dead lock)
                                        #
                                        #==>r[8]==>p[4]==>p[2](not dead lock)

'''
p = []
r = []

n =int(input("enter the number of processes: "))
for i in range(n):

    try:
        x = list(map(int,input("P"+str(i+1)+" wait for: ").split(' ')))
    except ValueError:
        x = []

    for j in range(len(x)):
        x[j] = x[j]-1

    p.append(x)

check = [0]*n

n = int(input("enter the number of Resources: "))
for i in range(n):

    try:
        x = list(map(int,input("R"+str(i+1)+" Own: ").split(' ')))
    except ValueError:
        x=[]

    for j in range(len(x)):
        x[j] = x[j]-1

    r.append(x)

print(p)
print(r)

dl = []

def deadlock(curr,Type): #type (check if it process or resource and curr (for current process)
    if Type:    #type = 1 then process else R
        for i in p[curr]:
            if curr == x and check[curr]:
                for j in dl:
                        if j==dl[0]: print(dl[-1]+" ==> ",end='')
                        if j==dl[-1]:   print(j)
                        else:   print(j +" ==> ",end='')
                return
            elif check[curr]:
                return

            check[curr]=1
            dl.append('R' + str(i+1))
            deadlock(i,0)
            dl.pop()
            check[curr]=0

    else:
        for i in r[curr]:
            dl.append('P' + str(i+1))
            deadlock(i,1)
            dl.pop()


for i in range(5):
    x=i
    deadlock(i,1)
