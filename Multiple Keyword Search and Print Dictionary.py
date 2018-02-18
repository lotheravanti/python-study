import sys, re, os
dict ={}

def keysearch(keyword):
    hot = open("input.txt", "r")
    list = []
    #keyword = "(.*)(H|h)otnews(.*)"
    
    for num, line in enumerate(hot, 1):
        if re.match("(.*)"+keyword.lower()+"(.*)", line.lower()):
            list.append(num)

    return list



keywords = ["Hotnews","are","invitat","vreme","ponta"]
for keyword in keywords:
    dict[keyword]= keysearch (keyword)

for key in dict:
    print "Keyword ",key," found at following lines", dict[key]