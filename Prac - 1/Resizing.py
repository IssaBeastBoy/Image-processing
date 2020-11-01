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
    resizing_Small = []
    Small = 'Make smaller dimension options: \n '
    large = 'Make larger dimension options: \n '
    if (w > 3 and h > 3):
        small_W = w
        small_H = h
        count = 1
        while True:
            small_W = small_W/2
            small_H = small_H/2
            if small_W > 1 and small_H > 1:
                resizing_Small.append(small_W)
                resizing_Small.append(small_H)
                Small = Small + 'dimensions ' + str(int(small_W)) + ', ' + str(int(small_H)) + ' -> ' + str(count) + '\n '
            else:
                break
            count = count + 1
    else:
        return "Image dimensions are too small to resize."   
    resizing_Large = [] 
    count = 0
    stop = int(len(resizing_Small)/2) + 1
    large_W = w
    large_H = h
    while count < len(resizing_Small):
        large_W = large_W + w
        large_H = large_H + h
        resizing_Large.append(large_W)
        resizing_Large.append(large_H)
        large = large + 'dimensions ' + str(large_W) + ', ' + str(large_H) + ' -> ' + str(stop) + '\n '
        count = count + 2
        stop = stop + 1

    output = 'Select dimension: \n ' + Small + large + '\n -> '
    resize_Type = input(output)

    if int(resize_Type) > stop:
        return "Wrong dimension"

    if int(resize_Type) <= int(len(resizing_Small)/2):
        Width = resizing_Small[int(resize_Type)]
        Height = resizing_Small[int(resize_Type)]
        parse = 0
        count = 0
        size = 0
        while True:
            start = 0
            stop = 0
            pixels = lines[parse]
            count =  count
            pixel_count = 7
            while True:
                if pixels[count] != '':
                    start = 1
                        
                if start == 1:
                    if pixels[count] != '':
                        pixel_count = pixel_count - 1
                    if pixel_count == 0:
                        break
                    if pixel_count < 4:
                        del lines[parse][count]
                        count = count - 1
                    del lines[parse + 1][1]
                if len(lines[parse + 1]) == 1 :
                    del lines[parse + 1]
                    break
                count = count + 1
            size = size + 1
            if size == 2:
                parse = parse + 1
                count = 0
            if size == 4:
                break            
        Store = open('Smaller.ppm','w')
            
    if int(resize_Type) > int(len(resizing_Small)/2):
        Store = open('Large.ppm','w')
        Width = large_W
        Height =large_W
        parse = 0
        size = 0
        new_Size = []
        while parse < len(lines):
            start = 0
            stop = 1
            count = 0
            pixels = lines[parse]
            count =  count
            pixel_count = 7
            store_pixels = []
            extend = []
            while True:
                if stop == 1:
                    pixel_Adder = ['', '', '']
                    
                if stop == 2 and pixels[count] == '':
                    pixel_Adder.append(pixels[count])
                    
                if pixels[count] != '':
                    pixel_Adder.append(pixels[count])
                    if stop == 1:
                        stop = 2
                    start =  start + 1
                
                extend.append(pixels[count]) 
                store_pixels.append(pixels[count])
                
                if start == 3:
                    start = 0
                    
                    while start < len(pixel_Adder):
                        store_pixels.append(pixel_Adder[start])
                        extend.append(pixel_Adder[start]) 
                        start = start + 1
                    start = 0
                    stop = 1
                count = count + 1    
                if count == len(pixels):
                    new_Size.append(store_pixels)
                    new_Size.append(extend)
                    break
            parse = parse + 1
        lines = new_Size

    Store.write(format_type)
    Store.write(str(int(Width)) + ' ' + str(int(Height)) + '\n')
    Store.write(colour)
    parse_list = 0
    while parse_list < len(lines):
        start = 0
        parse = 0
        pixels = lines[parse_list]
        save = ''
        while True:
            if pixels[parse] != '':
                start = start + 1
                save = save + pixels[parse]
            else:
                save = save + " "
            if start == Width * 3:
                save = save + '\n'
                break
            parse = parse + 1
        Store.write(save)
        parse_list = parse_list + 1
    Store.close()
    return format_type, w, h, colour, lines
    

def showFile (t, w, h, colours, dta):
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