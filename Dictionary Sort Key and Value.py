import sys, re, os

dict = {"Victor":40, "Ion":45, "Ilie":50, "Vasile":34, "Marian":60, "Cristache":32, "Ionel":28}

for key in sorted(dict.iterkeys()):
    print "%s: %s" % (key, dict[key])
    
for key, value in sorted(dict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)