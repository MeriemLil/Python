import os

def listDirectory():
    directory = os.getcwd()
    print(directory)
    print("\nFiles in this directory: \n")
    for file in os.listdir(directory):
        print(file)

def sortDirectory():
    directory = os.getcwd()
    files = sorted(os.listdir(directory))
    for file in files:
        print(file)


def goIntoDirectory():
    directory = os.getcwd()
    newDirectory = input("Enter the name of the new directory: ")
    os.chdir(newDirectory)
    print("The current directory has changed to ")
    print(os.getcwd())
    for file in os.listdir(os.getcwd()):
        print(file)

def goIntofile():
    file = input("Enter name of file you want to access: ")
    f = open(file, 'r')
    print(f.read())
    f.close()

print("***Welcome to file handling program***\n")
print("Enter: \n")
print("1 to get the name of the current working directory and list its files\n")
print("2 to get the files of the current working directory sorted by creation time\n")
print("3 to change the current working directory to another one and list its files\n")
print("4 to open and read the content of a given file in the current directory\n")

choice = input("Enter choice : ")

if (choice == '1'):
    listDirectory()
elif (choice == '2'):
    sortDirectory()
elif (choice == '3'):
    goIntoDirectory()
elif (choice == '4'):
    goIntofile()
else:
    print("No such entry!")


