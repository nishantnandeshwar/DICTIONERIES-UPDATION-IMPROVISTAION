lines=open("file_name.txt")
outstr = open("output-file_name.txt","w")
sample=[]
#rang=len(lines)
for i in range(15584):
    sample.append(lines.readline().strip())
sample_string=' '.join(sample)
#print(sample_string)
text=sample_string.split(' ,')
#print(sample_string.split(' ,'))
size=len(text)
#print(text[191])

for i in range(0,size-1):
	if text[i]=='n'or text[i]=="n." or text[i]=="a" or text[i]=="a." or text[i]=="adv" or text[i]=="adv." or text[i]=="n&a." or text[i]=="prep." or text[i]=="vi." or text[i]=="vi" or text[i]=="u." or text[i]=="u" or text[i]=="vt." or text[i]=="vt":
		text[i]=" " + text[i]
		text[i-1]="<>" + text[i-1]
	
str1 = ""
for ele in text:
	str1 += ele + " " 

str2 = str1.split("<>")

outstr.write(str(str2))
lines.close()
outstr.close()

