lines=open("file_name.txt")
outstr = open("file_name_output.txt","w")
sample=[]
for i in range(9):
    sample.append(lines.readline().strip())
sample_string=' '.join(sample)
#print(sample_string)
text=sample_string.split(' ')
#print(sample_string.split(' '))
size=len(text)
#print(size)
#print(text[1])
for i in range(0,size-1):
	if text[i]=="V" or text[i]=="V.":
		text[i] = "_" + text[i]
		text[i-1] = text[i-1] + text[i]

for i in range(0,size-1):
	if text[i]=="_V" or text[i]=="_V.":
		text[i]=""

while("" in text) : 
    text.remove("") 
size1=len(text)
#print(size1)


for i in range(0,size1-1):
	if text[i].isupper():
		text[i]="<>" + text[i]
outstr.write(str(text))
lines.close()
outstr.close()
