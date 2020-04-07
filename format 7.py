lines=open("sample.txt")
outstr = open("sample_ouput.txt","w")
flag=0
sample=[]
for i in range(20):
    sample.append(lines.readline().strip())
sample_string=' '.join(sample)#in single line
#print(sample_string)


sample_string=sample_string.split(' n ')
#print(sample_string)

sample_output=[] #this is list

#print(sample_string)
#print(len(sample_string))


for i in sample_string:
	sample_output.append(i.split(" n ")) #split with list and make [] until " n " occurse.
#print(sample_output)
#print(len(sample_string))
#print(len(sample_output))

for i in range(0,len(sample_output)-1): #from down to up putting splitted item.
	r=sample_output[i].pop(-1)
	sample_output[i+1].insert(0,r)
#print(r)
#print(b)   
for i in range(len(sample_output)-1):
    if len(sample_output[i])==0:
        sample_output.pop(i)
    sample_output[i].insert(1,'n')
    sample_output[i]=' '.join(sample_output[i])
#print(sample_output)
"""for i in range(0,len(sample_output)):
	for list in range
"""
print(sample_output[0])
outstr.write(str(sample_output[0]))
lines.close()
outstr.close()
