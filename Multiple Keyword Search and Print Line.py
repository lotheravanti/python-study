import sys, re, os


def keysearch(keyword):
    hot = open("input.txt", "r")
    list = []
    #keyword = "(.*)(H|h)otnews(.*)"
    
    for num, line in enumerate(hot, 1):
        if re.match("(.*)"+keyword+"(.*)", line.lower()):
            list.append(num)

    print "Keyword ",keyword," found at following lines", list
    return keyword


keywords = ["Hotnews","are","invitat","vreme","ponta"]
for keyword in keywords:
    print keyword
    keysearch (keyword)