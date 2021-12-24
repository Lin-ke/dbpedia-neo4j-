#coding:utf-8
from py2neo import Graph,Node,Relationship
import os
##连接neo4j数据库，输入地址、用户名、密码
graph = Graph("bolt://@localhost:7687")
tx = graph.begin()
path = "D://neo4j-community-4.3.6-windows/neo4j-community-4.3.6/import/"#请改成您的地址
for file in os.listdir(path):
    print("import:"+file)
    tx.run("CALL n10s.rdf.import.fetch(\"file:///"+path+file+"\",\"Turtle\");")
