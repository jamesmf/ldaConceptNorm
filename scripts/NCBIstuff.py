# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:41:39 2015

@author: frickjm
"""
import cPickle

#with open("../data/pickledTitles/OMIM_titles.pickle", 'rb') as f:
#    ots  = cPickle.load(f)
#ots2 = []
#for o in ots:
#    ots2.append(o[:12])

#wOMIM = []
#with open("../data/NCBI/NCBItrainset_corpus.txt",'rb') as f:
#    for x in f:
#        if x.find("OMIM:") > -1:
#            uid     = x.split("\t")[0]
#            wOMIM.append(uid)

#print len(wOMIM)            
#wOMIM   = list(set(wOMIM))
#print len(wOMIM)

mentionDict     = {}

with open("../data/NCBI/NCBItrainset_corpus.txt",'rb') as f:
    for x in f:
        sPipe   = x.split("|")
        sTab    = x.split("\t")

        #if we encounter a new title, update the text, new abstract added to title
        if len(sPipe) > 1:
            if (sPipe[1] == "t"):
                text    = sPipe[2]
                
            if (sPipe[1] == "a"):
                text    +=sPipe[2]
        
        if len(sTab) > 1:
            snip    = sTab[3].strip()
            codes   = sTab[-1].strip().replace(":",'').split("|")
            
            if len(codes[0].split("+")) > 1:
                codes = codes[0].split("+")
                
            for code in codes:
                    
                if not mentionDict.has_key(code):
                    mentionDict[code] = [text,snip]
                else:
                    if text not in mentionDict[code]:
                        mentionDict[code].append(text)
                    mentionDict[code].append(snip)
s=0
for k,v in mentionDict.iteritems():
    s += len(v)
    with open("../data/NCBI/trainingDocs/"+k,'wb') as f:
        f.write('\n'.join(v))
print "training set categories: ", len(mentionDict.keys())   
trainkeys   = mentionDict.keys()




mentionDict     = {}

with open("../data/NCBI/NCBItestset_corpus.txt",'rb') as f:
    for x in f:
        sPipe   = x.split("|")
        sTab    = x.split("\t")

        #if we encounter a new title, update the text, new abstract added to title
        if len(sPipe) > 1:
            if (sPipe[1] == "t"):
                text    = sPipe[2]
                
            if (sPipe[1] == "a"):
                text    +=sPipe[2]
        
        if len(sTab) > 1:
            snip    = sTab[3].strip()
            codes   = sTab[-1].strip().replace(":",'').split("|")
            
            if len(codes[0].split("+")) > 1:
                codes = codes[0].split("+")
                
            for code in codes:
                    
                if not mentionDict.has_key(code):
                    mentionDict[code] = [text,snip]
                else:
                    if text not in mentionDict[code]:
                        mentionDict[code].append(text)


for k,v in mentionDict.iteritems():
    s += len(v)
    with open("../data/NCBI/testDocs/"+k,'wb') as f:
        f.write('\n'.join(v))
print "test set categories: ", len(mentionDict.keys())   
testkeys    = mentionDict.keys()








mentionDict     = {}

with open("../data/NCBI/NCBIdevelopset_corpus.txt",'rb') as f:
    for x in f:
        sPipe   = x.split("|")
        sTab    = x.split("\t")

        #if we encounter a new title, update the text, new abstract added to title
        if len(sPipe) > 1:
            if (sPipe[1] == "t"):
                text    = sPipe[2]
                
            if (sPipe[1] == "a"):
                text    +=sPipe[2]
        
        if len(sTab) > 1:
            snip    = sTab[3].strip()
            codes   = sTab[-1].strip().replace(":",'').split("|")
            
            if len(codes[0].split("+")) > 1:
                codes = codes[0].split("+")
                
            for code in codes:
                    
                if not mentionDict.has_key(code):
                    mentionDict[code] = [text,snip]
                else:
                    if text not in mentionDict[code]:
                        mentionDict[code].append(text)
                    mentionDict[code].append(snip)
s=0
for k,v in mentionDict.iteritems():
    s += len(v)
    with open("../data/NCBI/devDocs/"+k,'wb') as f:
        f.write('\n'.join(v))
print "dev set categories: ", len(mentionDict.keys())   
devkeys   = mentionDict.keys()


overlap = 0
for testk in testkeys:
    if (testk in trainkeys) or (testk in devkeys):
        overlap+=1
    else:
        print testk
        
print overlap


textDict = {}
with open("../data/NCBI/NCBItestset_corpus.txt",'rb') as f:
    for x in f:

        sPipe   = x.split("|")
        sTab    = x.split("\t")

        if (x.find("|t") > -1 ) or (x.find("|a") > -1):
            if x.find("\t") > -1:
                print "oops"

        #if we encounter a new title, update the text, new abstract added to title
        if ((len(sPipe) > 1) and ((x.find("|t") > -1) or (x.find("|a") > -1))) :
            if (sPipe[1] == "t"):
                text    = sPipe[2]
                
            if (sPipe[1] == "a"):
                text    +=sPipe[2]
        
        if len(sTab) > 1:

            snip    = sTab[3].strip()
            codes   = sTab[-1].strip().replace(":",'').split("|")
            
            if len(codes[0].split("+")) > 1:
                codes = codes[0].split("+")
                
            for code in codes:
                    
                if not textDict.has_key(text):
                    textDict [text] = [code]
                else:
                    if code not in textDict [text]:
                        textDict [text].append(code)


with open("../data/testText.pickle",'wb') as f:
    cp = cPickle.Pickler(f)
    cp.dump(textDict)