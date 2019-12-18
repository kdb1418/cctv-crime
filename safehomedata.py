import os
rflist=os.listdir("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/safehome_original")
print(rflist)
wnf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/safehome_number.txt","a")
print(rflist[0])
for i in rflist:
    s=''
    data=[]
    cnt=0
    rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/safehome_original/" + i
    rf = open(rfstr,"r")
    wf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/safehome/"+str(i),"w+")
    while True:
        line = rf.readline()
        data = []
        if not line : break
        data = line.split(',')
        s = data[6] + ',' + data[7] + '\n'
        wf.write(s)
        cnt=cnt+1
    wnf.write(str(i) + ',' + str(cnt))
    wnf.write('\n')
    rf.close()
    wf.close()
wnf.close()
