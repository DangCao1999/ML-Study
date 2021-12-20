f = open("train-features-700.txt", "rt")
data100Nword = []
data_filter = {}
for word in f.readlines():
    word1 = word.split(" ")
    if(data_filter.get((word1[0])) == None):
        data_filter[word1[0]] = [word1[1]]
    else:
        data_filter[word1[0]].append(word1[1])

f.close()  
for keyEmail in data_filter:
    find = True
    for value in data_filter[keyEmail]:
        if(int(value) > 1000):
            find = False
            break
    if(find):
        data100Nword.append(keyEmail)
        


print(data100Nword)