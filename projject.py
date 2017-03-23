# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:00:05 2016

@author: Sangeet
"""
#mapper
import codecs
exampledata = []
with codecs.open('movie_data.txt',encoding='utf-16')as source:
    for line in source:
        fields = line.strip(" ").split('\t')
        exampledata.append(fields)

exampleData = exampledata[1:]

director_name = []
movie_title = []
actor1_name = []
rating = []
for row in exampleData:
    director = row[1].encode('utf-8')
    director_name.append(director)
    movie = row[11].encode('utf-8')
    movie_title.append(movie)
    actor = row[10].encode('utf-8')
    actor1_name.append(actor)
    score = float(row[25])
    rating.append(score)

print rating[:5]
print director_name[:5]
print actor1_name[:5]
print movie_title[:5]

#reducer

dire = raw_input("Who is the director? ")
act = raw_input("who is the actor? ")

for word in director_name:
    if dire == word:
        position = director_name.index(word)
        rat1 = rating[position]

print (dire, rat1)

for word in actor1_name:
    if act == word:
        position = actor1_name.index(word)
        rat2 = rating[position]

print (act, rat2)
print ('pred', (rat1+rat2)/2)
