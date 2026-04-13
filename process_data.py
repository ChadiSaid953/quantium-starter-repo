import pandas as pd
import glob


files = glob.glob("data/*.csv")


df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)


df = df[df["product"].str.lower() == "pink morsel"]


df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)


df["Sales"] = df["quantity"] * df["price"]

df = df[["Sales", "date", "region"]]


df = df.rename(columns={"date": "Date", "region": "Region"})


df.to_csv("formatted_data.csv", index=False)

print("formatted_data.csv created successfully") 
