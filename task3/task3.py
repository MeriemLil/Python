
MORSE_CODE = { 'A':'.*', 'B':'*...',
               'C':'*.*.', 'D':'*..', 'E':'.',
               'F':'..*.', 'G':'**.', 'H':'....',
               'I':'..', 'J':'.***', 'K':'*.*',
               'L':'.*..', 'M':'**', 'N':'*.',
               'O':'***', 'P':'.**.', 'Q':'**.*',
               'R':'.*.', 'S':'...', 'T':'*',
               'U':'..*', 'V':'...*', 'W':'.**',
               'X':'*..*', 'Y':'*.**', 'Z':'**..',
               '1':'.****', '2':'..***', '3':'...**',
               '4':'....*', '5':'.....', '6':'*....',
               '7':'**...', '8':'***..', '9':'****.',
               '0':'*****', ', ':'**..**', '.':'.*.*.*',
               '?':'..**..', '/':'*..*.', '*':'*....*',
               '(':'*.**.', ')':'*.**.*'}

# conventions:
# - one space to separate two letters
# - three spaces to separate two words
# - the last word must terminate by a space, at least
def MorseToEng():
    file = 'myPWD.txt' #input("Enter name of file: ")
    f = open(file, 'r')
    m = f.read()

    tmp = ""
    c = 0  # to count how many spaces
    for x in m:
        if (x != " "):  # building a letter
            tmp += x
            c = 0
        else:   # a letter terminates by one space
            c += 1
            if (c == 1):
                for y in MORSE_CODE:
                    if (tmp == MORSE_CODE[y]):
                         print(y)
                tmp = ""
            elif (c == 3):
                print(" ")

    f.close()


def EngToMorse():
    file = 'myPWD.txt' #input("Enter name of file: ")
    f = open(file, 'r')
    m = f.read()
    for x in m:
        if (x != " "): # an English letter
            for y in MORSE_CODE:
                if (x == y):
                    print(MORSE_CODE[y] + " ") # a space between two letters
        else:
            print("   ") # a space, so print 3 spaces to separate between words

    f.close()

#EngToMorse()
MorseToEng()

