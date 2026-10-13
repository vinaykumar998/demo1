import pandas as pd

data = (

"Study_Hours": [2, 5, 4, 7, 3],

"Attendance": [60, 80, 75, 90, 65),

"Study_Mode": ["Online", "Classroom", "Online", "Classroom", "Online"], "Marks": [45, 70, None, 90, 55]

df = pd.DataFrame(data)

print("Original dataset:")

print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].median()) df = pd.get_dummies(df, columns=["Study_Mode"], dtype=int) print("Prepared dataset:")

print(df)