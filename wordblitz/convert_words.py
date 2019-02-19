import re

all_words = open("words.txt",'r').read().replace('\n'," ")

a = re.findall('[A-z]+',all_words)

a = [x.lower() for x in a]

a = list(set(a)) # removing duplicates

a = [i for i in a if len(i) > 1] #removing single character words


with open('new.txt', 'w') as f:
    for item in a:
        f.write("%s\n" % item)