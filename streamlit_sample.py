import streamlit as st
import yfinance as yf 
import pandas as pd
import numpy as np
import talib 

st.title("Stock Price Prediction App")
# st.header("이건 헤더입니다")
# st.subheader("이건 서브헤더입니다")
st.write("Input a ticker, we'll let you know if tomorrow's return will go up or down")
# st.code("print('Hello, Streamlit!')", language='python')

name = st.text_input("Ticker:")
start_date = st.text_input("Start date (YYYY-MM-DD): ")
end_date = st.text_input("End date (YYYY-MM-DD): ")
if name and start_date and end_date:
    data = yf.download(name, start=start_date, end=end_date)  
    data['Daily Return'] = data['Close'].pct_change() 
    data.columns = data.columns.droplevel('Ticker')

    data["SMA20"] = talib.SMA(data["Close"], timeperiod=20)
    data["EMA60"] = talib.EMA(data["Close"], timeperiod=60)
    data["SMA20"] = talib.RSI(data["Close"], timeperiod=14)
    data["MACD"], data["MACD_SIGNAL"], data["MACD_HIST"] = talib.MACD(data["Close"])
    upper, middle, lower = talib.BBANDS(data["Close"], timeperiod=20)
    data["BB_upper"], data["BB_middle"], data["BB_lower"] = upper, middle, lower
    data["ATR"] = talib.ATR(data["High"], data["Low"], data["Close"], timeperiod=14)

    data.loc[data['Daily Return']>0,'Return'] = 1
    data.loc[data['Daily Return']<=0,'Return'] = 0

    st.line_chart(data['SMA20'])

    # st.write(f"반가워요, {name}님!")

age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, value=25)
st.write(f"입력한 나이: {age}")

if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다!")

color = st.radio("좋아하는 색깔은?", ["빨강", "파랑", "초록"])
st.write(f"당신이 고른 색은 {color}입니다.")

agree = st.checkbox("이용약관에 동의합니다.")
if agree:
    st.write("감사합니다!")

level = st.slider("난이도 설정", 1, 10, 5)
st.write(f"선택한 난이도: {level}")


animal = st.selectbox("좋아하는 동물은?", ["강아지", "고양이", "토끼"])
st.write(f"당신은 {animal}를 좋아하네요!")

hobbies = st.multiselect("취미를 골라보세요", ["독서", "운동", "게임", "음악", "요리"])
st.write(f"선택한 취미: {', '.join(hobbies)}")


file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
if file:
    import pandas as pd
    df = pd.read_csv(file)
    st.dataframe(df)


data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randint(1, 100, size=10)
})

st.line_chart(data)
st.bar_chart(data)




