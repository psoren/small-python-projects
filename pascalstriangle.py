def nextRow(numList):
    newList = [1]
    for i in range(len(numList)):
        if len(numList)>i+1:
            newList.append(numList[i] + numList[i+1])
    newList.append(1)
    return newList

height = int(input("Please enter the height of the Pascal's triangle you wish to display: "))

triangleList = [[1], [1,1]]

for i in range(1, height):
   triangleList.append(nextRow(triangleList[i]))

for row in triangleList:    
    print(str(row).strip("[]").replace(',','').center(height*8))
