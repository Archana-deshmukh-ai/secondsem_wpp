import pandas as pd

df=pd.read_csv(r"C:/TURBOC3/Turbo C++/Python\A11_3_car_prices.csv")
ap=df["asking_prices"]
fp=df["fair_prices"]
#sample data
#ap = pd.Series([10000, 12000, 9000, 13000, 11000])
#fp = pd.Series([15000, 12000, 11000, 14000, 12000])

profitdeal = ap < fp

indices = profitdeal[profitdeal].index
   
print("Good deal car indices:", indices.tolist())
