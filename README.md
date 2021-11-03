# 2021ESWContest_지능형휴머노이드_2016_MECHA
이 문서는 2021 제 19회 임베디드 소프트웨어 경진대회 지능형 휴머노이드 부문 MECHA 팀의 프로젝트입니다.


## Team Members
### MECHA
이름|분장
---|---
김희성|
이원종|
정구열|
차주호|

## Contents
### DeepLearning
  - Object Detection 라벨링 및 학습을 위한 Jupyer Notebook File
  - ABCD Classification 학습 폴더
  - Arrow Corner/Arrow_body Classification 학습 폴더
  - ENSW Classification 학습 폴더

### Robot Control
  - Python Files
    - main file
    - functions
  - Text Files
    - ENSW, ABCD, Arrow 와 관련된 index
  - TFLITE Files
    - TFLite format으로 변환한 ENSW, ABCD, Arrow direction 학습 파일

### Robobasic
  - ROBOBASIC File

### Mobilenet
  - Transfer Learning에 활용한 SSD_Mobilenet_v2_fpmlite_320x320 Model
![MobileNet bakbone architecture](https://user-images.githubusercontent.com/88422973/140049002-18f983de-be18-4e57-9bd8-1b9b8724ea04.png)

  
### FlowChart
  - 전체 순서도
![전체순서도](https://user-images.githubusercontent.com/88422973/140042489-64e4ecd9-6e2a-469f-9321-27c0a4fe6e18.png)

  - 문자 구분 순서도
![문자구분순서도](https://user-images.githubusercontent.com/88422973/140042485-af42daa5-e564-4809-b354-132d91f5ef83.png)

  - 라인트레이싱 순서도
![라인트레이싱순서도](https://user-images.githubusercontent.com/88422973/140042482-65abfeb6-8bfd-4ab9-b7e4-15a8cacfdc41.png)

  - 라인 복귀 순서도
![라인복귀순서도](https://user-images.githubusercontent.com/88422973/140042477-59e2456e-8b0e-48ee-a9b9-3b0ca86773d3.png)

  - 시민 구출 순서도
![시민구출순서도](https://user-images.githubusercontent.com/88422973/140042487-c7677e34-fd6f-4170-a6f5-edf7271fc2ac.png)





## Results
### Detect ABCD
![20211029_17060220](https://user-images.githubusercontent.com/88422973/140038283-30813b91-fbaf-4c36-a96c-29fc6d38476a.png)


### Detect ENSW
![20211029_17063163](https://user-images.githubusercontent.com/88422973/140038288-dc42762e-7c5b-4d8d-ae33-6a946547795a.png)


### Detect Arrow and Corner to distinguish Left or Right
![20211029_17064470](https://user-images.githubusercontent.com/88422973/140038278-5e73de91-0095-4e56-9f5a-e81704d7a5d2.png)

### Line Detect Preprocessing
  - GaussianBlur
  - Convert Color (BGR to HSV)
  - InRange (upper color limit & lower color limit)
  - Canny Edge Detection
  - HoughLine
  - 
