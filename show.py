import sys
from words import makeWords

# Goal:
# show the contents of a given file.


def printLine(line):
    print(line, end='')


def printWords(line):
    words = makeWords(line)
    for word in words:
        print(word)


if __name__ == "__main__":
    # 1. read the file name from argument #1
    fileName = sys.argv[1]
    if len(sys.argv) < 3:
        words = False
    else:
        words = bool(sys.argv[2])

    # 2. Open the file and assign to a variable f
    f = open(fileName, 'r')

    # 3. while true, read one line from the file f
    while True:
        line = f.readline()

        # 4. if that line is not empty print it
        if line:
            if words:
                printWords(line)
            else:
                printLine(line)
        else:  # 5. else stop
            break

    # 6. close the file
    f.close()
