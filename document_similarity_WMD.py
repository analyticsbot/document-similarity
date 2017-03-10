import difflib
from os import listdir
from os.path import isfile, join
import pandas as pd
from word_mover_distance import similarity
"""
refer :: https://docs.python.org/2/library/difflib.html
"""
import os
print 'all modules imported correctly'

verbose = 0 ## change to 1 for more verbose
#mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents/business/'
#mypath = '/home/ras15116/ravi/Ravi/Individual Sections of IPO documents/business'
mypath = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

new_df = pd.DataFrame()
i = 0
for f1 in onlyfiles:
    print f1
    s1 = open(join(mypath, f1), 'r').read()
    j = 0
    for f2 in onlyfiles:
        if i<=j:
            s2 = open(join(mypath, f2), 'r').read()
            new_df.loc[i, j] = similarity(s1, s2)
        if verbose:
            print 'currently processing', i, ', ', j
        j+=1
    i+=1

new_df.columns = onlyfiles
new_df.index = onlyfiles
print 'all calculations made. Exporting to csv'
new_df.to_csv('document_similarity_business.csv', encoding = 'utf-8')
print 'Export to csv done!'

