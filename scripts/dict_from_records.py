# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 08:14:44 2015

Reads in the pickled docLists and combines them, then creates a dictionary.
The argument is the number of words to include in the dictionary.  
This will include the top W most frequent words in the corpus

By default this removes stopwords using the NLTK stopword corpus

@author: jmf
"""

import sys
import cPickle
from helper_funcs   import  *
from os.path        import  isfile
from os             import  listdir


docList =   []

if len(sys.argv) > 1:    
    print sys.argv[1]
    cutoff   =   sys.argv[1]

p   =   "../data/pickledDocs/"
l   =   listdir(p)
fileList    =   [p+f for f in l]
    
for x in fileList:
    #print x
    if isfile(x):
        with open(x,'rb') as f:
            temp =   cPickle.load(f)
            #print type(temp)
            for i,d in temp.iteritems():
                #print d
                docList.append(d)

whole_str   =   ""
for doc in docList:
    whole_str+=doc.lower()
    
print whole_str    
    
print "before"
file_list_to_lda(whole_str,int(cutoff),stop="yes")
print "after"
    

