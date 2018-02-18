import sys, re, os

hot = open("input.txt", "r")
list = []
keyword = "(.*)(H|h)otnews(.*)"

for num, line in enumerate(hot, 1):
    if re.match(keyword, line):
        list.append(num)

print "Keyword found at following lines", list