
with open('pervik.txt','r') as pervik, open('vtorik.txt','a') as vtorik: 
	for line in pervik: 
			vtorik.write(line)

print("pervik was copied into vtorik")