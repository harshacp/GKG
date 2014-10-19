#!/usr/bin/python
import rdflib
g=rdflib.Graph()
g.load('test.xml')

for s,p,o in g:
	print p," : ",o