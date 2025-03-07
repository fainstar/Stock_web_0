# 股票 AI 預測 Web 應用

這是一個基於 Web 的應用，使用蠟燭圖顯示股票數據，並結合 AI 預測的買入與賣出點。該應用的後端使用 **Flask**，前端使用 **Plotly.js** 來渲染交互式圖表。

## 主要功能

- **蠟燭圖**：顯示股票的開盤、收盤、最高與最低價格。
- **買入與賣出標註**：顯示模型建議的買入和賣出點。
- **預測的買入與賣出標註**：顯示 AI 模型的預測買入和賣出點。
- **折線圖**：顯示股票的開盤價與收盤價的變動。

## 技術棧

- **後端**：Python + Flask
- **前端**：HTML, JavaScript (Plotly.js)
- **AI 模型**：訓練的機器學習模型，用於預測買入/賣出點
- **數據**：從 CSV 文件中讀取股票數據

## 安裝與設置

### 1. 克隆倉庫

```bash
git clone https://github.com/your-repository-name.git
cd your-repository-name
