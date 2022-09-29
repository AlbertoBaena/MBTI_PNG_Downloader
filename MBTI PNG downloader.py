# Yo wassup
import requests

letters = [['e','i'],['n','s'],['f','t'],['j','p']]
persType = 0

while(persType < 16):
    # Start with empty string and iterator for getting the 4 letters
    fourLetters = ""; i = 0
    
    # Getting binary number of the current iterator:
    # (16 types ~ 16 numbers)
    b = bin(persType)
    # b starts with "0b", so these chars will be removen
    b = b.replace('0', '', 1)
    b = b.replace('b', '', 1)
    # Adding zeroes so all numbers have 4 digits
    le = len(b)
    if(le < 4):
        while (le < 4):
            b = "0" + b
            le += 1

    # Getting the four letters from the binary number
    while(i < 4):
        j = int(b[(le-1) - i]) # We get the correspondent letter from the current digit binary number
        fourLetters = fourLetters[:i] + letters[i][j] + fourLetters[i+1:]
        i += 1
        
    # Getting PNGs yay
    url = "https://www.16personalities.com/images/types/" + fourLetters + ".png"
    r = requests.get(url, allow_redirects = True)
    open(fourLetters.upper() + ".png", 'wb').write(r.content)

    # You lost the game >:) (if u don't get it, search "The Game")
    persType += 1