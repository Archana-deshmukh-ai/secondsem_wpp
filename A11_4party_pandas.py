import pandas as pd
import numpy as np
#sample data
#data = {
#    "day": range(1, 11),
#    "John": [True, False, True, False, True, False, False, True, False, True],
#    "Judy": [False, True, True, False, False, False, True, True, False, True]
#}
#
#df = pd.DataFrame(data)
df=pd.read_csv(r"C:/TURBOC3/Turbo C++/Python/A11_4_schedule_with_party.csv")

#already given so remove the column named party
df=df.drop("party",axis=1)

df["party"] = (df["John_visits"] & df["Judy_visits"]).astype(int)

df["days_till_party"] = 0

for i in range(len(df)):
    for j in range(i, len(df)):
        if df.loc[j, "party"] == 1:
            df.loc[i, "days_till_party"] = j - i
            break 
print(df.to_string(index=False))
