# 实验文件夹内容
In ./:\
query1.txt: 错误的作家名列表\
query2.txt: 正确的作家名列表\
实验报告.pdf \
In ./Btree/:\
Neo4j用的B-树数据结构(java)\
In ./DBpedia/:\
导入dbpedia需要的文件。\
In ./test/:\
work1.py错误人名搜索\
work2.py正确人名搜索

# DBpedia导入Neo4j
学号：1190201024
姓名：魏宇鹏


0.OpenJDK 11。在ubuntu下可以使用


```

sudo apt-get install default-jdk

```



1.获取Neo4j :终端输入命令


```

./get-neo4j.sh

```


2.下载DBpedia文件，解压缩，准备导入。

请注意：#注释掉的文件将不被下载。如果有自己的需求删去“#”

```

./download-dbpedia.sh dbpedia_files.txt

```


3.加载数据文件
```

./import-dbpedia.sh

```


4.现在就可以使用浏览器查看了：


-计数节点

```

${NEO4J_HOME}/bin/cypher-shell -u neo4j -p 'admin' "MATCH (r:Resource) RETURN COUNT(r)"

```


-数边

```

${NEO4J_HOME}/bin/cypher-shell -u neo4j -p 'admin' "MATCH (r1:Resource)-[l]->(r2:Resource) RETURN COUNT(l)"

```
# 使用须知：
导入数据后，请您将各个文件中的地址改成自己的地址。
# ：新年快乐