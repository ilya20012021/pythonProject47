import pandas as pd

df = pd.read_csv("kripta.csv")
print(df.iloc[:,1:3])
print("-------------------")
print(df.loc[[1],["group","mark"]])
print("-------------------")
print(df.loc[:, 'group':'mark'])
print("-------------------")
r = df[df["group"].isin(["BISO-01-19","BISO-02-19"])]
print(r.iloc[:,1:])
print("-------------------")
df1 = pd.read_csv("krip.csv")
df2 = pd.concat([df,df1],ignore_index=True)
print(df2.iloc[:,1:])
print("-------------------")
print(df.loc[(df["group"] == "BISO-02-19")|(df["mark"] == "5")])
print("-------------------")
df2.rename(columns={"id":"ID"},inplace=True)
print(df2)
print("-------------------")
print(df2.loc[2:5])
print("-------------------")
print(df2.sort_values("mark",ascending=True))
print("-------------------")
print(df["group"].info())
print("-----------------")
print(df.describe())
print("-----------------")
print(df[["id","mark"]].describe())