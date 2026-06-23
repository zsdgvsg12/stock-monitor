import yfinance as yf

vix = yf.download("^VIX", period="5d")["Close"].iloc[-1]
spy = yf.download("SPY", period="1y")["Close"]

ma50 = spy.rolling(50).mean().iloc[-1]
ma200 = spy.rolling(200).mean().iloc[-1]

print("VIX:", vix)
print("MA50:", ma50)
print("MA200:", ma200)

if vix > 30:
    print("🚨 VIX > 30")

if ma50 > ma200:
    print("📈 Golden Cross")
else:
    print("📉 Death Cross")
