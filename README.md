# Taiwan Weather Web

一個使用中央氣象局（CWA）開放資料的天氣查詢工具，提供全台 22 縣市未來 36 小時天氣預報
透過 Python + Flask 架設網頁介面

---

## 快速開始
```bash

安裝依賴套件
pip install -r requirements.txt

啟動 Flask 網頁伺服器
python app.py
```
打開瀏覽器前往：http://localhost:5000
即可查詢任一縣市天氣！
功能介紹
查詢 CWA 提供之 36 小時天氣預報（全台 22 縣市）

### 城市下拉選單選擇

顯示預測時間、天氣狀況、氣溫範圍

## 技術架構

| 類別       | 技術                          |
|------------|-------------------------------|
| 前端       | HTML + CSS (Jinja2 Template) |
| 後端       | Python + Flask               |
| 第三方 API | 中央氣象局 CWA Open Data     |


## 專案結構
```bash
weather-checker-selenium/
├── app.py                  # Flask 主程式
├── weather_fetcher_cwa.py  # 查天氣邏輯
├── templates/
│   └── index.html          # 前端畫面
├── requirements.txt
├── .gitignore
└── README.md
```
## 授權 License
本專案使用 MIT 授權
氣象資料來源：中央氣象局開放資料平台

## 作者

本專案由samuel開發，用於練習串接第三方 API 與 Flask 架構開發。
