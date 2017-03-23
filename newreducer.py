#!/usr/bin/python
 
import sys
 
movies_num = {}
prevGenre = None
prevMovie = None
Movies = 0 #initialization
 
for line in sys.stdin:
    req = line.strip().split("\t")
    if len(req) !=2:
       #cancel out unnecessary data
        continue
 
    genre, movieID = req
    if prevGenre and prevGenre != genre:
 
        movies_num[prevGenre] = Movies
        #check condition 
        Movies = 0
 
    Movies += 1 #increment step
 
    prevGenre = genre
 
for key in sorted(movies_num, key=movies_num.get, reverse=True):
    print "{0}\t{1}".format(key, movies_num[key])
 

