import sys

def readFile(fname):
    f = open(fname, "r")

    format_type = f.readline()
    ignore = f.readline()
    dim = f.readline()
    dlst = dim.split(" ")
    w = int(dlst[0])
    h = int(dlst[1])
    colour = f.readline()    
    lines = []
    for i in range(h):
        lines.append(f.readline().rstrip().split(" "))
    parse = 0
    pixels = lines[0]
    string_Output = ''
    while parse < len(lines):
        lines[parse].reverse()
        parse = parse + 1

    parse = 0
    pixel_size = 0
    while parse < len(pixels):
        if pixels[parse] != '':
            pixel_size = pixel_size + 1
        parse = parse + 1
     
    count_pixel = 0 
    parse = 0
    shift = 0
    dimension = 0
    parse_pixels = 0 
    pixels = lines[shift]
    while True:
        if pixels[parse_pixels] != '':
            string_Output = string_Output + pixels[parse_pixels]
            parse_pixels = parse_pixels + 1
            count_pixel = count_pixel + 1
            parse = parse + 1
                    
        if pixels[parse_pixels] == '' and parse < 3:
            string_Output = string_Output + ' '
            parse_pixels = parse_pixels + 1
                
        if count_pixel == pixel_size:
            dimension = dimension + 1
            count_pixel = 0
            string_Output = string_Output + '\n'
            shift = 0
            pixels = lines[shift]
            parse = 0
            parse_pixels = parse_pixels + 3
        
        if dimension == h: 
            break
                    
        if parse == 3: 
            shift = shift + 1
            parse = 0
            pixels = lines[shift]
            if dimension == 0:
                parse_pixels = 0
            else: 
                parse_pixels = parse_pixels - 5
            add_Padding = 0
            while add_Padding < 3:
                string_Output = string_Output + ' '
                add_Padding = add_Padding + 1

    Store = open('Rotate90L.ppm','w')
    Store.write(format_type)
    Store.write('#Image rotated 90 degrees to the left \n')
    Store.write(str(int(w)) + ' ' + str(int(h)) + '\n')
    Store.write(colour)
    Store.write(string_Output)
    Store.close()
    return format_type, w, h, colour, lines
    

def showFile (t, w, h, colours, dta):
    print ('This self developed algorithm only works for even dimension and rotate ppm image 90 degrees left')
    print ("This file is of type: " + t)
    print ("Its dimensions are: " + str(w) + ", " + str(h))
    print ()


def main():
    
    if len(sys.argv) == 2:
        stuff = readFile(sys.argv[1])
        showFile (stuff[0], stuff[1], stuff[2], stuff[3], stuff[4])
    else:
        print("Usage: pbmview filename")


if __name__ == "__main__":
    main()