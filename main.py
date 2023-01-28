import pandas as pd
from tabulate import tabulate
df = pd.DataFrame({})

col = []
n = str(input("Введите число столбцов:"))
if(n.isdigit()):
    n = int(n)
    for i in range(n):
        x = str(input("Введите имя столбца:"))
        col.append(x)

else:
    exit("Ошибка!")


n = str(input("Введите число значений:"))
if(n.isdigit()):
    for k in col:
        val = []
        n = int(n)
        for i in range(n):
            y = str(input("Введите значение:"))
            val.append(y)
        df[k] = val

else:
    exit("Ошибка!")

iny = []
g = len(val)
for i in range(g):
    s = str(input("Введите индекс:"))
    iny.append(s)

df = pd.DataFrame(df,index=iny)


name = str(input("Напишите имя таблицы:"))
df.to_csv(f"{name}.csv")
print(tabulate(df,headers="keys",tablefmt="psql"))