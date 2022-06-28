# removes first and last elements from list
# chop returns 'None'; middle returns new list

def chop(listToChop):
    print(listToChop[1:-1])
    return

def middle(listToMiddle):
    return listToMiddle[1:-1]

startingList = [1, 2, 3, 4, 5]
startingList = chop(startingList)
print(startingList)

startingList = [1, 2, 3, 4, 5]
bobarino = middle(startingList)
print(bobarino)
