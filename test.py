import glob, os

path_data = 'data/Coin'
for pathAndFilename in glob.iglob(path_data+"/*.txt"):
    print(pathAndFilename)
    f = open(pathAndFilename, 'r+')
    
    contents = f.read()
    print(contents)
    
    new = list(contents)
    if(pathAndFilename == "data/Coin/"+"coin1"+"*.txt"):
        if (new[0] != '0'):
            break
    if(pathAndFilename == "data/Coin/"+"coin5"+"*.txt"):
        if (new[0] != '1'):
            break
    if(pathAndFilename == "data/Coin/"+"coin10"+"*.txt"):
        if (new[0] != '2'):
            break
    if(pathAndFilename == "data/Coin/"+"coin50"+"*.txt"):
        if (new[0] != '3'):
            break
    if(pathAndFilename == "data/Coin/"+"coin100"+"*.txt"):
        if (new[0] != '4'):
            break
    if(pathAndFilename == "data/Coin/"+"coin500"+"*.txt"):
        if (new[0] != '5'):
            break
           
    #new[0] = "5"
    contents = "".join(new)
    print(contents)
    f = open(pathAndFilename, 'w+')
    f.write(contents)
    f.close()
    