from py2neo import Graph,Node,Relationship
from py2neo.matching import *
import os

from py2neo.matching import NodeMatch
import time

time_start=time.time()

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph("bolt://@localhost:7687")
nodes = NodeMatcher(graph)

file = open("C:\\Users\\yungaroo\\Desktop\\query1.txt",'r')
count = 0
Not_find_count = 0
for line in file:
    count = count+1
    line = line.strip('1234567890. \n')
    print(line)
    names = line.split(" ")
    if(len(names))==1:
        keanu = nodes.match("Resource", ns0__name=Contains(names[0]))
    else:
        keanu = nodes.match("Resource", ns0__name=AND(Contains(names[0]),Contains(names[1])))
    if keanu.first()==None:    
        print("not find")
        Not_find_count=Not_find_count+1
time_end=time.time()
print('totally cost',time_end-time_start)
print('notfind:'+str(Not_find_count))