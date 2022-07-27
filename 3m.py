import csv
from collections import Counter
with open('Data2.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(float(num))
n=len(newdata)
total=0
for x in newdata:
    total+=x
mean=total/n
print("mean="+str(mean))
newdata.sort()
if n%2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median3=newdata(n//2)
    print(n)
print("median="+str(median))
data=Counter(newdata)
moderange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        moderange["50-60"]+=occurence
    elif 60<float(height)<70:
        moderange["60-70"]+=occurence
    elif 70<float(height)<80:
        moderange["70-80"]+=occurence
range,modeoccurence=0,0
for range1,occurence in moderange.items():
    if occurence>modeoccurence:
        range,modeoccurence=[int(range1.split("-")[0]),int(range1.split("-")[1])],occurence
mode=float((range[0]+range[1])/2)
print(f"mode-->{mode:2f}")
