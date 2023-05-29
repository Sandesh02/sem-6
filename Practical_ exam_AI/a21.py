from glob import glob


global g
def printboard(elements):
    for i in range(9):
        if i%3==0:
            print()
        if elements[i]==-1:
            print("_",end=' ')
        else:
            print(elements[i],end=' ')

def solvable(start):
    inv=0
    for i in range(9):
        if start[i]==1:
            continue
        for j in range(i+1,9):
            if start[i]==1:
                continue
            if start[i]>start[j]:
                inv+=1

    if inv%2==0:
        return True
    else:
        return False

def hueristic(start , goal):
    global g 
    h=0
    for i in range(9):
        for j in range(9):
            if start[i]==goal[j] and start[i]!=-1:
                h+=abs(j-i)//3 + abs(j-1)%3

    return h+g

def moveleft(start, position):
    start[position],start[position-1]=start[position-1],start[position]
def moveright(start, position):
    start[position],start[position+1]=start[position+1],start[position]
def moveup(start, position):
    start[position],start[position-3]=start[position-3],start[position]
def movedown(start, position):
    start[position],start[position+3]=start[position+3],start[position]

def movetile(start , goal):
    
        
