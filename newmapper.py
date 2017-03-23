#!/usr/bin/python
 
# MovieID::Title::Genre
   

import sys
 
for line in sys.stdin:
    #splitting the stdin into different data elements
    req = line.strip().split(',') 
    if len(req) == 3:
        #to delete unwanted data
        movieID, title, genre = req
        req2 = genre.split('|')
        #split different genres
        for item in req2:
            print "{0}\t{1}".format(item, movieID)
            #deliver stdout

