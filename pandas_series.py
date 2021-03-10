import pandas as pd


grades = pd.Series([87, 100, 94])

print(grades)

grades = pd.Series(98.6, range(3))


print(grades)


a = grades[0]
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()


grades.describe()


grades = pd.Series([87, 100, 94], index=["Wally", "Eva", "Sam"])
print(grades)


grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})


print(grades["Eva"])


print(grades.Wally)


grades.dtype
# outputs the datatype


grades.values
# prints the array
