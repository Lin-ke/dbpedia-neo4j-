#!/bin/bash
export NEO4J_HOME=${PWD}
export NEO4J_IMPORT="${NEO4J_HOME}/neo4j-server/import"
export NEO4J_DB_DIR=$NEO4J_HOME/neo4j-server/data/databases/graph.db
ulimit -n 65535

echo "Importing"
for file in ${NEO4J_IMPORT}/*.ttl*; do
    # Extracting filename
    echo $file
    filename="$(basename "${file}")"
    echo "Importing $filename from ${NEO4J_HOME}"
    ${NEO4J_HOME}/neo4j-server/bin/cypher-shell -u neo4j -p 'admin' "CALL  n10s.rdf.import.fetch(\"file://${NEO4J_IMPORT}/$filename\",\"Turtle\");"
done