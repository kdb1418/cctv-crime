import os
rflist=os.listdir("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv_original")
print(rflist)
wnf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv_number.txt","a")
print(rflist[0])
for i in rflist:
    s=''
    data=[]
    cnt=0
    rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv_original/" + i
    rf = open(rfstr,"r")
    wf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv/"+str(i),"w+")
    wf.write("위도,경도\n")
    while True:
        line = rf.readline()
        data = []
        if not line : break
        data = line.split(',')
        if data[3] == "생활방범" or data[3] == "다목적":
            s = data[10] + ',' + data[11] + '\n'
            wf.write(s)
            cnt=cnt+1
    wnf.write(str(i) + ',' + str(cnt))
    wnf.write('\n')
    rf.close()
    wf.close()
wnf.close()
