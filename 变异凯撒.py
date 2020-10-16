k = 5
str = 'afZ_r9VYfScOeO_UL^RWUc'      #ASCII码偏移
for i in str:
 print(chr(ord(i)+k),end="")            #第一位偏移5，第二位偏移6,·····
 k +=1