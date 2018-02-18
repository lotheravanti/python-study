def keysearch(str, keyword):
    split = str.split()
    count = split.count(keyword)
    return count

with open("Test.txt", "r") as myfile:
    data=myfile.read()

cnt = keysearch(data,"man")
print "Keyword is present ", cnt, " times"
