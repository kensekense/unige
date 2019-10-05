# 1. Modelling

Represent the following facts with RDF graphs

p1 and p2 are political parties
c1, c2, c3, c4 were candidates for p1
d1, d2, d3 were candidates for p2
c3, c1 have been elected (in this order) for p1
no one from p2 has been elected
elected candidates have become members of the parliament (MP)

# 2. Meta modelling

In RDF there is no direct construct to add information to a triple (metadata). However there are  situations in which we would like to have this possibility. For example

to define the validity time of a triple, e.g. “The population of Geneva is 453779 in 2010”
to define the validity space (location)
to add provenance information, e.g. “IBM was founded in 1911 according to Wikipedia”
to add a confidence or certainty level
Find two different ways to represent these additional pieces of information. In other words, find ways to represent quadruples (subject, predicate, object, additional-info) with triples.

# 3. Transformation to RDF

Create algorithms to

transform a spreadsheet (made of cells organized in rows and columns and containing numbers or strings or formulae) into an RDF graph.
transform a relational database (made of tables, rows, columns, keys, foreign key) into an RDF graph
transform an HTML document into an RDF graph that represents the structure and content of the document
The transformations must be lossless, i.e. it must be possible to go back to the original data.
