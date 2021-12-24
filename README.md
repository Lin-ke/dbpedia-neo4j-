# Import DBpedia 2020 into Neo4j v4 with Neosemantics

0. Prerequisite: OpenJDK 11. If you run ubuntu with root you can use

   ```
   apt-get install default-jdk
   ```
   
   Otherwise, consider using docker : https://hub.docker.com/_/openjdk
   
   Third option, not recommended, you can install Java in userspace, you will have to play around with terminal configuration. Here is a starting point under "Installing OpenJDK Manually": https://dzone.com/articles/installing-openjdk-11-on-ubuntu-1804-for-real


1. Get Neo4j v4.1.X Community server and install Neosemantics plugin, also configure neosemantics and add required index
    
    ```
    ./get-neo4j.sh
    ```

2. Download DBpedia Files, uncompress, ready to be imported

   ```
   ./download-dbpedia.sh dbpedia_files.txt
   ```
   
3. Load the data files
   **Notice 1:** DBpedia contains malformed IRIs, I've done my best to exclude those, but still some can pass through. A better solution is needed.
   **Notice 2:** DBpedia has multi-valued properties with inconsistent types. At the moment `handleMultival: "OVERWRITE"` could be an option.
   
   ```
   ./import-dbpedia.sh
   ```
   
4. Test data is all right:

     - Count nodes
        ```
        ${NEO4J_HOME}/bin/cypher-shell -u neo4j -p 'admin' "MATCH (r:Resource) RETURN COUNT(r)"
        ```
        
     - Count edges
        ```
        ${NEO4J_HOME}/bin/cypher-shell -u neo4j -p 'admin' "MATCH (r1:Resource)-[l]->(r2:Resource) RETURN COUNT(l)"
        ```

     - Distinct relationship types
        ```
        ${NEO4J_HOME}/bin/cypher-shell -u neo4j -p 'admin' "CALL db.relationshipTypes() YIELD relationshipType RETURN relationshipType"
        ```

     - Example node-edges
        ```
        ${NEO4J_HOME}/bin/cypher-shell -u neo4j -p 'admin' "MATCH (r1:Resource)-[l]->(r2:Resource) RETURN r1, l, r2 LIMIT 20"
        ```
