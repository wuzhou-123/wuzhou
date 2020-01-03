#coding:gbk
"""
基于Python和Gelphi的《黎明破晓的街道》人物关系图谱构建
作者：吴洲
"""
import codecs
import jieba.posseg as pseg
import jieba
#导入库

names = {}
relationships = {}
lineNames = []
jieba.load_userdict("人物表.txt")                               #读取人物名字
with codecs.open("黎明破晓的街道.txt", 'r', 'ansi') as f:       #打开文本
    for line in f.readlines():
        poss = pseg.cut(line) 
        lineNames.append([])  
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue 
            lineNames[-1].append(w.word)
            if names.get(w.word) is None: 
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1


for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1


with codecs.open("People_node.txt", "w", "ansi") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        if times > 10:
            f.write(name + " " + name + " " + str(times) + "\r\n")


with codecs.open("People_edge.txt", "w", "ansi") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")
                
                
                
f=open('People_edge.txt','r',encoding='ansi')
f2=open('人物表.txt','r',encoding='utf-8').read()
lines=f.readlines()


A=[]
for line in lines:
    A.append([])
    m=line.strip('\n').split(' ')
    for x in m:
        A[-1].append(x)
for items in A:
    if items[0]and items[1] not in f2:
        del(items)
print(A)
f.close()
