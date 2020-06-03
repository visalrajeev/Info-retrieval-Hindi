from nltk.tokenize import word_tokenize 
import os

doc_list = []

invert = dict()
i = 1


basepath = './docs'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        f = open(os.path.join(basepath, entry), 'r', encoding='utf8') 
        doc_list.append(entry)
        
        #tokenazation
        data = f.read()
        token = word_tokenize(data)

        #Filtering of Non-hindi words
        def hindiver(l):
            for j in range(len(l)):
                c=ord(l[j])

                if((2304<=c and c<=2416)):
                    continue
                else:
                    return 0
            return 1

        for j in token:
            word = j
            if hindiver(word) == 0:
                token.remove(word)
            else:
                pass

        #Removing punctuations
        punch = ['.', ',', '?', ';', '।', ':', '(', ')', '{', '}', "'", '"', '!', '@', '#', '$', '%', '^', '/', '*', '&']

        for x in token:
            for j in punch:
                if x == j:
                    token.remove(x)

        n = []
        for x in token:
            if '।' == x[-1]:
                x = x[:len(x)-1]

            n.append(x)

        token = n
        
        #Removing the stopword
        file = open('stopwords.txt', "r", encoding='utf8')
        strings = file.read()

        for w in token:

            search_word = w
            if(search_word in strings):
                token.remove(search_word)
            else:
                pass
            
        #Stemming of the Token
        suffixes = {
        1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
        2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
        3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
        4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
        5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
        }
        def hi_stem(word):
            for L in 5, 4, 3, 2, 1:
                if len(word) > L + 1:
                    for suf in suffixes[L]:
                        if word.endswith(suf):
                            return word[:-L]
            return word

        stemmed = []

        for j in range(0,len(token)):
            stemmed.append(hi_stem(token[j]))               
        
        #Generating Inverted Index
        for words in stemmed:
            words = words.lower()

            # Check if the word is already in dictionary 
            if words in invert:
                #check = invert[words] +','+ str(i)
                check = invert[words]
                check = check[-1]
                if str(i) == check:
                    pass
                else:
                    invert[words] = invert[words] +','+ str(i)
            else: 
                # Add the word to dictionary with count 1 
                    invert[words] = str(i)
                    
        i = i + 1

def get_invert():
    return invert

def query(key):

    output = []

    if key in invert.keys():
        a = invert[key]
        a = a.split(',')
        a = list(dict.fromkeys(a))
        
        for x in range(0,len(doc_list)):
            for y in a:
                if (int(y)-1) == x:
                    output.append(doc_list[x])


        return output
    
    else:
        return 'No Document'


def queryAND(a,b):

    output = []

    if a in invert.keys():
        a1 = invert[a]
    
    else:
        return 0
    
    if b in invert.keys():
        b1 = invert[b]
    
    else:
        return 0
    
    c = []
    
    a1 = a1.split(',')
    b1 = b1.split(',')
    
    for i in range(0,len(a1)):
        for j in range(0,len(b1)):
            if(a1[i]==b1[j]):
                c.append(b1[j])
            else:
                pass
    
    if len(c) is 0:
        return 'No Document'
    
    else:
        c = list(dict.fromkeys(c))

        for x in range(0, len(doc_list)):
            for y in c:
                if (int(y)-1) == x:
                    output.append(doc_list[x])

        return output
    

def queryOR(a,b):

    output = []

    if (a in invert.keys() and b in invert.keys()):
        a1 = invert[a]
        b1 = invert[b]
    
        a1 = a1.split(',')
        b1 = b1.split(',')
        
        c = []
        
        if len(a1) > len(b1):
            c = a1

            for i in range(0,len(c)):
                for j in range(0,len(b1)):
                    if(c[j]!=b1[j]):
                        c.append(b1[j])
                    else:
                        pass

        else:
            c = b1

            for i in range(0,len(c)):
                for j in range(0,len(a1)):
                    if(c[j]!=a1[j]):
                        c.append(a1[j])
                    else:
                        pass
                    
    elif a in invert.keys():
        a1 = invert[a]
        a1 = a1.split(',')
        c = a1
        
    elif b in invert.keys():
        b1 = invert[b]
        b1 = b1.split(',')
        c = b1
              
    else:
        return 'No Document'
    
    c = list(dict.fromkeys(c))
    
    for x in range(0, len(doc_list)):
        for y in c:
            if (int(y)-1) == x:
                output.append(doc_list[x])

    return output

def Not(a):

    output = []

    if a in invert.keys():

        a1 = invert[a]

        all_item = []
        for x,y in invert.items():
            all_item.append(y)
            
        all_item = list(dict.fromkeys(all_item))
        big = (max(all_item, key = len))

        big = big.split(',')

        c = []

        c = list(set(big) - set(a1))

        if len(c)==0:
            return 'No Document'

    else:
        a1 = ''
        c = []
        for x in invert:
            a1 += invert[x]

        c = a1.split(',')
        c = list(dict.fromkeys(c))

    for x in range(0, len(doc_list)):
        for y in c:
            if (int(y)-1) == x:
                output.append(doc_list[x])

    return output