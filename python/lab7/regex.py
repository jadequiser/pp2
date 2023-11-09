import re
with open('row.txt') as file:
    soderzhimoe = file.read()
# 1
res1 = re.findall("а.*б", soderzhimoe)
print(res1)

# 2
res2=re.findall("аб{2,3}", soderzhimoe)
print(res2)

# 3
res3=re.findall('^[a-z]+_[a-z]+$', soderzhimoe)
print(res3)

# 4
pattern = '[A-Z][a-z]+'
res4=re.findall(pattern, soderzhimoe)
print(res4)

# 5
pattern = r'а.*б'
res5=re.findall(pattern, soderzhimoe)
print(res5)

# 6
res6=re.sub(r'[ ,.]', ':', soderzhimoe)
print(res6)

# 7
words = soderzhimoe.split('_')
capwords = [word.capitalize() for word in words]
res7 = ''.join(capwords)
print(res7)

# 8
res8=re. findall('[A-Z][^A-Z]*', soderzhimoe)
print(res8)

# 9
res9=re.sub(r"(\w)([A-Z])", r"\1 \2", soderzhimoe)
print(res9)

# 10
words = re.findall(r'[a-zA-Z][^A-Z]*', soderzhimoe)
capwords = '_'.join(map(str.lower, words))
print(capwords)






















