import pandas as pd

data = pd.read_csv("Titanic-Dataset.csv")

# adult_names = data.loc[data["Age"] > 18, "Name"]
# print(adult_names)

# print(data.iloc[9:25, 2:5])

# data.iloc[0:3, 3] = "Pulkit Chawla"
# print(data["Name"])

# data["Test"] = data["Fare"] + 2
# data["Test2"] = data["Fare"] * data["Pclass"]

# data_renamed = data.rename(
#     columns = {
#         "Pclass": "Passenger Class",
#         "Sibsp": "Sibling"
#     }
# )

# print(data_renamed.info())

# print(data["Age"].mean())
# print(data[["Age", "Fare"]].mean())
# print(data.agg({
#     "Age": ["min", "max", "median"],
#     "Fare": ["min", "max", "median"]
# }))

# print(data[["Sex", "Age"]].groupby("Sex").mean())
# print(data.groupby("Sex")["Age"].mean())
# print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

# print(data["Pclass"].value_counts())
# print(data.groupby("Pclass")["Pclass"].count())

print(data.sort_values(by = "Age", ascending = False))
print(data[["Name","Age"]].head(10))