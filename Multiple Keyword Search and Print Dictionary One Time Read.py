import re

def has_word(keyword, line):
    if re.match("(.*)"+keyword.lower()+"(.*)", line.lower()):
        return True
    return False

#init
keywords = ["are","Hotnews","invitat","vreme","ponta"]
dict ={}
for key in keywords:
    dict[key] = []

#do stuff
hot = open("input.txt", "r")
for num, line in enumerate(hot, 1):
    for keyword in keywords:
        if has_word(keyword, line):
            dict[keyword].append(num)

#print
for key in dict:
    print "Keyword ",key," found at following lines", dict[key]