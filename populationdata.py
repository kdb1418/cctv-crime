import os
rflist=os.listdir("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/population_original")
print(rflist)
print(rflist[0])
for i in rflist:
    s=''
    data=[]
    rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/population_original/" + i
    rf = open(rfstr,"r")
    wf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/population/"+str(i),"w+")
    wf.write("자치구,인구수\n")
    rf.readline()
    alias = """11110,종로구 11140,중구 11170,용산구 11200,성동구 11215,광진구 11230,동대문구 11260,중랑구
11290,성북구 11305,강북구 11320,도봉구 11350,노원구 11380,은평구 11410,서대문구 11440,마포구 11470,양천구
11500,강서구 11530,구로구 11545,금천구 11560,영등포구 11590,동작구 11620,관악구 11650,서초구 11680,강남구 11710,송파구 11740,강동구"""
    
    alias_dict = dict(aliasset.split(',') for aliasset in alias.split())
        
    while True:
        line = rf.readline().strip()
        data = []
        if not line : break
        data = line.split(',')
        if int(data[0].strip('"'))<20181201 or int(data[0].strip('"'))>20181207:
            break
        else:
            s = str(alias_dict.get(data[2].strip())) + ',' + data[3] + '\n'
            wf.write(s)
    rf.close()
    wf.close()
    
for i in rflist:
    s=''
    data=[]
    cnt=0
    rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/population/" + i
    rf = open(rfstr,"r")
    wf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/population/final/"+str(i),"w+")
    wf.write("자치구,인구수\n")
    lines = rf.readlines()
    lines = lines[1:]
    lines.sort()
    j=0
    while j+167 < len(lines):
        if j+168 != len(lines) and lines[j].strip().split(',')[0] == lines[j+1].strip().split(',')[0]:
            sum = 0
            for k in range(168):
                sum = sum + int(lines[j+k].strip().split(',')[1])
            avg = int(sum/168)
            s = lines[j].strip().split(',')[0] + ',' + str(avg) + '\n'
            j = j+168
        else:
            data3 = lines[j].strip().split(',')
            s = data3[0] + ',' + data3[1] + '\n'
        j = j+1
        wf.write(s)
    rf.close()
    wf.close()
    
