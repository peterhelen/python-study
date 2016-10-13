#-*-coding: gbk -*- 

import  chardet

f1 = open('123.txt','r')
a = f1.read()
print chardet.detect(a)
f1.close()

f2 = open('234.txt','r')
b = f2.read()
print chardet.detect(b)
f2.close()

c = 'aaa'
print chardet.detect(c)

d = '你好'
d = d.decode(chardet.detect(d)['encoding']).encode('gbk')
print d