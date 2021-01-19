#!/usr/bin/python3
# coding=utf-8
import urllib.request, urllib.parse, urllib.error, sys, pickle, rdflib, json
import requests, time, calendar, datetime, sys
from rdflib import Graph, Namespace, RDF, XSD, OWL, URIRef, plugin, Literal
from urllib.parse import urlencode
import pprint
import os
import sys

owl = Namespace("http://www.w3.org/2002/07/owl#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
ykl = Namespace("http://urn.fi/URN:NBN:fi:au:ykl:")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
dct = Namespace('http://purl.org/dc/terms/')
isothes = Namespace('http://purl.org/iso25964/skos-thes#')
foaf = Namespace('http://xmlns.com/foaf/0.1/')
ysa = Namespace('http://www.yso.fi/onto/ysa/')

# Multipurpose graph
g = rdflib.Graph()


# Opening the file for your manipulations
# If the RDF file is on Internet
# result = g.parse("http://...")
result = g.parse(file = open(sys.argv[1], "r"), format="turtle")

# Functions area starts

def how_many_statements():
    return "{} statements".format(len(g))

def list_arguments():
    print(sys.argv[1])
    print(sys.argv[2])

# If you are wondering is there life in the graph
def is_there_graph():
    for subj, pred, obj in g:
        if (subj, pred, obj) not in g:
            raise Exception("For one reason or another the triples are missing")

# If you want to print out statements in pretty mode
def print_statemens_out(): 
    for statement in g:
        pprint.pprint(statement)

# Functions area ends

# Playground starts

print(how_many_statements())
list_arguments()
is_there_graph()
how_many_statements()

# Playground ends

# What ever you did, it should be saved to the file

file_to_be_saved = open(sys.argv[2], "w+")

file_to_be_saved.write(g.serialize(format="turtle").decode("utf-8"))

file_to_be_saved.close()

