
fileWrite = open("DataBt2-Tranfer.txt", "wt")
f = open("DataBt2.txt", "rt")
for word in f.readlines():
    word1 = word.split(" ")
    firstNumber = int(word1[0])
    if (firstNumber > 10):
        newWord =  firstNumber - 680
        fileWrite.write( str(newWord) + " " + word1[1] + " " + word1[2])
    else:
        fileWrite.write(word)
    #fileWrite.write(str(word).lower().rstrip()+"\n")
    #print(word)
fileWrite.close()
f.close()