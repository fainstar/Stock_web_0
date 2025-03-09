from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# 載入 CSV 數據
@app.route('/')
def index():
    # 假設CSV文件已經存在於相同目錄下
    CSV_FILE = "B_Data/XGB_3711.csv"  # 請修改為正確的檔案路徑
    df = pd.read_csv(CSV_FILE)  # 載入 CSV

    # 提取所需的資料，並轉換為字典格式
    stock_data = df[['Date', 'Open', 'High', 'Low', 'Close', 'target','predict']]  # 取相關欄位資料

    # 將日期格式轉為 ISO 格式（YYYY-MM-DD）
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

    # 將資料轉換為字典的列表
    stock_data = df.to_dict(orient='records')

    # 提取 target 為 1 和 -1 的點（買入和賣出點）
    buy_points = df[df['target'] == 1][['Date', 'Close']].to_dict(orient='records')
    sell_points = df[df['target'] == -1][['Date', 'Close']].to_dict(orient='records')

    # 假設 CSV 中有 'predict' 列，並提取預測的買入賣出點
    # 如果 CSV 中沒有 predict 列，請確保正確處理此部分
    predicted_buy_points = df[df['predict'] == 2][['Date', 'Close']].to_dict(orient='records')
    predicted_sell_points = df[df['predict'] == 0][['Date', 'Close']].to_dict(orient='records')


    # 傳遞數據到前端模板
    return render_template('index.html', 
                           stock_data=stock_data, 
                           buy_points=buy_points, 
                           sell_points=sell_points,
                           predicted_buy_points=predicted_buy_points, 
                           predicted_sell_points=predicted_sell_points
                           )


if __name__ == '__main__':
    app.run(debug=True)
