from os import listdir
from os.path import isfile, join
import pandas as pd
import distance
import os
import difflib
print 'all modules imported correctly'

verbose = 0 ## change to 1 for more verbose
mypath = 'C:\\Users\\Hari\\Dropbox\\IPO_analysis_sourcecode\\IPO_Project\\Data\\Individual_Sections_of_IPO_documents\\newuseofproceeds'
mypath = '/home/ras15116/ravi/Ravi/Individual_Sections_of_IPO_documents/mda'
## get the list of all files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

## read all the text files so as not to read it again and again
fileData = [ ' '.join(open(join(mypath, f), 'r').read().split()[1:]) for f in onlyfiles]

## intialize an empty dataframe
new_df = pd.DataFrame()

## iterate between files and find the similarity metric
i = 0
for f1 in fileData:
    j = 0
    for f2 in fileData:
        if i == j:
            new_df.loc[i, j] = 1
            
        if verbose: #and (j%100 == 0):
            print 'currently processing', onlyfiles[i], ' with ', onlyfiles[j]
            
        if i != j :
            new_df.loc[i, j] = difflib.SequenceMatcher(None,f1 , f2).ratio()
        
        j+=1
    i+=1

new_df.columns = onlyfiles
new_df.index = onlyfiles
print 'all calculations made. Exporting to mda_similarity_difflib_serial.csv'
new_df.to_csv('mda_similarity_difflib_serial.csv', encoding = 'utf-8')
print 'Export to csv done!'


