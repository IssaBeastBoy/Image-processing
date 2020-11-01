import sys

def readFile(fname, conversion_Type):
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
    stop = 0
    
    while stop < len(lines):       
        data = lines[stop]
        parse_Data = 0
        pixel_count = 0  
        channel = 0.0 
        indexes = [] 
        while parse_Data < len(data):            
            if conversion_Type == 0:
                if data[parse_Data] != '' and pixel_count >= 1:
                    data[parse_Data] = channel
                    pixel_count = pixel_count + 1

                if data[parse_Data] != '' and pixel_count == 0:
                    channel = data[parse_Data]
                    pixel_count = pixel_count + 1  
                                  
                
                if pixel_count == 3:
                    pixel_count = 0

            if conversion_Type == 1:
                if data[parse_Data] != '' and pixel_count >= 1:
                    channel = channel + int(data[parse_Data])
                    pixel_count = pixel_count + 1
                    indexes.append(parse_Data)

                if data[parse_Data] != '' and pixel_count == 0:
                    channel = int(data[parse_Data])
                    pixel_count = pixel_count + 1 
                    indexes.append(parse_Data)
                if pixel_count == 3:
                    pixel_count = 0
                    average = channel/3
                    write_back = 0
                    while write_back < len(indexes):
                        data[indexes[write_back]] = average
                        write_back = write_back + 1
                    indexes = []
            
            if conversion_Type == 2:
                if data[parse_Data] != '' and pixel_count >= 1:
                    channel = channel + int(data[parse_Data])
                    pixel_count = pixel_count + 1
                    indexes.append(parse_Data)

                if data[parse_Data] != '' and pixel_count == 0:
                    channel = int(data[parse_Data])
                    pixel_count = pixel_count + 1 
                    indexes.append(parse_Data)

                if pixel_count == 3:
                    pixel_count = 0
                    weight = 0.0
                    write_back = 0
                    while write_back < len(indexes):
                        if channel != 0:
                            weight = weight + (int(data[indexes[write_back]]) * ( ( (int(data[indexes[write_back]]) * 100) / channel)/100) )
                        else:
                            weight = weight + 0
                        write_back = write_back + 1
                    write_back = 0
                    while write_back < len(indexes):
                        data[indexes[write_back]] = int(weight)
                        write_back = write_back + 1
                    indexes = []
            
            parse_Data = parse_Data + 1
        lines[stop] = data
        stop = stop + 1

    if conversion_Type == 0:
        Store = open('Single_GrayScale.ppm','w')
    if conversion_Type == 1:
        Store = open('Average_GrayScale.ppm','w')
    if conversion_Type == 2:
        Store = open('Weighted_GrayScale.ppm','w')
    Store.write(format_type)
    Store.write(str(w) + ' ' + str(h) + '\n')
    Store.write(colour)
    stop = 0
    while stop < len(lines):
        data = lines[stop]
        pixels = data[0]
        del data[0]
        parse = 0
        while parse < len(data):
            pixel = data[parse]
            if pixel == '':
                pixel= '  '
            else:
                pixel =  str(int(pixel))
            pixels =  pixels + pixel
            parse = parse + 1
        Store.write(pixels + '\n')
        stop = stop + 1
    Store.close()
    return format_type, w, h, colour, lines
    

def showFile (t, w, h, colours, dta):
    print ("This file is of type: " + t)
    print ("Its dimensions are: " + str(w) + ", " + str(h))
    print ()


def main():
    grayscale_type = input("Select grayscale method \n Single Channel -> 0 \n Average -> 1 \n Weighted -> 2 \n -> ")
    
    if len(sys.argv) == 2:
        stuff = readFile(sys.argv[1], int(grayscale_type))
        showFile (stuff[0], stuff[1], stuff[2], stuff[3], stuff[4])
    else:
        print("Usage: pbmview filename")


if __name__ == "__main__":
    main()