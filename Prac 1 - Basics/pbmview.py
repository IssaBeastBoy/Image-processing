import sys

def readFile(fname):
    f = open(fname, "r")
    type = f.readline()
    dim = f.readline()
    dlst = dim.split(" ")
    w = int(dlst[0])
    h = int(dlst[1])
    lines = []
    for i in range(h):
        lines.append(f.readline().rstrip().split(" "))
    return type, w, h, lines
    
def greyScaling (image):
    imageLines = image[3]
    red, blue, green = 


def showFile (t, w, h, dta):
    print ("This file is of type: " + t)
    print ("Its dimensions are: " + str(w) + ", " + str(h))
    print ("And it looks like this:")
    print ()
    for i in range(h):
        for j in range(w):
            if dta[i][j] == "1":
                print (chr(9608), end="")  
            else:
                print(" ", end = "")
        print()
    print()


def main():
    if len(sys.argv) == 2:
        stuff = readFile(sys.argv[1])
        showFile (stuff[0], stuff[1], stuff[2], stuff[3])
    else:
        print("Usage: pbmview filename")


if __name__ == "__main__":
    main()