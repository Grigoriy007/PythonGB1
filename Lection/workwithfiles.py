
fileName = 'text.txt'

def writeFile(file_name):
    with open(file_name, 'a') as data:
        data.write("Sidorov, Petr, Ivanovich, +926474747477" + '\n')


def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result


def findUsers(userList):
    name = 'Ivan,'
    for user in userList:
        if user[1] == name:
            print(user[3])


def changeUsers(userList):

    with open("text.txt", "rt") as fin:
        data = fin.read()
        data = data.replace('Ivanov, Ivan, Ivanovich, +7125478541', 'Ivanov, Ivan, Ivanovich, +79261177330')

    with open("text.txt", "wt") as fin:
        fin.write(data)




# writeFile(fileName)
# print(type(readFile(fileName)))
# print(readFile(fileName))
# # findUsers(readFile(fileName))
changeUsers(fileName)
# print(readFile(fileName))



# fin = open("text.txt", "rt")
# data = fin.read()
# data = data.replace('Jon', 'Koko')
# fin.close()
# fin = open("text.txt", "wt")
# fin.write(data)
# fin.close()


# fin = open("text.txt", "rt")
# fout = open("out.txt", "wt")
# for line in fin:
#     fout.write(line.replace('Jon', 'Koko'))
# fin.close()
# fout.close()