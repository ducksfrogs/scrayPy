from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper('http://ja.dbpedia.org/sparql')
sparql.setQuery(r"""
    SELECT * WHERE {
        ?s rdf:type dbpedia-owl:Museum ;
            prop-ja:所在地 ?address .
            FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
    } ORDER BY ?s
    """)

sparql.setReturnFormat('json')
response = sparql.query().convert()

for result in response['results']['bindings']:
    print(result['s']['value'], result['address']['value'])
