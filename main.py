import yfinance as yf

spy = yf.download("SPY", period="5d")

print("DATAFRAME:")
print(spy)

print("COLUMNS:", spy.columns)
print("SHAPE:", spy.shape)
