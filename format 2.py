lines=open("file_name.txt")
outstr = open("file_name_ouput.txt","w")
flag=0
sample=[]
for i in range(20):
    sample.append(lines.readline().strip())
sample_string=' '.join(sample)

sample_string=sample_string.split(' n ')

sample_output=[] #this is list

for i in sample_string:
	sample_output.append(i.split(" n ")) #split with list and make [] until " n " occurse.
	
for i in range(0,len(sample_output)-1): #from down to up putting splitted item.
	r=sample_output[i].pop(-1)
	sample_output[i+1].insert(0,r)
   
for i in range(len(sample_output)-1):
    if len(sample_output[i])==0:
        sample_output.pop(i)
    sample_output[i].insert(1,'n')
    sample_output[i]=' '.join(sample_output[i])

print(sample_output[0])
outstr.write(str(sample_output[0]))
lines.close()
outstr.close()
