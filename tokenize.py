import gzip, re, sys

def tokenize(l):

    s=re.findall(r"(\$\d+|[\w]*['][\w]+|\w+|\$[0-9]+\,[0-9]+\,*[0-9]+|[^a-zA-Z0-9-\s]+)",l)
    return s
##    s= "; |\$ |\*|\s"
##    print(re.split(s,l))
##    return re.split(s,l)s

# The first argument is the filename to work with
fname = sys.argv[1]
            
with gzip.open(fname, mode='rt',encoding='utf8') as infile:
    for line in infile:
            # Tokenize each sentence/line
        tokens = tokenize(line)
        for t in tokens:
            print(t)
        print()
 
