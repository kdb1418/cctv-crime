import os
rflist=os.listdir("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/bell_original")
wnf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/bell_number.txt","a")
print(rflist)
print(rflist[0])
checknull=0
for j in rflist:
    s=''
    data=[]
    cnt=0#데이터 갯수
    rfname = 'C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/bell_original/' + j
    rf = open(rfname,'r')
    wf = open('C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/bell/'+str(j),'w+')
    while True:
        line = rf.readline()
        data = []
        if not line : break
        data = line.split(',')
        for i in range(0,3):
            if(data[i]==''):#공백일경우
                checknull=checknull+1
        s = data[6+checknull] + ',' + data[7+checknull] + '\n'
        wf.write(s)
        cnt = cnt+1
        checknull=0
    wnf.write(str(j) + ',' + str(cnt))
    wnf.write('\n')
    rf.close()
    wf.close()
wnf.close()
