from os import listdir
from os.path import isfile, join
import pandas as pd
import distance
import os
print 'all modules imported correctly'

verbose = 0 ## change to 1 for more verbose
mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'

## get the list of all files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))][:3]

## read all the text files so as not to read it again and again
fileData = [ ' '.join(f.read().strip().split()[1:]) for f in onlyfiles]

## intialize an empty dataframe
new_df = pd.DataFrame()

## iterate between files and find the similarity metric
i = 0
for f1 in fileData:
    #print 'currently processing ', onlyfiles[i]
    s1 = open(join(mypath, f1), 'r').read()
    j = 0
    for f2 in fileData:
        if i<=j:
            new_df.loc[i, j] = distance.nlevenshtein(f1.lower().strip(),f2.lower().strip(), method = 2)
        if verbose and (j%100 == 0):
            print 'currently processing', onlyfiles[i], ' with ', onlyfiles[j]
        j+=1
    i+=1

new_df.columns = onlyfiles
new_df.index = onlyfiles
print 'all calculations made. Exporting to csv'
new_df.to_csv('document_similarity_levenstein_business.csv', encoding = 'utf-8')
print 'Export to csv done!'

