lines=open(“file_name")
flag=0
sample=[]
for i in range(100):
    sample.append(lines.readline().strip())
sample_string=' '.join(sample)
sample_string=sample_string.split('संज्ञा')
sample_output=[]
for i in sample_string:
    sample_output.append(i.split("।"))
for i in range(0,len(sample_output)-1):
    r=sample_output[i].pop(-1)
    sample_output[i+1].insert(0,r)
print(len(sample_output))    
for i in range(len(sample_output)-1):
    if len(sample_output[i])==0:
        sample_output.pop(i)
    sample_output[i].insert(1,'संज्ञा')
    sample_output[i]=' '.join(sample_output[i])
print(sample_output)
 
 
