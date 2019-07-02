
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

def MorseToEng():
    file = input("Enter name of file: ")
    f = open(file, 'r')
    n  = f.read()
    for x in n:
        for y in MORSE_CODE:
            if (x == MORSE_CODE[y]):
                print(y)


    f.close()


def EngToMorse():
    file = input("Enter name of file: ")
    f = open(file, 'r')
    m = f.read()
    for x in m:
        for y in MORSE_CODE:
            if (x == y):
                print(MORSE_CODE[y])
    f.close()


EngToMorse()
