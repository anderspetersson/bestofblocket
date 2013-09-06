import os
indir = '/Users/Anders/Sites/bestofblocket_project/nyabilder/'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        print f