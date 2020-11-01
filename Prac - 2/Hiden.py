import sys

word = input('Enter words you want to hide - ')
if len(word) > 0:
    noSpace = word.replace(' ', '')
    characters = list(noSpace)
    toAscii = 0
    image = "P2 \n" + str(len(characters)) + ' 3 \n255 \n'
    pixels_count = 0
    while pixels_count < 3:
        while toAscii < len(characters):
            if pixels_count == 0:
                if characters[toAscii] == 'a' or characters[toAscii] == 'b' or characters[toAscii] == 'c' or ( ord(characters[toAscii]) >= 65 and ord(characters[toAscii]) <= 90 ) :
                    image = image + '0' + str(ord(characters[toAscii])) + " "
                    toAscii = toAscii + 1
                else:
                    image = image + str(ord(characters[toAscii])) + " "
                    toAscii = toAscii + 1
            else:
                image = image + '000 '
                toAscii = toAscii + 1
        image = image + '\n'
        pixels_count= pixels_count + 1   
        toAscii = 0 

    Store = open('Hidden.ppm','w')
    Store.write(image)
    Store.close()        

else:
    print("\n No word input")