import sys, re, os


def keysearch(keyword):
    hot = open("input.txt", "r")
    list = []
    #keyword = "(.*)(H|h)otnews(.*)"
    keyword = "Hotnews"

    for num, line in enumerate(hot, 1):
        if re.match("(.*)"+keyword+"(.*)", line):
            list.append(num)

    print "Keyword ",keyword," found at following lines", list
    return keyword


keysearch ("hotnews")
