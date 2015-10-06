# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:53:21 2015

@author: jmf
"""
import cPickle
from os import listdir
import scipy.stats as sts
import numpy as np
import operator
from scipy.spatial.distance import euclidean

with open("../data/out/models/5kwords_200topics/LDA.pickle",'rb') as f:
    lda   = cPickle.load(f)
    
with open("../data/out/models/5kwords_200topics/gamma.pickle",'rb') as f:
    trainGamma = cPickle.load(f)
    
trainVectors = {}
    
for fi in listdir("../data/pickledDocs/"):
    count = 0
    with open("../data/pickledDocs/"+fi,'rb') as d:
        docs    =   cPickle.load(d)
    for k,x in docs.iteritems(): 
        trainVectors[k]     = trainGamma[count]

    
with open("../data/testText.pickle",'rb') as f:
    testset   = cPickle.load(f)

targets     = []
docList     = []
for key,val in testset.iteritems():
    docList.append(key)
    targets.append(val)
    
print docList[0]


(gamma, bound)      = lda.update_lambda(docList) 

for count in range(0,len(gamma)):
    vec1        = gamma[count]
    print vec1

    simDocs     = []
#    for k,vec2 in trainVectors.iteritems():
#        ent     = sts.entropy(vec1,vec2)
#        print vec1
#        print vec2
#        print ent
#        stop=raw_input("")
    print "targets:", targets[count]      
    
    simDocs     = [[euclidean(vec2,vec1), k] for k,vec2 in trainVectors.iteritems()]
    
    print max( np.array(simDocs)[:,0])
    simDocs     = sorted(simDocs,key=operator.itemgetter(0),reverse=True)
    print simDocs[:10]
    stop=raw_input("")



