# cctv-crime
***

## directory
* bell - 가공한 데이터
* bell_original - 비상벨 데이터셋
* cctv - 가공한 데이터
* cctv_origin - cctv 데이터셋
* crime1 - 범죄발생데이터
* crime1_origin - 범죄발생 데이터셋
* crime2 - 범죄검거데이터
* crime2_origin - 범죄검거 데이터셋
* population - 유동인구 데이터
* population_origin - 유동인구 데이터셋
* safehome - 안전지킴이집 데이터
* safehome_origin - 안전지킴이집 데이터셋

## .py
* belldata.py - 벨 가공
* cctvdata.py - cctv 가공
* crimedata1.py - 범죄발생 데이터 가공
* crimedata2.py - 범죄검거 데이터 가공
* populationdata.py - 유동인구 데이터 가공
* safehomedata.py - 안전지킴이 집 데이터 가공
* regression_analysis.py - 분석
* draw_map.py - folium map

## .html
* cctv.html - 각 자치구별 cctv 운영량에 따른 맵
* total.html - 각 자치구별 cctv+비상벨+지킴이집 운영량에 따른 맵
* crime1_population.html - 각 자치구별 범죄발생량/유동인구
* crime2_crime1.html - 각 자치구별 검거량/범죄발생량

## .text
* cctv_number - cctv 갯수
* bell_number - 벨 갯수
* safehome_number - 지킴이집 갯수
