import sys


char_freqs = {}
count=0
types=0
total_token=0

fname = sys.argv[1]

with open(fname, mode='rt',encoding='utf8') as infile:
    for line in infile:
        if(line.isspace()==True):
            continue
        word = line.lower()
        char_freqs[word] = char_freqs.get(word, 0) + 1

for word,freq in sorted(char_freqs.items(), key=lambda x : x[1], reverse=True):
    if(freq==1):
        count=count+1
    if(freq>1):
        types=types+1
    total_token+=freq
    print("{freq} : {word}".format(freq=freq,word=str(word)))
print("Total Tokens: {g}".format(g=total_token))
types=types+count
print("Types: {g}".format(g=types))
print("Hapax Legomena: {f}".format(f=count))

