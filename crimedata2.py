import os
rflist=os.listdir("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2_original")
print(rflist)
print(rflist[0])
for i in rflist:
    s=''
    data=[]
    rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2_original/" + i
    rf = open(rfstr,"r")
    wf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2/"+str(i),"w+")
    wf.write("관서,검거건수\n")
    rf.readline()
    rf.readline()
    alias = """서울중부경찰서,중구 서울종로경찰서,종로구 서울남대문경찰서,중구 서울서대문경찰서,서대문구 서울혜화경찰서,종로구 서울용산경찰서,용산구 서울성북경찰서,성북구 서울동대문경찰서,동대문구
서울마포경찰서,마포구 서울영등포경찰서,영등포구 서울성동경찰서,성동구 서울동작경찰서,동작구 서울광진경찰서,광진구 서울서부경찰서,은평구
서울강북경찰서,강북구 서울금천경찰서,금천구 서울중랑경찰서,중랑구 서울강남경찰서,강남구 서울관악경찰서,관악구 서울강서경찰서,강서구
서울강동경찰서,강동구 서울종암경찰서,성북구 서울구로경찰서,구로구 서울서초경찰서,서초구 서울양천경찰서,양천구 서울송파경찰서,송파구
서울노원경찰서,노원구 서울방배경찰서,서초구 서울은평경찰서,은평구 서울도봉경찰서,도봉구 서울수서경찰서,강남구"""
    
    alias_dict = dict(aliasset.split(',') for aliasset in alias.split())
    
    while True:
        line = rf.readline().strip()
        data = []
        if not line : break
        data = line.split(',')
        if data[0] != "서울":
            break
        else:
            s = str(alias_dict.get(data[1])) + ',' + data[2] + '\n'
            wf.write(s)
    rf.close()
    wf.close()
#########################################경찰서 이름  구에 맞게 

for i in rflist:
    s=''
    data=[]
    cnt=0
    rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2/" + i
    rf = open(rfstr,"r")
    wf = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2/final/"+str(i),"w+")
    wf.write("관서,발생건수\n")
    rf.readline()
    lines = rf.readlines()
    lines.sort()
    j=0
    while j < len(lines):
        if j+1 != len(lines) and lines[j].strip().split(',')[0] == lines[j+1].strip().split(',')[0]:
            data1 = lines[j].strip().split(',')
            data2 = lines[j+1].strip().split(',')
            s = data1[0] + ',' + str((int(data1[1])+int(data2[1]))) + '\n'
            j = j+1
        else:
            data3 = lines[j].strip().split(',')
            s = data3[0] + ',' + data3[1] + '\n'
        j = j+1
        wf.write(s)
    rf.close()
    wf.close()
    
