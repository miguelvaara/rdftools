#!../bin/python3
# coding=utf-8
import urllib.parse, sys, os, rdflib
from rdflib import Graph, Namespace, URIRef, RDF, Literal

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

g = rdflib.Graph()
g.parse(open(sys.argv[1], "r"), format="turtle")

# ******************************************************
# Playground starts, comment the lines you do not need

g.add((URIRef("http://urn.fi/URN:NBN:fi:au:ykl:00.1"), skos["hiddenLabel"], Literal('Hoppa på!', 'sv')))
g.remove((None, skos["broader"], '<http://urn.fi/URN:NBN:fi:au:ykl:muotoluokka'))

# g.query("SELECT * WHERE { ?v ?p ?o }")

# g.query("""
# SELECT * WHERE {
#         ?s ?p ?o .
# }
# """)

query = """PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
DELETE WHERE {
    ?sTest skos:broader <http://urn.fi/URN:NBN:fi:au:ykl:0> . } """



# Playground ends
# ******************************************************

# If you used sparql
g.update(query)

file_to_be_saved = open(sys.argv[2], "w+")
file_to_be_saved.write(g.serialize(format="turtle").decode("utf-8"))
file_to_be_saved.close()

# Some instructions:
# python3 -m venv ./vocabularies
# cd vocabularies/
# ../bin/pip3 install rdflib
# ../bin/pip3 install requests
#./easychanges.py source_file.ttl destination_file.ttl
