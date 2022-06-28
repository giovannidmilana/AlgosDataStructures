#dict1 = dict()
#dict2 = dict()
words = ['the', 'cat', 'ran']

# create empty hashmap from list of words
def make_hash_map(words):
    dict1 = dict()
    dict2 = dict()
    for j in range(len(words)):
        dict2[words[j]] = dict1
        dict1 = dict()
        for i in range(len(words)):
            dict1[words[i]] = 0.0
    return dict2     

###





# load text to string inside list
def load_file(fl_name):
    with open(fl_name) as f:
        lines = f.readlines()
    #print(lines)
    return lines[0]
#




# function to clean string data
def clean_corpus(corpus):
    corpus = corpus.lower()
    corpus = corpus.encode('ascii', 'ignore').decode()
    corpus = corpus.split(' ')
    
    #print(corpus)
    return corpus
    
#clean_corpus(lines)
#
corpus = load_file('marc_text.txt')
print('corpus')
print(corpus)
words = clean_corpus(corpus)
print('words')
print(words)
hashMp = make_hash_map(words)
print('hash map')
print(hashMp)



for i in range(len(words)-1):
    #print(words[i])
    #print(words[i+1])
    hashMp[words[i]][words[i+1]] = hashMp[words[i]][words[i+1]] + 1

for i in range(len(words)-1):
    #print(words[i])
    #print(words[i+1])
    hashMp[words[i]][words[i+1]] = hashMp[words[i]][words[i+1]] / len(words) *100 

print('hash map')
print(hashMp)

