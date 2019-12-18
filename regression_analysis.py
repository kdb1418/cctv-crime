import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

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

print(crime1_data.merge(population_data, on=['관서'], how='inner'))

print(crime1_data['발생건수']/population_data['인구수'])

for i in range(25):
  totalNum.append(int(cctvNumlines[i].strip().split(',')[1])+int(bellNumlines[i].strip().split(',')[1])+int(safeHomeNumlines[i].strip().split(',')[1]))
  cctvNum.append(int(cctvNumlines[i].strip().split(',')[1]))

dfX = pd.DataFrame({
    'totalNum':totalNum,
    'cctvNum':cctvNum
  })

dfY = pd.DataFrame({
    '발생건수/인구수': crime1_data['발생건수']/population_data['인구수']
  })

dfY2 = pd.DataFrame({
    '검거건수': crime2_data['발생건수']
  })

'''Y = dfY['발생건수/인구수']
X = dfX['totalNum']
lr = LinearRegression().fit(X.values.reshape(-1,1),Y)



plt.plot(X, Y, 'o')
plt.plot(X, lr.predict(X.values.reshape(-1,1)))
plt.show()

Y = dfY['발생건수/인구수']
X = dfX['cctvNum']
lr = LinearRegression().fit(X.values.reshape(-1,1),Y)



plt.plot(X, Y, 'o')
plt.plot(X, lr.predict(X.values.reshape(-1,1)))
plt.show()

Y = dfY2['검거건수']
X = dfX['cctvNum']
lr = LinearRegression().fit(X.values.reshape(-1,1),Y)



plt.plot(X, Y, 'o')
plt.plot(X, lr.predict(X.values.reshape(-1,1)))
plt.show()'''


Y = dfY2['검거건수']
X = dfX['totalNum']
lr = LinearRegression().fit(X.values.reshape(-1,1),Y)



plt.plot(X, Y, 'o')
plt.plot(X, lr.predict(X.values.reshape(-1,1)))
plt.show()


