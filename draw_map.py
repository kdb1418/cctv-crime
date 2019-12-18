import os
import json
import folium
import numpy as np
import pandas as pd
import itertools

geo_path = '02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

'''cctvflist = os.listdir("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv")
cctvlatlon = []
for i in cctvflist:
  rfstr = "C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv/" + i
  rf = open(rfstr,"r")
  rf.readline()
  rf.writelines
  line = rf.readline()
  while line != '':
    cctvlatlon.append(line.strip().split(','))
    line = rf.readline()
  rf.close()

print(cctvlatlon)'''

cctvNumFile = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv_number.txt", "r")
bellNumFile = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/bell_number.txt", "r")
safeHomeNumFile = open("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/safehome_number.txt", "r")

cctvNumlines = cctvNumFile.readlines()
bellNumlines = bellNumFile.readlines()
safeHomeNumlines = safeHomeNumFile.readlines()
cctvNum = []
totalNum = []
cctvNumFile.close()
bellNumFile.close()
safeHomeNumFile.close()

crime1_data = pd.read_csv("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime1/final/전국 경찰서별 범죄발생 현황_(2018년).csv", engine="python",encoding="cp949")
crime2_data = pd.read_csv("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2/final/전국 경찰서별 범죄검거 현황_(2018년).csv", engine="python",encoding="cp949")
population_data = pd.read_csv("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/population/final/LOCAL_PEOPLE_GU_201812.csv", engine="python",encoding="cp949")


for i in range(25):
  totalNum.append(int(cctvNumlines[i].strip().split(',')[1])+int(bellNumlines[i].strip().split(',')[1])+int(safeHomeNumlines[i].strip().split(',')[1]))
  cctvNum.append(int(cctvNumlines[i].strip().split(',')[1]))

crime1_population = pd.DataFrame({
    '관서':crime1_data['관서'],
    '사건발생/인구':crime1_data['발생건수']/population_data['인구수']
  })

crime2_crime1 = pd.DataFrame({
    '관서':crime2_data['관서'],
    '사건검거/사건발생':crime2_data['발생건수']/crime1_data['발생건수']
  })

cctv = pd.DataFrame({
    '관서':crime1_data['관서'],
    'cctv':cctvNum
  })

total = pd.DataFrame({
    '관서':crime1_data['관서'],
    'total':totalNum
  })


crime1_population_map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                tiles='stamentoner')
folium.Choropleth(geo_data=geo_str,
               data = crime1_population,
               columns = ['관서', '사건발생/인구'],
              fill_color = 'PuRd',
              key_on='feature.id').add_to(crime1_population_map)
crime1_population_map.save("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime1_population.html")


crime2_crime1_map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                tiles='stamentoner')
folium.Choropleth(geo_data=geo_str,
               data = crime2_crime1,
               columns = ['관서', '사건검거/사건발생'],
              fill_color = 'OrRd',
              key_on='feature.id').add_to(crime2_crime1_map)
crime2_crime1_map.save("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/crime2_crime1.html")


cctv_map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                tiles='stamentoner')
folium.Choropleth(geo_data=geo_str,
               data = cctv,
               columns = ['관서', 'cctv'],
              fill_color = 'PuBu',
              key_on='feature.id').add_to(cctv_map)
cctv_map.save("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/cctv.html")

total_map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                tiles='stamentoner')
folium.Choropleth(geo_data=geo_str,
               data = total,
               columns = ['관서', 'total'],
              fill_color = 'BuPu',
              key_on='feature.id').add_to(total_map)
total_map.save("C:/Users/김다빈/Desktop/데이터크롤링/프로젝트/total.html")
