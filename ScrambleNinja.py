import os; import re
from termcolor import colored
import colorama

byteList = []

colorama.init()

BANNER1 = colored('''
      ██████  ▄████▄   ██▀███   ▄▄▄       ███▄ ▄███▓ ▄▄▄▄    ██▓    ▓█████  ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
    ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒▓█████▄ ▓██▒    ▓█   ▀  ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
    ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░▒██▒ ▄██▒██░    ▒███   ▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
      ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ ▒██░█▀  ▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
    ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒░▓█  ▀█▓░██████▒░▒████▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
    ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
    ░  ░  ░  ░          ░░   ░   ░   ▒   ░      ░    ░    ░   ░ ░      ░      ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
          ░  ░ ░         ░           ░  ░       ░    ░          ░  ░   ░  ░         ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                                ScrambleNinja: The File Scrambler & Unscrambler''', 'red')
BANNER3 = colored('''                                -----------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3)


def operate():
    with open(filePath, "rb") as inputFile:
        for line in inputFile:
            byteList.append(line)

    if (operation == "1"):
            byteList.insert(-1, b'\r\n')

    length = len(byteList)
    half = length // 2

    with open(output, "wb") as outputFile:
        for element in byteList[half::-1]:
            outputFile.write(element)
        for element in byteList[:half:-1]:
            outputFile.write(element)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


def outputFileName():
        try:
            outputMatch = re.search(r"(.+)[$\.].+", filePath)
            output = str(outputMatch[1])
            extensionMatch = re.search(r".+[$\.](.+)", filePath)
            extension = str(extensionMatch[1])
        except:
            output = filePath
            extension = ""

        if (operation == "1"):
            output += " [Scrambled]." + extension
        elif (operation == "2"):
            output += " [Unscrambled]." + extension
        return(output)


############### Main ###############

if __name__ == "__main__":

    printBanner()

    try:

        while (True):
            print("Operations:-")
            print("1. Scramble a file\n2. Unscramble a file")
            operation = input("\nSelect operation number: ")
            if (operation in ["1", "2"]):
                while (True):
                    filePath = input("\nEnter file path: ")
                    if (os.path.isfile(filePath) is True):
                        break
                    else:
                        clrscr()
                        print("\nEither file does not exist or invalid path entered. Try again.")
                        continue
                clrscr()
                output = outputFileName()
                print("\nWorking...", end='')
                operate()
                break
            else:
                clrscr()
                print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
                continue
        clrscr()
        print("\n\nThe task completed successfully.")
        print("Press Enter to exit.")
        input()
    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
