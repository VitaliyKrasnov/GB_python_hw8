print("Содержимое файла 'file.txt'")
with open("file.txt", "r") as file:
    for line in enumerate(file):
        print("№"+str(line[0]+1), line[1], end='')
strNum = int(input("Введите номер строки для копирования в файл 'file_copy.txt':"))
requiredString = ""
with open("file.txt", "r") as file:
    for line in enumerate(file):
        if line[0]+1 == strNum:
            requiredString = line[1]
            break
with open("file_copy.txt", "a") as fileCopy:
        fileCopy.write(requiredString)
        print("Скопирована строка №", strNum)
print("Содержимое файла 'file_copy.txt':")
with open("file_copy.txt", "r") as fileCopy:
    for line in fileCopy:
        print(line, end='')


