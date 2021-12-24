# 选题：29
【X=1.0】如何为知识图谱建立索引？ 【题目背景】由于大数据的出现，计算能力的升级，涌现出以知识图谱为代表的一批大数据 人工智能时代的产物。知识图谱的查询一直受到学术界和工业界的广泛关注，知识查询的效 率与知识图谱的索引密切相关。 【数据来源】Yago 知识图谱：https://www.mpi-inf.mpg.de/departments/databases-andinformation-systems/research/yago-naga/yago/downloads/ DBPedia 知识图谱：https://wiki.dbpedia.org/develop/datasets 【设计要求】给定知识图谱存储结构为图数据库，如 Neo4j 或 gStore，利用所给 Yago 知识 图谱和 DBPedia 知识图谱，设计知识图谱索引结构，要求（1）基于索引的查询效率尽可能 高；（2）保证知识图谱查询的准确率；（3）索引的存储空间不宜过大。 【实验要求】记录（1）基于索引的查询效率提升程度；（2）查询的准确率；（3）索引结构 的存储空间

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

./get-neo.sh

```


2.下载DBpedia文件，解压缩，准备导入。

请注意：#注释掉的文件将不被下载。如果有自己的需求删去“#”

```

./dw-d.sh dbpedia_files.txt

```


3.加载数据文件
```

./impt.sh

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
请至少预留40G磁盘空间~
# ：新年快乐
