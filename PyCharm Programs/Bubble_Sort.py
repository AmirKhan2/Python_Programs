def sort(inputList):
    for i in range(len(userList) - 1, 0, -1):
        for j in range(i):
            if inputList[j] > inputList[j + 1]:
                temp = inputList[j]
                inputList[j] = inputList[j + 1]
                inputList[j + 1] = temp


userList = [42, 5234, 254, 342, 554, 89, 230]
sort(userList)
print(userList)
